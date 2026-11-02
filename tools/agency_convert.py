#!/usr/bin/env python3
"""Convert one agency-agents agent (MIT) into a Molfar role folder.

    agency_convert.py <agent.md> <out dir> <category> [<source commit>]

An agent is YAML front matter (name, description, ...) plus "## " sections. Sections are sorted by their heading:
  prompt  - identity, mission, rules, communication style, principles (and the text before the first section);
  skill   - everything else (templates, workflow, frameworks, metrics);
  dropped - "Learning & Memory" (memory between chats, which Molfar does not have).
Emoji are removed from headings. Over 25,000 characters, whole sections / "###" subsections are dropped from the
end (low-priority sections first, then the last subsection of the largest section); text is never cut mid-way.
What was dropped is listed in the folder's README. The skill ends with an attribution line (MIT).
Standard library only.
"""
import os, re, sys

LIMIT = 25_000
PROMPT_KEYS = ("identity", "role definition", "who you are", "mission", "critical rules", "rules you must",
               "communication style", "coaching principles", "principles", "personality", "your role")
DROP_KEYS = ("learning & memory", "learning and memory")
# Dropped first when a text is too long.
LOW_PRIORITY = ("advanced capabilities", "success metrics", "continuous improvement", "what great", "domain expertise")
SOURCE = "https://github.com/msitarzewski/agency-agents"


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.index("\n---", 3)
    meta = {}
    for line in text[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[end + 4:].lstrip("\n")


def clean_heading(line):
    # Emoji and pictograms at the start of a heading go.
    m = re.match(r"^(#+)\s*(.*)$", line)
    title = re.sub(r"^[^\w(«\"'“]+", "", m.group(2), flags=re.U).strip()
    return f"{m.group(1)} {title}"


def sections(body):
    """[(heading or '', text)] split on "## "; headings (and "###" inside) are cleaned of emoji."""
    lines = [clean_heading(l) if re.match(r"^#{2,4}\s", l) else l for l in body.split("\n")]
    out, title, buf = [], "", []
    for line in lines:
        if line.startswith("## "):
            out.append((title, "\n".join(buf).strip()))
            title, buf = line, []
        else:
            buf.append(line)
    out.append((title, "\n".join(buf).strip()))
    return [(t, x) for t, x in out if t or x]


def kind_of(title):
    low = title.lower()
    if any(k in low for k in DROP_KEYS):
        return "drop"
    if not title or any(k in low for k in PROMPT_KEYS):
        return "prompt"
    return "skill"


def join(parts):
    return "\n\n".join((t + "\n\n" + x if t else x).strip() for t, x in parts if (t or x)).strip()


def fit(parts, limit, dropped):
    """Fit sections into the limit: low-priority sections go first (from the end), then the last "###"
    subsection of the LARGEST section, until it fits; sections without subsections go from the end."""
    parts = list(parts)
    def size():
        return len(join(parts))
    for i in reversed(range(len(parts))):
        if size() <= limit:
            return parts
        if any(k in parts[i][0].lower() for k in LOW_PRIORITY):
            dropped.append(parts[i][0].lstrip("# "))
            parts[i] = ("", "")
    while size() > limit:
        splittable = [i for i, (t, x) in enumerate(parts) if len(re.split(r"(?m)^(?=### )", x)) > 1]
        if splittable:
            i = max(splittable, key=lambda j: len(parts[j][1]))
            title, text = parts[i]
            subs = re.split(r"(?m)^(?=### )", text)
            gone = subs.pop()
            dropped.append(f"{title.lstrip('# ')} → {gone.split(chr(10), 1)[0].lstrip('# ').strip()}")
            parts[i] = (title, "".join(subs).strip())
        else:
            i = max(j for j, p in enumerate(parts) if p[0] or p[1])
            dropped.append(parts[i][0].lstrip("# ") or "(intro)")
            parts[i] = ("", "")
    return [p for p in parts if p[0] or p[1]]


def fence(text):
    ticks = "````" if "```" in text else "```"
    return f"{ticks}text\n{text}\n{ticks}"


def main():
    src, out, category = sys.argv[1], sys.argv[2], sys.argv[3]
    commit = sys.argv[4] if len(sys.argv) > 4 else ""
    meta, body = front_matter(open(src, encoding="utf-8").read().replace("\r\n", "\n"))
    name = meta.get("name", os.path.basename(src)[:-3]).strip()
    body = re.sub(r"^# .*\n", "", body, count=1)  # the top heading is the name
    parts = sections(body)
    prompt_parts = [p for p in parts if kind_of(p[0]) == "prompt"]
    skill_parts = [p for p in parts if kind_of(p[0]) == "skill"]
    dropped = [p[0].lstrip("# ") + " (memory between chats — Molfar has none)" for p in parts if kind_of(p[0]) == "drop"]
    rel = os.path.relpath(src, os.path.dirname(os.path.dirname(os.path.abspath(src)))) if "/" in src else src
    credit = (f"Adapted from “{name}” in The Agency ({SOURCE}, {rel}{', ' + commit if commit else ''}). "
              "MIT License, © AgentLand Contributors.")
    prompt = join(fit(prompt_parts, LIMIT, dropped))
    skill_body = join(fit(skill_parts, LIMIT - len(credit) - 4, dropped))
    skill = (skill_body + "\n\n---\n" + credit).strip()
    slug = re.sub(r"[^a-z0-9]+", "-", os.path.basename(src)[:-3].lower()).strip("-")
    folder = os.path.join(out, slug)
    os.makedirs(folder, exist_ok=True)
    description = " ".join(meta.get("description", name).split())
    with open(os.path.join(folder, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"---\ncode: agency-{slug}\nname: \"{name}\"\ndescription: \"{description.replace(chr(34), chr(39))}\"\n"
                f"seat: participant\ncategory: \"{category}\"\n---\n\n# {name}\n\n{description}\n\n"
                f"Source: [{rel}]({SOURCE}/blob/{commit or 'main'}/{rel}) · MIT License, © AgentLand Contributors\n\n"
                f"Prompt: {len(prompt)} · Skill: {len(skill)} characters\n")
        if dropped:
            f.write("\nLeft out to fit Molfar (25,000 characters each, no memory between chats):\n\n" + "\n".join(f"- {d}" for d in dropped) + "\n")
    for kind, text in (("prompt", prompt), ("skill", skill)):
        with open(os.path.join(folder, f"{kind}-{slug}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {kind.capitalize()} — {name}\n\n{fence(text)}\n")
    print(f"{slug}: prompt {len(prompt)} · skill {len(skill)} · dropped {len(dropped)}")
    for d in dropped:
        print("   -", d)


if __name__ == "__main__":
    main()
