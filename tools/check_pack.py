#!/usr/bin/env python3
"""Check Molfar role packs the way the app reads them (see ../FORMAT.md).

    check_pack.py <pack.zip>...

Exit code 0 when every pack is valid. Standard library only.
"""
import json, sys, zipfile

KINDS = {"participant", "orchestrator"}
LIMITS = {"name": 64, "description": 128, "prompt": 25_000, "skill": 25_000, "categoryName": 32}
ALLOWED = {"manifest.json", "data/roles.json"}


def check(path):
    problems = []
    with zipfile.ZipFile(path) as z:
        names = set(z.namelist())
        extra = names - ALLOWED
        if extra:
            problems.append(f"unexpected entries: {sorted(extra)}")
        if not ALLOWED <= names:
            return [f"missing {sorted(ALLOWED - names)}"]
        m = json.loads(z.read("manifest.json"))
        if m.get("app") != "molfar":
            problems.append("manifest.app must be \"molfar\"")
        if m.get("format") != 2:
            problems.append("manifest.format must be 2")
        if m.get("parts") != ["roles"]:
            problems.append("manifest.parts must be [\"roles\"]")
        if not isinstance(m.get("versionCode"), int):
            problems.append("manifest.versionCode must be an integer")
        roles = json.loads(z.read("data/roles.json"))
        if not isinstance(roles, list) or not roles:
            return problems + ["data/roles.json must be a non-empty array"]
        for i, r in enumerate(roles):
            label = f"role {i} ({r.get('name', '?')})"
            if r.get("kind") not in KINDS:
                problems.append(f"{label}: kind must be participant or orchestrator")
            if not str(r.get("name", "")).strip():
                problems.append(f"{label}: empty name")
            for key, limit in LIMITS.items():
                value = str(r.get(key, ""))
                if len(value) > limit:
                    problems.append(f"{label}: {key} has {len(value)} characters, the limit is {limit}")
    return problems


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    bad = 0
    for path in sys.argv[1:]:
        problems = check(path)
        print(("OK   " if not problems else "FAIL ") + path)
        for p in problems:
            print("     - " + p)
        bad += bool(problems)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
