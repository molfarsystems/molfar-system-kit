**English** · [Українська](README.ua.md)

# Built-in roles in Ukrainian

Ukrainian versions of 26 built-in Molfar roles (the app ships them in English). This section is also a sample of how a pack is built from role folders.

**Install them all at once:** [`../packs/molfar-builtin-ua.zip`](../packs/molfar-builtin-ua.zip) → Molfar → **Settings** → **Data archive** → **Restore from archive** → **Add** (Molfar 2.0.4+). The roles appear in both catalogs in the category **Українською** ("In Ukrainian"), next to the English ones, replacing nothing.

Three roles — Role Architect, Interviewer, Technology Journalist — are also in [`molfar-kit-ua.zip`](../packs/molfar-kit-ua.zip) in a different edition; install both and the app asks "Already exists".

The role list with descriptions (in Ukrainian) is in [`README.ua.md`](README.ua.md).

## Role folder layout

```
builtin-ua/<code>/
  README.md        front matter: code, name, description (≤ 128), seat (participant / orchestrator)
  prompt-<code>.md the prompt in a ```text block (≤ 10,000 characters)
  skill-<code>.md  the skill in a ```text block (≤ 10,000 characters)
```

CC0 1.0.
