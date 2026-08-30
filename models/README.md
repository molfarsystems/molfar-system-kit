# Models

English only — this folder is mostly model names and numbers, which do not need translating.

- [`providers.md`](providers.md) — the three supported providers, what each is good for, how their free tiers behave
- [`recommended.md`](recommended.md) — which model to put in which seat
- [`catalogue.md`](catalogue.md) — specific models with IDs, context windows and prices
- [`app-defaults.md`](app-defaults.md) — working file: the model list the app ships with

## The one rule worth knowing

**Do not fill all four seats with the same model.** Four copies of one model produce four versions of the same answer, and the Orchestrator will report perfect agreement that means nothing.

The value comes from disagreement. Mix providers, mix model families, and the places where they diverge are exactly the places worth a second look.

## Model names go stale

Providers rename, deprecate and replace models constantly. If a model listed here is gone, check the provider's own model list — the app pulls the current list when you open the model picker.
