# Roles

Ready-made roles for Molfar System. Each one is a **prompt** (who the role is) and a **skill** (how it works).

The app already comes with 29 built-in roles. This folder holds only roles that are **not** in the app. Ready-made `.zip` packs of these roles are in [`packs/`](packs/) — the quickest way to install them (see the [main README](../README.md)).

---

## All roles

Roles are not mirrored across languages. A role written in Ukrainian and one written in English are separate roles: different people wrote them, they can be improved independently, and one may end up better than the other. Each is listed once, on the page for its own language.

**English roles are below.** Ukrainian ones are in [`README.ua.md`](README.ua.md), everything else in [`OTHER-LANGUAGES.md`](OTHER-LANGUAGES.md).

| Role | What it does | Seat | Language |
|---|---|---|---|
| Technology journalist | Technical articles built from supplied material. Fact kept apart from interpretation, sources checked. | Participant | [en](en/tech-journalist/) |
| Interviewer | Draws out the details of an idea through questions and returns a structured summary. Does not advise. | Participant | [en](en/interviewer/) |
| Devil's Advocate | Attacks a plan to find where it breaks | Participant | [en](en/devils-advocate/) |

---

## How to use a role

The quickest way is a pack from [`packs/`](packs/): **Settings** → **Data archive** → **Install roles** → **Add** (Molfar 2.0.5+).

One role by hand:

1. Open the role folder, then `prompt-*.md`, and tap the copy button on the code block
2. In the app: the **Roles** block on the home screen → **Experts** (or **Orchestrators**) → **+** → category, name, description → **Save**
3. Tap the **Prompt** block → paste → save. The same with `skill-*.md` in the **Skill** block

Or save the `.md` file to your phone and open it in the prompt / skill editor: **⋮** → **Open** → **Storage** or **From device**.

---

## Folder rules

```
roles/<language>/<role-name>/
  README.md
  prompt-<role-name>.md
  skill-<role-name>.md
```

- Folders and files: lowercase Latin, words separated by hyphens
- The suffix in `prompt-*.md` matches the folder name exactly
- No language code in the filename — the language is already in the path
- The folder name is in the role's own language: `ua/advokat-dyiavola/`, `de/anwalt/`

---

## Expert roles vs Orchestrator roles

**Expert roles** (the **Experts** catalog; "Participant" in the tables above — seats 1-4 of a meeting and the expert chat) answer the question. Write them as a specialist with a point of view.

**Orchestrator roles** (seat 5) run the round. The round mechanics are built into the app, and an Orchestrator's skill stacks on top of the fixed rules of that seat. So an Orchestrator skill should describe only the **leading style and evaluation criteria** — not how rounds work. Repeating the mechanics wastes context and can conflict with the built-in rules.

---

## Writing a good role

**Give it a real opinion.** A role that agrees with everything adds nothing to a meeting. The useful roles are the ones that push back.

**Say what it should refuse to do.** "Do not soften the assessment to be polite" does more work than three sentences describing expertise.

**Up to 25,000 characters each — prompt and skill.** The prompt is who the role is and how it talks; the procedure, checklists and output formats belong in the skill. A role goes into every request, so a long one costs tokens — keep it as long as it needs to be, not longer.

**Test it in the expert chat first.** One model, instant feedback, no meeting to set up: Projects → **+** → Expert → pick the role.

**Any language works.** The language of a role doesn't set the language of the answer — the model answers in the language of the question. Write in the language you think in best.

---

## Contributing

Open a **New issue** → *Submit a role*. Fill in the form, send it. No git knowledge needed.

Everything here is CC0 — public domain. By submitting, you agree to release your text the same way.
