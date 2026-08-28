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

    branch = f"role/{slug}"
    run(["git", "checkout", "-b", branch])
    run(["git", "add", folder])
    run(["git", "commit", "-m", f"Add role: {role_name} ({slug})"])
    run(["git", "push", "-u", "origin", branch])

    pr_body = (
        f"Closes #{ISSUE_NUMBER}\n\n"
        "Auto-generated from the *Submit a role* issue form. Please review before merging:\n\n"
        "- [ ] Prompt/skill text reads well and doesn't need edits\n"
        f"- [ ] Add a row for this role to `roles/README.md`"
        f"{' and `roles/README.ua.md`' if lang != 'en' else ''}\n"
        f"- [ ] Credit: submitted by @{username}\n"
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
    comment(f"Opened {pr_url} — this issue will close automatically once it's merged.")


if __name__ == "__main__":
    main()
