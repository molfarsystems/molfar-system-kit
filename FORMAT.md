# Molfar role pack format

A role pack is a `.zip` file that [Molfar System](https://play.google.com/store/apps/details?id=com.nova_hata.molfar) (Android) adds to the user's role catalog: **Settings → Data archive → Install roles → Add**. This page describes the format so that anyone can build packs. The tools in [`tools/`](tools/) build and check them.

## Files

```
pack.zip
├── manifest.json
└── data/roles.json
```

Nothing else. The app ignores other entries, and the checker reports them.

### manifest.json

```json
{"app": "molfar", "format": 2, "versionCode": 12, "versionName": "2.0.4", "created": 1762041600000, "parts": ["roles"]}
```

| Field | Meaning |
|---|---|
| `app` | Always `"molfar"`. |
| `format` | `2` — the partial-archive format: its contents are **added** to the user's data without a restart. (`1` is the full backup, which replaces everything; packs never use it.) |
| `versionCode` | The oldest app version code that can install the pack. The app refuses a pack from a newer version. `12` = Molfar 2.0.4, the first with packs and 25,000-character roles. |
| `versionName` | For people only. |
| `created` | Unix time in milliseconds. |
| `parts` | `["roles"]` for a role pack. (The app also knows `"models"` and `"files"` in its own archives.) |
| `license` | Optional. The full license text of the roles' source, when it requires that the notice travels with every copy (e.g. MIT). The app ignores it; it is there for people who unpack the file. |

### data/roles.json

An array of roles:

```json
[{
  "kind": "participant",
  "code": "agency-sales-discovery-coach",
  "builtin": false,
  "name": "Discovery Coach",
  "description": "Coaches sales teams on elite discovery methodology…",
  "prompt": "You are Discovery Coach…",
  "skill": "## The Three Discovery Frameworks…",
  "category": "",
  "categoryName": "Agency — Sales",
  "categoryDescription": ""
}]
```

| Field | Limit | Meaning |
|---|---|---|
| `kind` | — | `participant` (the **Experts** catalog: meeting seats 1–4 and the expert chat) or `orchestrator` (runs a meeting, seat 5). The catalogs never mix. |
| `code` | — | A stable id of the role in its source, e.g. `agency-<file>`. Used to recognise the same role on a second install. |
| `builtin` | — | Always `false` in a pack. |
| `name` | 64 | Shown in the catalog. Required. |
| `description` | 128 | One line under the name. |
| `prompt` | 25,000 | Who the role is and how it talks. |
| `skill` | 25,000 | What it does and in what order: procedures, checklists, output formats. |
| `category` | — | Code of a built-in category (`business`, `court`, `analytics`, `it`, `sport`, `other`) or empty. |
| `categoryName` | 32 | Name of a custom category, created if missing (matched by name, case-insensitive). |
| `categoryDescription` | 128 | Description of a new custom category. |

Texts are plain Markdown. A role goes into every request to the model, so a long role costs tokens.

## What the app does on install

1. Checks the manifest: `app`, `format`, `versionCode` not newer than the app.
2. Compares each role with the catalog — by `code`, otherwise by `name` within the same catalog:
   - not there → **added**;
   - there with the same texts → **skipped**;
   - there with different texts → the user chooses **Replace**, **Keep both** ("Name (2)") or **Skip**.
3. Writes through the same path as the app's own Save button (same limits). A role over a limit is skipped, never cut.

Nothing is deleted, nothing else is touched (keys, chats, meetings), no restart.

## Compatibility promise

- **Format 2 stays readable.** Changes to it only **add** optional fields; the app ignores fields it doesn't know, so an older app reads a newer pack's roles as long as `versionCode` allows it.
- A change that an older app could misread gets a **new `format` number**, which older apps refuse with a clear message instead of guessing.
- Limits only go **up**. If a pack needs a newer limit, it raises `versionCode` to the first app version that has it.

## Tools

- [`tools/build_pack.py`](tools/build_pack.py) — role folders → pack.
- [`tools/check_pack.py`](tools/check_pack.py) — checks packs the way the app reads them.
- [`tools/agency_convert.py`](tools/agency_convert.py), [`tools/agency_packs.py`](tools/agency_packs.py) — [agency-agents](https://github.com/msitarzewski/agency-agents) → packs.

Python 3, standard library only. CC0 1.0, like the rest of this repository outside `external/`.
