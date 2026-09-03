# Models

English only — this folder is mostly model names and numbers, which do not need translating.

- [`providers.md`](providers.md) — the three supported providers, what each is good for, how their free tiers behave, and the one OpenRouter setting that has to be on
- [`recommended.md`](recommended.md) — which model to put in which seat
- [`catalogue.md`](catalogue.md) — all 20 models the app ships with: IDs, context windows, prices
- [`app-defaults.md`](app-defaults.md) — working file the catalogue is built from; edited by hand, read when an app update is prepared

## The one rule worth knowing

**Do not fill all four seats with the same model.** Four copies of one model produce four versions of the same answer, and the Orchestrator will report perfect agreement that means nothing.

The value comes from disagreement. Mix providers, mix model families, and the places where they diverge are exactly the places worth a second look.

**The same model from two providers does not count as two.** `Laguna XS 2.1` ships both ways; two seats running it give you one opinion twice. The catalogue groups every default model by training family for exactly this reason.

## Model names go stale

Providers rename, deprecate and replace models constantly. If a model listed here is gone, check the provider's own model list — the app pulls the current list when you open the model picker.
