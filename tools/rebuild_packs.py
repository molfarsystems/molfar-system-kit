#!/usr/bin/env python3
"""Rebuild the Molfar role packs in roles/packs/ from the role folders, and the pack tables in its READMEs.

    rebuild_packs.py [repo root]

  roles/<lang>/*       -> roles/packs/molfar-kit-<lang>.zip   (every language folder: en, ua, de, ...)
  roles/builtin-ua/*/  -> roles/packs/molfar-builtin-ua.zip

A pack is rewritten only when its roles changed (manifest dates alone don't count), so a run with nothing new
leaves the repository untouched. Used by .github/workflows/rebuild-packs.yml after a role is merged.
Standard library only.
"""
import json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pack  # noqa: E402

LANG_NAMES = {"en": "English", "ua": "Українська", "de": "Deutsch", "fr": "Français", "es": "Español", "pl": "Polski", "it": "Italiano"}
SPECIAL = {"packs", "builtin-ua"}


def roles_of(folders, category):
    roles = []
    for folder in folders:
        r = build_pack.role(folder)
        r.update({"category": "", "categoryName": r.pop("_category") or category, "categoryDescription": ""})
        roles.append(r)
    return roles


def current(path):
    try:
        with zipfile.ZipFile(path) as z:
            return json.loads(z.read("data/roles.json"))
    except (OSError, KeyError, zipfile.BadZipFile, ValueError):
        return None


def table(packs, lang):
    head = "| Pack | Roles | Language |\n|---|---|---|\n" if lang == "en" else "| Набір | Ролі | Мова |\n|---|---|---|\n"
    rows = []
    for name, label, roles in packs:
        names = ", ".join(r["name"] for r in roles)
        if name == "molfar-builtin-ua.zip":
            names = (f"The {len(roles)} built-in roles in Ukrainian — see [`../builtin-ua/`](../builtin-ua/)" if lang == "en"
                     else f"{len(roles)} вбудованих ролей українською — див. [`../builtin-ua/`](../builtin-ua/README.ua.md)")
        rows.append(f"| [`{name}`]({name}) | {names} | {label} |")
    return head + "\n".join(rows)


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)
    roles_dir, packs_dir = os.path.join(root, "roles"), os.path.join(root, "roles", "packs")
    plan = []
    for lang in sorted(d for d in os.listdir(roles_dir) if os.path.isdir(os.path.join(roles_dir, d)) and d not in SPECIAL):
        folders = sorted(os.path.join(roles_dir, lang, f) for f in os.listdir(os.path.join(roles_dir, lang))
                         if os.path.isfile(os.path.join(roles_dir, lang, f, "README.md")))
        if folders:
            plan.append((f"molfar-kit-{lang}.zip", LANG_NAMES.get(lang, lang), roles_of(folders, "Molfar Kit")))
    builtin = os.path.join(roles_dir, "builtin-ua")
    if os.path.isdir(builtin):
        folders = sorted(os.path.join(builtin, f) for f in os.listdir(builtin) if os.path.isfile(os.path.join(builtin, f, "README.md")))
        plan.append(("molfar-builtin-ua.zip", "Українська", roles_of(folders, "Українською")))
    changed = []
    for name, _, roles in plan:
        path = os.path.join(packs_dir, name)
        if current(path) != roles:
            build_pack.write_pack(path, roles)
            changed.append(name)
    # Packs whose folder is gone (e.g. a language with no roles left) are removed.
    wanted = {name for name, _, _ in plan}
    for f in os.listdir(packs_dir):
        if f.startswith("molfar-") and f.endswith(".zip") and f not in wanted:
            os.remove(os.path.join(packs_dir, f))
            changed.append(f"-{f}")
    for readme, lang in (("README.md", "en"), ("README.ua.md", "ua")):
        path = os.path.join(packs_dir, readme)
        text = open(path, encoding="utf-8").read()
        new = re.sub(r"(<!-- packs:start -->\n).*?(\n<!-- packs:end -->)", lambda m: m.group(1) + table(plan, lang) + m.group(2), text, flags=re.S)
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            changed.append(readme)
    print("changed: " + (", ".join(changed) if changed else "nothing"))


if __name__ == "__main__":
    main()
