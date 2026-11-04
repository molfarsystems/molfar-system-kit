#!/usr/bin/env python3
"""Build Molfar role packs from an agency-agents checkout, one pack per division.

    agency_packs.py <agency-agents checkout> <out dir>

Writes <out dir>/packs/agency-<division>.zip, <out dir>/LICENSE (the source's MIT license) and
<out dir>/ROLES.md (the role list per pack). Divisions about writing code, games, security tooling, spatial
computing and testing are left out, as are agents that drive tools (code bases, package managers, files,
webhooks, several shell commands): Molfar models talk, they don't run tools. Standard library only.
"""
import json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pack  # noqa: E402

DIVISIONS = ["academic", "design", "finance", "gis", "marketing", "paid-media", "product", "project-management",
             "research", "sales", "specialized", "support"]
# Tool-driving agents: any of these, or more than one bash block.
STRONG = re.compile(r"\b(npm |pip install|\.py\b|run `|codebase|pull request|file system|filesystem|webhook|CLI\b)", re.I)
BASH = re.compile(r"\bbash\b", re.I)


def tool_driven(text):
    return bool(STRONG.search(text)) or len(BASH.findall(text)) > 1


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    repo, out = sys.argv[1], sys.argv[2]
    commit = subprocess.run(["git", "-C", repo, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    labels = json.load(open(os.path.join(repo, "divisions.json"), encoding="utf-8"))
    labels = labels.get("divisions", labels)
    os.makedirs(os.path.join(out, "packs"), exist_ok=True)
    shutil.copy(os.path.join(repo, "LICENSE"), os.path.join(out, "LICENSE"))
    license_text = open(os.path.join(repo, "LICENSE"), encoding="utf-8").read()
    listing, skipped, total = [], [], 0
    for div in DIVISIONS:
        label = labels.get(div, {}).get("label", div.title()) if isinstance(labels.get(div), dict) else div.title()
        category = f"Agency — {label}"[:build_pack.CATEGORY]
        files = sorted(os.path.join(r, f) for r, _, fs in os.walk(os.path.join(repo, div)) for f in fs if f.endswith(".md"))
        files = [f for f in files if open(f, encoding="utf-8").read().startswith("---")]
        work = tempfile.mkdtemp()
        roles = []
        for f in files:
            rel = os.path.relpath(f, repo)
            if tool_driven(open(f, encoding="utf-8").read()):
                skipped.append(rel)
                continue
            subprocess.run([sys.executable, os.path.join(HERE, "agency_convert.py"), rel, work, category, commit],
                           cwd=repo, check=True, capture_output=True)
            folder = os.path.join(work, re.sub(r"[^a-z0-9]+", "-", os.path.basename(f)[:-3].lower()).strip("-"))
            r = build_pack.role(folder)
            r.update({"category": "", "categoryName": r.pop("_category") or category, "categoryDescription": ""})
            roles.append(r)
        shutil.rmtree(work)
        if not roles:
            continue
        name = f"agency-{div}.zip"
        build_pack.write_pack(os.path.join(out, "packs", name), roles, license_text)
        total += len(roles)
        listing.append((name, label, roles))
        print(f"{name}: {len(roles)} roles")
    with open(os.path.join(out, "ROLES.md"), "w", encoding="utf-8") as f:
        f.write(f"# Roles in the agency-agents packs\n\nSource: https://github.com/msitarzewski/agency-agents at `{commit}` · "
                f"MIT License, © AgentLand Contributors · {total} roles in {len(listing)} packs.\n")
        for name, label, roles in listing:
            f.write(f"\n## {label} — [`packs/{name}`](packs/{name})\n\n| Role | What it does |\n|---|---|\n")
            for r in sorted(roles, key=lambda x: x["name"].lower()):
                f.write(f"| {r['name']} | {r['description'].replace('|', '/')} |\n")
        f.write("\n## Left out\n\nAgents that drive tools (code bases, package managers, files, webhooks), "
                "and the divisions engineering, game development, healthcare, security, spatial computing and testing.\n\n")
        f.write("\n".join(f"- `{s}`" for s in skipped) + "\n")
    print(f"total {total} roles, skipped {len(skipped)} tool-driven agents")


if __name__ == "__main__":
    main()
