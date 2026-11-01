#!/usr/bin/env python3
"""Build a Molfar role pack (.zip) from role folders.

    build_pack.py <out.zip> <category name> <role folder>...

A role folder holds README.md, prompt-*.md and skill-*.md. The prompt and the skill are the contents of the
first fenced block (```text ... ```) in their files. README.md is either:
  * YAML front matter: code, name, description, seat (participant | orchestrator), optional category; or
  * "# Name", a "**Seat:**" line and a first paragraph used as the description.

Limits follow the app (name 64, description 128, prompt and skill 25,000 characters, category name 32).
A text over the limit is an error, never cut silently. The pack format is described in ../FORMAT.md.
Standard library only.
"""
import json, os, re, sys, time, zipfile

NAME, DESCRIPTION, TEXT, CATEGORY = 64, 128, 25_000, 32
# The oldest Molfar that installs packs with 25,000-character roles.
VERSION_CODE, VERSION_NAME = 12, "2.0.4"


def block(path):
    lines = open(path, encoding="utf-8").read().replace("\r\n", "\n").split("\n")
    start = next(i for i, l in enumerate(lines) if l.strip().startswith("```"))
    end = max(i for i, l in enumerate(lines) if l.strip().startswith("```") and i > start)
    return "\n".join(lines[start + 1:end]).strip()


def short(text, limit):
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[:limit - 1].rsplit(" ", 1)[0].rstrip(",;:—- ") + "…"


def front_matter(readme):
    if not readme.startswith("---\n"):
        return {}
    out = {}
    for line in readme[4:readme.index("\n---", 4)].split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip().strip('"')
    return out


def role(folder):
    readme = open(os.path.join(folder, "README.md"), encoding="utf-8").read().replace("\r\n", "\n")
    meta = front_matter(readme)
    if meta:
        name, seat, description, code = meta["name"], meta.get("seat", "participant"), meta.get("description", meta["name"]), meta.get("code")
    else:
        name = re.search(r"^# (.+)$", readme, re.M).group(1).strip()
        seat = re.search(r"^\*\*(?:Seat|Місце):\*\*\s*(.+)$", readme, re.M).group(1)
        body = re.split(r"^## ", readme, maxsplit=1, flags=re.M)[0]
        paras = [p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith(("#", "**"))]
        description, code = (paras[0] if paras else name), None
    seat = seat.lower()
    kind = "orchestrator" if ("orchestrator" in seat or "оркестратор" in seat) else "participant"
    slug = os.path.basename(os.path.normpath(folder))
    lang = os.path.basename(os.path.dirname(os.path.normpath(folder)))
    prompt = block(next(os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.startswith("prompt-")))
    skill = block(next(os.path.join(folder, f) for f in sorted(os.listdir(folder)) if f.startswith("skill-")))
    for label, value, limit in (("name", name, NAME), ("prompt", prompt, TEXT), ("skill", skill, TEXT)):
        if len(value) > limit:
            sys.exit(f"{folder}: {label} has {len(value)} characters, the limit is {limit}")
    return {"kind": kind, "code": code if (code or "").startswith("agency-") else f"kit-{lang}-{code or slug}",
            "builtin": False, "name": name, "description": short(description, DESCRIPTION),
            "prompt": prompt, "skill": skill, "_category": meta.get("category", "")}


def write_pack(out, roles):
    manifest = {"app": "molfar", "format": 2, "versionCode": VERSION_CODE, "versionName": VERSION_NAME,
                "created": int(time.time() * 1000), "parts": ["roles"]}
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False))
        z.writestr("data/roles.json", json.dumps(roles, ensure_ascii=False, indent=1))


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    out, category, folders = sys.argv[1], sys.argv[2], sys.argv[3:]
    if len(category) > CATEGORY:
        sys.exit(f"category name has {len(category)} characters, the limit is {CATEGORY}")
    roles = [role(f) for f in folders]
    for r in roles:
        r.update({"category": "", "categoryName": r.pop("_category") or category, "categoryDescription": ""})
    write_pack(out, roles)
    for r in roles:
        print(f"  {r['kind'][:5]}  {r['name']}  ·  {len(r['description'])}/{len(r['prompt'])}/{len(r['skill'])}")
    print(f"{out}: {len(roles)} roles")


if __name__ == "__main__":
    main()
