# App default models

Working file, not user documentation. This is the list that goes into the app
as `default_models` in `tools/providers_registry.py` — the models a person sees
in the picker before they add anything of their own.

**Who edits what.** You fill this in by hand. When an update is being prepared,
the list is read from here and written into the registry, so the two never
drift apart.

**Order matters.** The order within a provider is the order shown in the app's
picker. Put the model you want people to reach for first at number 1.

**Format is strict** — exactly two lines per model, in this order:

```
N. `model-id`
   Display name
```

The ID goes in backticks, on its own line. The display name goes on the next
line, indented. Nothing else between entries. Keep display names short — they
appear on a phone as `G · Gemini 2.5 Flash`, and the provider prefix is already
eating space.

Only models that work on a free tier belong here. Anything paid is a choice the
user makes deliberately, not a default.

---

## Google AI Studio

Model list: https://ai.google.dev/gemini-api/docs/models

1. `gemini-2.5-flash`
   Gemini 2.5 Flash

2. `gemini-2.0-flash`
   Gemini 2.0 Flash

---

## NVIDIA NIM

Model list: https://build.nvidia.com/models

1. `nvidia/nemotron-3-ultra-550b-a55b`
   Nemotron 3 Ultra 550B

2. `google/gemma-4-31b-it`
   Gemma 4 31B

---

## OpenRouter

Model list: https://openrouter.ai/models

Free models carry `:free` in the ID. Without that suffix the model bills
against the user's balance — check before adding.

1. `nvidia/nemotron-3-super-120b-a12b:free`
   Nemotron 3 Super 120B

2. `google/gemma-4-31b-it:free`
   Gemma 4 31B

---

## Notes

Entries above are the ones already shipping in the app, kept as a starting
point. Replace or extend them freely.

Two things worth checking on the next pass: Google has released newer Flash
generations than the 2.x pair listed here, and model IDs at every provider get
renamed or retired without warning. The app's own picker pulls the live list
from each provider — that is the source to verify against.
