# Handoff: kit → app update

Written at the end of the session that finished the kit, for the session that
does the app update. Everything below is either not written down anywhere else,
or written down somewhere a fresh session would not think to look.

**Read this first, then the files it points at.** Do not trust it over the
files — if they disagree, the files are right and this note is stale.

- Kit repo: `molfarsystems/molfar-system-kit`, branch `main`
- App repo: `molfarsystems/Molfar-System` — the code currently on Google Play,
  version 1.0.3, `buildozer.spec` line 10

---

## 1. What the app update has to do

Two independent pieces of work. Neither has been started.

### A. Replace `default_models` in `tools/providers_registry.py`

Source of truth: [`models/app-defaults.md`](../models/app-defaults.md) — 20
models, verified by the owner against each provider's own model page.

**Provider order changes.** The file lists OpenRouter first, then Google AI
Studio, then NVIDIA NIM, and that order is deliberate: it is the order the
app's picker shows. Within a provider, the numbering is the picker order too.

The delta, computed against the registry as it stands at `bebfc70`:

| provider | now | after | added | removed |
|---|---:|---:|---:|---:|
| OpenRouter | 10 | 12 | 8 | 6 |
| Google AI Studio | 2 | 1 | 0 | 1 |
| NVIDIA NIM | 4 | 7 | 7 | 4 |

NVIDIA is a **complete replacement** — not one of the four models currently
there survives. Google keeps only `gemini-2.5-flash`; `gemini-2.0-flash` goes.

**Paid models.** Four of the twenty are paid, all on OpenRouter, and each
carries a literal `$ ` prefix in its display name (`$ GLM 5.3 Flash`). This is
not something invented for this update — `providers_registry.py` already
documents the convention in a comment. Keep it.

**Display names** in `app-defaults.md` are already final. They were derived
from the model IDs by dropping the vendor prefix, the active-parameter suffix
(`a55b`, `a12b`, `a4b`) and the `-it` marker. Do not re-derive them; copy them.

`context` and `price` in that file are for the human reader. The registry
takes only the ID and the name.

### B. Add three roles to `modules/roles_seed.py`

They came in through the kit's issue pipeline and are already mirrored in
`roles/default-roles/participants/{ua,en}/`:

| code | ua name | en name |
|---|---|---|
| `interviewer` | Інтерв'юер | Interviewer |
| `tech_journalist` | Технічний журналіст | Technology Journalist |
| `architect_roles` | Архітектор ролей | Role Architect |

All three are participants (seats 1–4). Each folder's `README.md` carries
`code` / `name` / `description` / `seat` as YAML front matter, matching the
field names `roles_seed.py` needs — that is what makes the folder machine-
readable back into the seed.

The seed takes the **Ukrainian** text. `roles_seed.py` says so explicitly near
the top: name, description and prompt are Ukrainian and are not localised. The
English folders are documentation for the kit, not app data.

Seed count goes 23 → 26 (20 participants + 6 orchestrators).

---

## 2. Traps that will cost you if you do not know them

### Codes use underscores in the app, hyphens in the kit

This is deliberate, not a mistake to "fix".

- `roles_seed.py` and `roles/default-roles/` use `tech_journalist`,
  `architect_roles` — English words, snake_case, like every existing seed code.
- `roles/<lang>/` uses `tech-journalist`, `architect-roles`, because the build
  script slugifies the code for a folder name and turns `_` into `-`.

The seed's `code` is a **stable key that must never change** — the comment at
the top of `roles_seed.py` says so, and the folder slug on device is derived
from it (`{code}_{id}_{hash6}`). Renaming a code orphans a user's role folder.

### Three defects live in `roles_seed.py` right now

Found while validating the kit; the kit copies are already fixed, the app is
not. Fix them in the same pass or the kit and app diverge again.

1. **`criminal_judge` declares `name: criminal-judge`** in its skill front
   matter — hyphen where the code has an underscore.
2. **Four football roles have an unquoted `description` containing `": "`**
   in their skill front matter (`football_coach`, `football_journalist`,
   `football_tactician`, `football_psychologist`). A colon followed by a space
   ends a key in YAML, so the block does not parse. Quote the value.
3. Nothing else — the four orchestrators without front matter
   (`moderator`, `referee`, `analyst`, `project_manager`) are **correct**.
   Their skills stack on top of the orchestrator seat's own system skill and
   are kept as short additions on purpose; the seed comment explains it.

### Character limits are counted in code points, not bytes

`MAX_ROLE_PROMPT` and `MAX_ROLE_SKILL` are both 5000, `MAX_ROLE_DESC` is 128,
all in `modules/schemas.py`. Cyrillic is two bytes per letter, so `wc -c` and
`wc -m` in the C locale both mislead. Count with Python `len()` on a decoded
string.

