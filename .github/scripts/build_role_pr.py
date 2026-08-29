#!/usr/bin/env python3
"""Turn an approved "Submit a role" issue into a role folder + PR.

Triggered by .github/workflows/add-role.yml when the "approved" label is
added to an issue. Reads the issue via `gh`, parses the Issue Forms fields,
builds roles/<lang>/<code>/{README,prompt-*,skill-*}.md, and opens a PR.
"""

import json
import os
import re
import subprocess
import sys

REPO = os.environ["REPO"]
ISSUE_NUMBER = os.environ["ISSUE_NUMBER"]

LANG_MAP = {
    "English": "en",
    "Ukrainian": "ua",
    "German": "de",
    "Spanish": "es",
    "French": "fr",
}

SEAT_MAP = {
    "Participant (seats 1-4)": "participant (1-4)",
    "Orchestrator (seat 5)": "orchestrator (seat 5)",
    "Works as either": "participant or orchestrator",
}

SEAT_KEY_MAP = {
    "Participant (seats 1-4)": "participant",
    "Orchestrator (seat 5)": "orchestrator",
    "Works as either": "either",
}

# A role in language X and "the same" role in language Y are treated as two
# separate roles: written by different people, they evolve independently and
# one may be better than the other. So each role is listed in exactly one
# index - the one for its own language. Languages without an index page of
# their own share OTHER_INDEX until they earn a dedicated page (at which point
# they just get a line here, no code change).
LANG_INDEX = {
    "en": "roles/README.md",
    "ua": "roles/README.ua.md",
}
OTHER_INDEX = "roles/OTHER-LANGUAGES.md"

# Language the index page itself is written in, used only to word the Seat
# column. OTHER_INDEX is written in English.
INDEX_LANG = {
    "roles/README.md": "en",
    "roles/README.ua.md": "ua",
    OTHER_INDEX: "en",
}

TABLE_SEAT = {
    "en": {"participant": "Participant", "orchestrator": "Orchestrator", "either": "Participant or Orchestrator"},
    "ua": {"participant": "Учасник", "orchestrator": "Оркестратор", "either": "Учасник або Оркестратор"},
}

# Ukrainian -> Latin, close to the official transliteration (resolution 55/2010).
# Used only as a fallback when "Role code" is empty/non-Latin.
UA_TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g", "д": "d", "е": "e",
    "є": "ie", "ж": "zh", "з": "z", "и": "y", "і": "i", "ї": "i", "й": "i",
    "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
    "с": "s", "т": "t", "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch",
    "ш": "sh", "щ": "shch", "ь": "", "ю": "iu", "я": "ia", "'": "", "’": "",
}


def run(cmd, **kwargs):
    print("+", " ".join(cmd), file=sys.stderr)
    return subprocess.run(cmd, check=True, text=True, **kwargs)


