# App default models

Working file, not user documentation. This is the list that goes into the app
as `default_models` in `tools/providers_registry.py` — the models a person sees
in the picker before they add anything of their own.

**Who edits what.** You fill this in by hand. When an update is being prepared,
the list is read from here and written into the registry, so the two never
drift apart.

**Order matters.** Providers appear in the order below, and within a provider
the order is the order shown in the app's picker. Put the model you want people
to reach for first at number 1.

**Format is strict** — one field per line, blank line between them:

```
N. model: `model-id`

   name: `Display name`

   context: 1M

   price: $0,10/$0,20 per 1M
```

The blank lines are load-bearing: without them markdown runs the fields
together into a single line.

`model` and `name` go in backticks so the boundaries are unambiguous. Keep
display names short — they appear on a phone as `G · Gemini 2.5 Flash`, and the
provider prefix is already eating space.

`context` is the input window, written the short way: `1M`, `262K`, `131K`. It
is there for the user, not for the app — the registry only takes the ID and the
name.

`price` is **input/output per million tokens**, and appears **only on paid
models**. No `price` line means the model runs on a free tier. Paid models also
carry a `$` in front of the display name, so they are obvious in the picker.

---

## OpenRouter

Model list: https://openrouter.ai/models

Free models carry `:free` in the ID. Without that suffix the model bills
against the user's balance — check before adding.

1. model: `nvidia/nemotron-3-ultra-550b-a55b:free`

   name: `Nemotron 3 Ultra 550B`

   context: 1M

2. model: `nvidia/nemotron-3-super-120b-a12b:free`

   name: `Nemotron 3 Super 120B`

   context: 262K

3. model: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`

   name: `Nemotron 3 Nano Omni 30B`

   context: 256K

4. model: `nvidia/nemotron-3.5-lightning:free`

   name: `Nemotron 3.5 Lightning`

   context: 1M

5. model: `poolside/laguna-xs-2.1:free`

   name: `Laguna XS 2.1`

   context: 262K

6. model: `minimax/minimax-m3:free`

   name: `MiniMax M3`

   context: 1M

7. model: `inclusionai/ling-3.0-flash-fin:free`

   name: `Ling 3.0 Flash Fin`

   context: 262K

8. model: `minimax/minimax-m2.7:free`

   name: `MiniMax M2.7`

   context: 197K

9. model: `qwen/qwen3.8-flash`

   name: `$ Qwen 3.8 Flash`

   context: 1M

   price: $0,15/$0,47 per 1M

10. model: `z-ai/glm-5.3-flash`

    name: `$ GLM 5.3 Flash`

    context: 1M

    price: $0,05/$0,17 per 1M

11. model: `meta/muse-spark-1.2-contributor`

    name: `$ Muse Spark 1.2`

    context: 1M

    price: $0,10/$0,20 per 1M

12. model: `openai/gpt-5.6-luna`

    name: `$ GPT 5.6 Luna`

    context: 1M

    price: $0,10/$0,20 per 1M

---

## Google AI Studio

Model list: https://ai.google.dev/gemini-api/docs/models

1. model: `gemini-2.5-flash`

   name: `Gemini 2.5 Flash`

   context: 1M

---

## NVIDIA NIM

Model list: https://build.nvidia.com/models

1. model: `poolside/laguna-xs-2.1`

   name: `Laguna XS 2.1`

   context: 262K

2. model: `moonshotai/kimi-k3`

   name: `Kimi K3`

   context: 1M

3. model: `deepseek-ai/deepseek-v4-flash-0731`

   name: `DeepSeek V4 Flash`

   context: 1M

4. model: `google/diffusiongemma-26b-a4b-it`

   name: `DiffusionGemma 26B`

   context: 262K

5. model: `deepseek-ai/deepseek-v4-pro-0813`

   name: `DeepSeek V4 Pro`

   context: 1M

6. model: `nvidia/nemotron-3.5-lightning-30b-a3b`

   name: `Nemotron 3.5 Lightning 30B`

   context: 1M

7. model: `openai/gpt-oss-20b`

   name: `GPT-OSS 20B`

   context: 131K

---

## Notes

20 models, verified against the providers' own model lists: 16 free, 4 paid
(all four on OpenRouter).

Display names are derived from the model IDs, dropping the vendor prefix, the
active-parameter suffix (`a55b`, `a12b`, `a4b`) and the `-it` instruction-tuned
marker, since none of that helps a person choosing a seat.

`poolside/laguna-xs-2.1` appears twice on purpose — once free through
OpenRouter, once direct through NVIDIA NIM. Same model, two routes, and the
free one is rate-limited where the direct one is not.

Model IDs at every provider get renamed or retired without warning. The app's
own picker pulls the live list from each provider — that is the source to
verify against.