Every prompt and skill in the kit is currently under 5000 and every
default-role description under 128 — verified, not assumed. Keep it that way:
adding a role to the seed with an oversized field is the kind of thing that
only shows up on device.

### Do not stage with `git add .github` after running anything

A `.pyc` reached `main` that way once already (commit `c874ee2`, removed in
`#34`). There is a `.gitignore` now, but the habit is the real fix.

---

## 3. The state of the kit, for reference

`main` at the time of writing carries everything below. Nothing is in flight.

- `models/app-defaults.md` — the 20 models. **The working file**; the owner
  edits it by hand and the app update reads from it.
- `models/catalogue.md` — the same 20 for users, with per-model notes,
  generated from `app-defaults.md`. Deliberately carries **no** speed or
  language-quality ratings: those were never measured and an invented number
  is worse than an admitted gap.
- `models/providers.md` — the three providers, and the OpenRouter privacy trap
  (see below).
- `models/recommended.md`, `models/README.md` — seat advice, kept in step.
- `roles/default-roles/` — 26 roles × 2 languages, front matter on every
  README, the machine-readable source for regenerating the seed.
- `roles/<lang>/` — community roles, submitted through the issue pipeline.
- `.github/` — the pipeline: issue form → `approved` label → role folder → PR
  → merge → close issue. Working; do not touch it for the app update.
- `TMP/Pravyla_Roli.md` on branch `tmp/issues-skill` — the three-layer role
  design (Base / prompt = persona / skill = method). **Not implemented in the
  app.** If the update touches how roles are assembled, read it first.

### The OpenRouter privacy trap

A fresh OpenRouter key fails on every `:free` model with a 404 mentioning
*"Free model training violation (account settings)"*. Nothing is broken:
OpenRouter drops endpoints that do not match the account's data policy, and
most free endpoints train on or publish prompts, so with those permissions off
there is nothing left to route to. Fix is both toggles at
`openrouter.ai/settings/privacy`. Confirmed working by the owner.

Documented in `models/providers.md`, `help/{en,ua}/api-keys.md` (as step 5 of
creating the key) and `help/{en,ua}/troubleshooting.md`.

**Open offer, not done:** `tools/ai_adapters/openai_compat.py` surfaces this
correctly but as raw English provider text inside a Ukrainian app. It maps to
`code="http"` like any other non-200. Recognising this specific 404 and
showing a Ukrainian message with the settings link was offered and not yet
approved.

---

## 4. Branches in `Molfar-System`

Checked at `bebfc70`. Four of the six carry **zero** commits that are not
already in `main`:

| branch | unique commits | note |
|---|---:|---|
| `main` | — | at `bebfc70` |
| `update/complete-overhaul` | 0 | same SHA as `main`; CI builds on push here |
| `claude/review-prompt-cosmetics` | 0 | same SHA as `main` |
| `claude/claude-code-mobile-asic2n` | 0 | 35 behind, fully merged |
| `claude/roles-editor-cosmetics` | 0 | 10 behind, fully merged |
| `claude/16kb-page-size` | 0 | 19 behind, fully merged |

Nothing would be lost by deleting the three `claude/*` branches that are
behind, plus `claude/review-prompt-cosmetics`. **`update/complete-overhaul`
must stay** — `.github/workflows/main.yml` builds the APK on every push to it.
The owner has not decided; do not delete anything without asking.

---

## 5. Suggested order for the update

1. Read `models/app-defaults.md` and `roles/default-roles/README.md` in full.
2. Do the registry swap (A) — small, self-contained, easy to verify.
3. Do the seed addition (B) plus the three `roles_seed.py` defects.
4. Bump `version` in `buildozer.spec`.
5. Let CI build the APK. Do not try to build locally unless the packaging
   itself is what is being tested — `CLAUDE.md` explains why the pinned
   toolchain versions matter.

### The part that is easy to get wrong

**Adding roles to the seed does not add them to an existing install.**
`_seed_roles` in `modules/creator.py` counts the rows in each role table and
skips seeding entirely if the table is not empty — checked per table, so
`roles_participant` and `roles_orchestrator` are decided independently. Any
phone that has already launched the app once keeps exactly the 23 roles it
seeded on first run.

So a fresh install gets 26 roles and an upgrade gets 23, silently, unless a
numbered branch is added to `_migrate()` in `creator.py` to insert the three
new ones. Whether existing users should get them is **not decided** — ask
before writing that migration. If it is written: migrations there are additive
and numbered (`if from_version < N <= to_version:`), a new one goes on the end
without touching the existing branches, and `ROLES_DB_VERSION` in
`modules/schemas.py` has to go up with it.

Test on a device either way. This is the class of bug that looks fine in CI
and only appears on an upgrade.
