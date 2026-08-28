# API keys

Molfar System has no server and no accounts. It talks to AI providers using **your** keys, which stay on your device.

All three supported providers issue free keys. You need at least one.

---

## Where to paste a key

Menu → **AI Settings** → find the provider's field → paste → tap the **diskette** icon.

The provider turns on automatically. The **Test** button sends a real request and tells you whether the key works.

---

## Google AI Studio

1. Open [aistudio.google.com/apikey](https://aistudio.google.com/apikey)
2. Sign in with a Google account
3. **Create API key**
4. Copy it and paste into the Google field in AI Settings

No payment card, no billing setup. This is the shortest path to a working app.

---

## NVIDIA NIM

1. Open [build.nvidia.com](https://build.nvidia.com)
2. Sign up or sign in
3. Open **any** model page
4. Click **Get API Key**
5. Copy and paste into the NVIDIA field

The key is account-wide even though it is issued from a model page — you do not need a separate key per model. People often look for a settings screen and get stuck; there isn't one.

---

## OpenRouter

1. Open [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up or sign in
3. **Create Key**
4. Copy and paste into the OpenRouter field

**Free and paid models live side by side here.** In the app, paid models are marked with `$` and draw from your OpenRouter balance. Free ones usually have `:free` in the name. If you never top up your balance, you simply cannot be charged — but check the marking before picking a model, or a round will fail with a billing error.

Web search through OpenRouter is also billed. The app warns you before enabling it.

---

## Where keys are stored

In the app's own folder on your device. They are never sent to any Molfar server — there is no Molfar server. At request time each key goes to its own provider and nowhere else.

**Uninstalling the app deletes them,** along with everything else. Keep your keys somewhere you can find them again, in a password manager or wherever you keep such things.

---

## Free tier limits

Every free tier has limits — usually requests per minute and per day.

The way this bites in practice: a meeting sends one request per participant **simultaneously**. Four participants on the same provider means four requests in the same second, against the same per-minute quota.

Spread your seats across providers and this stops being a problem.

If a seat starts failing mid-session, a limit is the most likely cause. Wait a minute, or switch that seat to a different provider.
