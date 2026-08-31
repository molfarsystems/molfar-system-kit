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
import time

import yaml

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


def form_field_labels():
    """The `### <label>` headings GitHub writes for the submit-role form.

    Read from the form itself so the two can't drift apart. Splitting on any
    `### ` instead would eat the role's own content: a skill with `### 1. Step`
    headings gets cut at the first one, silently - the run still succeeds and
    the truncated role still merges.
    """
    form = os.path.join(os.path.dirname(__file__), "..", "ISSUE_TEMPLATE", "submit-role.yml")
    with open(form, encoding="utf-8") as f:
        spec = yaml.safe_load(f)
    labels = []
    for item in spec.get("body", []):
        if item.get("type") == "markdown":
            continue
        label = item.get("attributes", {}).get("label")
        if label:
            labels.append(label)
    if not labels:
        raise RuntimeError(f"no field labels found in {form}")
    return labels


def parse_issue_body(body: str) -> dict:
    pattern = "|".join(re.escape(lbl) for lbl in form_field_labels())
    parts = re.split(rf"^### ({pattern})$", body, flags=re.MULTILINE)
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
    # Kept short on purpose. GitHub gives no control over table column widths,
    # so on a phone a long cell wraps to roughly one word per line. An index
    # entry is a short phrase; the role's own README carries the full text.
    if len(text) > 110:
        text = text[:109].rstrip() + "…"
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


def merge_pr(pr_number: str, rebuild, attempts: int = 3) -> bool:
    """Squash-merge the PR, rebuilding it onto a fresh main between attempts.

    Roles approved together are built in parallel, each from whatever main
    existed when its run started. The first to merge moves main, and every
    other run is then holding a branch built on a base that no longer exists.
    The role files never clash - they are new files in their own folder - but
    the index table does: two runs insert a row at the same line.

    So a failed merge is not a reason to stand down. Rebuild the branch from
    the current main, which re-reads the index with the other role's row
    already in it, and ask again.
    """
    for attempt in range(attempts):
        try:
            run(["gh", "pr", "merge", pr_number, "-R", REPO, "--squash", "--delete-branch"])
            return True
        except subprocess.CalledProcessError:
            if attempt == attempts - 1:
                return False
            print(f"merge attempt {attempt + 1} failed, rebuilding on main", file=sys.stderr)
            time.sleep(5)
            rebuild()
    return False


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
    branch = f"role/{slug}"

    def build_and_push() -> None:
        """Write the role folder and the index row, commit, force-push.

        Called again after a failed merge, on a branch reset to the current
        main, so the index row lands in the index as it stands now. The slug
        is deliberately not re-resolved: the PR is already pointing at this
        branch name.
        """
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
        with open(f"{folder}/README.md", "w", encoding="utf-8") as f:
            f.write("\n".join(readme))

        with open(f"{folder}/prompt-{slug}.md", "w", encoding="utf-8") as f:
            f.write(
                f"# Prompt — {role_name}\n\n"
                "Copy the block below into the **Prompt** field of a new role.\n\n"
                f"```text\n{prompt}\n```\n"
            )

        if skill:
            with open(f"{folder}/skill-{slug}.md", "w", encoding="utf-8") as f:
                f.write(
                    f"# Skill — {role_name}\n\n"
                    "Copy the block below into the **Skill** field of the role.\n\n"
                    f"```text\n{skill}\n```\n"
                )

        index_path = update_roles_index(lang, slug, role_name, purpose, seat_raw)

        run(["git", "add", folder])
        if index_path:
            run(["git", "add", index_path])
        run(["git", "commit", "-m", f"Add role: {role_name} ({slug})"])
        # Force-push: this branch is exclusively bot-owned and regenerated
        # fresh each run and each rebuild, so whatever is on the remote
        # should just be overwritten, not blocked on.
        run(["git", "push", "-f", "-u", "origin", branch])

    def rebuild() -> None:
        run(["git", "fetch", "origin", "main"])
        run(["git", "checkout", "-B", branch, "origin/main"])
        build_and_push()

    # Start from the newest main, not whatever the checkout happened to fetch:
    # a sibling role may have merged while this run was queuing.
    rebuild()

    pr_body = (
        f"Closes #{ISSUE_NUMBER}\n\n"
        "Auto-generated from the *Submit a role* issue, reviewed before the "
        "`approved` label was applied.\n\n"
        f"- Role code: `{slug}`\n"
        f"- Credit: submitted by @{username}\n"
    )
    # A PR for this branch may already be open: the label was removed and
    # re-applied, or an earlier run opened one and failed to merge it. Reuse
    # it - the force-push above already put the current content on its head.
    try:
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
    except subprocess.CalledProcessError:
        result = run(
            ["gh", "pr", "list", "-R", REPO, "--head", branch,
             "--state", "open", "--json", "url", "-q", ".[0].url"],
            capture_output=True,
        )
        pr_url = result.stdout.strip()
        if not pr_url:
            raise
        print(f"reusing existing PR {pr_url}", file=sys.stderr)
    pr_number = pr_url.rstrip("/").rsplit("/", 1)[-1]

    if merge_pr(pr_number, rebuild):
        comment(f"Merged {pr_url} — the role is live in `{folder}`.")
        # Don't rely solely on the "Closes #N" auto-link - it can fail to
        # fire when more than one PR has referenced the same issue (e.g.
        # an earlier attempt that was closed without merging).
        try:
            run(["gh", "issue", "close", ISSUE_NUMBER, "-R", REPO, "--reason", "completed"])
        except subprocess.CalledProcessError:
            pass
    else:
        comment(f"Opened {pr_url} but couldn't auto-merge it — needs a manual merge.")


if __name__ == "__main__":
    main()