def slugify_ascii(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def transliterate(text: str) -> str:
    return "".join(UA_TRANSLIT.get(ch, ch) for ch in text.lower())


def make_code(role_code_raw: str, role_name: str) -> str:
    code = slugify_ascii(role_code_raw)
    if code:
        return code
    code = slugify_ascii(transliterate(role_name))
    return code or "role"


def parse_issue_body(body: str) -> dict:
    parts = re.split(r"^### (.+)$", body, flags=re.MULTILINE)
    fields = {}
    for i in range(1, len(parts), 2):
        label = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        if content == "_No response_":
            content = ""
        fields[label] = content
    return fields


def comment(text: str) -> None:
    run(["gh", "issue", "comment", ISSUE_NUMBER, "-R", REPO, "--body", text])


def escape_cell(text: str) -> str:
    text = text.replace("|", "\\|")
    text = re.sub(r"\s+", " ", text).strip()
    # 200, not 140: a full sentence in Ukrainian or German runs longer than in
    # English, and 140 was cutting them mid-word.
    if len(text) > 200:
        text = text[:199].rstrip() + "…"
    return text


def update_roles_index(lang: str, slug: str, role_name: str, purpose: str, seat_raw: str):
    """Add a row for this role to the index for its language.

    Exactly one index per role: `en` and `ua` have their own page, every other
    language shares OTHER_INDEX. Name and description go in as written - they
    are never translated - so each page stays in its own language.

    Returns the index file changed, or None.
    """
    path = LANG_INDEX.get(lang, OTHER_INDEX)
    if not os.path.isfile(path):
        return None

    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    sep_idx = None
    for i, line in enumerate(lines):
        if i > 0 and re.match(r"^\|[-\s|]+\|$", line) and lines[i - 1].lstrip().startswith("|"):
            sep_idx = i
            break
    if sep_idx is None:
        return None

    seat_key = SEAT_KEY_MAP.get(seat_raw, "participant")
    index_lang = INDEX_LANG.get(path, "en")
    seat_col = TABLE_SEAT.get(index_lang, TABLE_SEAT["en"]).get(seat_key, seat_key)
    row = (
        f"| {escape_cell(role_name)} | {escape_cell(purpose)} | "
        f"{seat_col} | [{lang}]({lang}/{slug}/) |"
    )
    lines.insert(sep_idx + 1, row)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return path


def main() -> None:
    raw = run(
        ["gh", "issue", "view", ISSUE_NUMBER, "-R", REPO, "--json", "body,author"],
        capture_output=True,
    ).stdout
    data = json.loads(raw)
    username = data["author"]["login"]
    fields = parse_issue_body(data["body"])

    role_name = fields.get("Role name", "").strip()
    prompt = fields.get("Prompt", "").strip()
    skill = fields.get("Skill", "").strip()
    purpose = fields.get("When is this role useful?", "").strip()
    lang_raw = fields.get("Language of the prompt", "").strip()
    seat_raw = fields.get("Which seat is it for?", "").strip()

    lang = LANG_MAP.get(lang_raw)
    if lang is None:
        comment(
            f"`{lang_raw or '(none)'}` isn't one of the languages this can file "
            "automatically. Please add the role folder by hand, or resubmit with "
            "one of English/Ukrainian/German/Spanish/French."
        )
        return

    if not role_name or not prompt:
        comment("Missing role name or prompt — can't build the role folder from this issue.")
        return

    code = make_code(fields.get("Role code", ""), role_name)
    seat_text = SEAT_MAP.get(seat_raw, seat_raw or "participant")

    roles_dir = f"roles/{lang}"
    slug = code
    if os.path.isdir(f"{roles_dir}/{slug}"):
        slug = f"{code}-{slugify_ascii(username)}"
    if os.path.isdir(f"{roles_dir}/{slug}"):
        slug = f"{code}-{ISSUE_NUMBER}"

    folder = f"{roles_dir}/{slug}"
    os.makedirs(folder, exist_ok=True)

    readme = [
        f"# {role_name}",
        "",
        f"**Seat:** {seat_text}",
        f"**Language:** {lang_raw}",
        "",
        purpose or "_No description provided._",
        "",
        "## Files",
        "",
        f"- [`prompt-{slug}.md`](prompt-{slug}.md)",
    ]
    if skill:
        readme.append(f"- [`skill-{slug}.md`](skill-{slug}.md)")
    readme += [
        "",
        "---",
        f"Submitted by [@{username}](https://github.com/{username}) via "
        f"[issue #{ISSUE_NUMBER}](https://github.com/{REPO}/issues/{ISSUE_NUMBER}).",
        "",
    ]
    with open(f"{folder}/README.md", "w") as f:
        f.write("\n".join(readme))

    with open(f"{folder}/prompt-{slug}.md", "w") as f:
        f.write(
            f"# Prompt — {role_name}\n\n"
            "Copy the block below into the **Prompt** field of a new role.\n\n"
            f"```text\n{prompt}\n```\n"
        )

    if skill:
        with open(f"{folder}/skill-{slug}.md", "w") as f:
            f.write(
                f"# Skill — {role_name}\n\n"
                "Copy the block below into the **Skill** field of the role.\n\n"
                f"```text\n{skill}\n```\n"
            )

    index_path = update_roles_index(lang, slug, role_name, purpose, seat_raw)

    branch = f"role/{slug}"
    run(["git", "checkout", "-b", branch])
    run(["git", "add", folder])
    if index_path:
        run(["git", "add", index_path])
    run(["git", "commit", "-m", f"Add role: {role_name} ({slug})"])
    # Force-push: this branch is exclusively bot-owned and regenerated fresh
    # each run, so a leftover remote branch from a prior (e.g. closed
    # without merge) attempt should just be overwritten, not block on.
    run(["git", "push", "-f", "-u", "origin", branch])

    pr_body = (
        f"Closes #{ISSUE_NUMBER}\n\n"
        "Auto-generated from the *Submit a role* issue, reviewed before the "
        "`approved` label was applied.\n\n"
        f"- Role code: `{slug}`\n"
        f"- Credit: submitted by @{username}\n"
    )
    result = run(
        [
            "gh", "pr", "create", "-R", REPO,
            "--title", f"Add role: {role_name} ({slug})",
            "--body", pr_body,
            "--base", "main",
            "--head", branch,
        ],
        capture_output=True,
    )
    pr_url = result.stdout.strip().splitlines()[-1]
    pr_number = pr_url.rstrip("/").rsplit("/", 1)[-1]

    try:
        run(["gh", "pr", "merge", pr_number, "-R", REPO, "--squash", "--delete-branch"])
        comment(f"Merged {pr_url} — the role is live in `{folder}`.")
        # Don't rely solely on the "Closes #N" auto-link - it can fail to
        # fire when more than one PR has referenced the same issue (e.g.
        # an earlier attempt that was closed without merging).
        try:
            run(["gh", "issue", "close", ISSUE_NUMBER, "-R", REPO, "--reason", "completed"])
        except subprocess.CalledProcessError:
            pass
    except subprocess.CalledProcessError:
        comment(f"Opened {pr_url} but couldn't auto-merge it — needs a manual merge.")


if __name__ == "__main__":
    main()
