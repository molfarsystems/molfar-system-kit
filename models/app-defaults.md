# App default models

Working file, not user documentation. This is the list that goes into the app
as `default_models` in `tools/providers_registry.py` — the models a person sees
in the picker before they add anything of their own.

**Who edits what.** You fill this in by hand. When an update is being prepared,
the list is read from here and written into the registry, so the two never
drift apart.

**Order matters.** The order within a provider is the order shown in the app's
picker. Put the model you want people to reach for first at number 1.

**Format is strict** — three fields per model, each on its own line, blank
line between them:

```
N. model: `model-id`

   name: `Display name`

   Context: 1M
```

Values go in backticks so the boundaries are unambiguous. Keep display names
short — they appear on a phone as `G · Gemini 2.5 Flash`, and the provider
prefix is already eating space.

Context is the input window, written the short way: `1M`, `262K`, `128K`. It is
there for the user, not for the app — the registry only takes the ID and the
name.

Only models that work on a free tier belong here. Anything paid is a choice the
user makes deliberately, not a default.

---

## Google AI Studio

Model list: https://ai.google.dev/gemini-api/docs/models

1. model: `gemini-2.5-flash`

   name: `Gemini 2.5 Flash`

   Context: 1M

2. model: `gemini-2.0-flash`

   name: `Gemini 2.0 Flash`

   Context: 256K

---

## NVIDIA NIM

Model list: https://build.nvidia.com/models

1. model: `nvidia/nemotron-3-ultra-550b-a55b`

   name: `Nemotron 3 Ultra 550B`

   Context: 1M

2. model: `google/gemma-4-31b-it`

   name: `Gemma 4 31B`

   Context: 262K

---

## OpenRouter

Model list: https://openrouter.ai/models

Free models carry `:free` in the ID. Without that suffix the model bills
against the user's balance — check before adding.

1. model: `nvidia/nemotron-3-super-120b-a12b:free`

   name: `Nemotron 3 Super 120B`

   Context: ?

2. model: `google/gemma-4-31b-it:free`

   name: `Gemma 4 31B`

   Context: 262K

---

## Notes

Entries above are the ones already shipping in the app, kept as a starting
point. Replace or extend them freely.

Two things worth checking on the next pass: Google has released newer Flash
generations than the 2.x pair listed here, and model IDs at every provider get
renamed or retired without warning. The app's own picker pulls the live list
from each provider — that is the source to verify against.
