# artifacts-board-data

Canonical card data for [Artifacts 工件看板](https://artifacts-board.vercel.app).

- **Source of truth (local write):** `/home/box/agent-data/docs/artifacts-data.json` on Grok Bot
- **Published:** this repo `main/artifacts-data.json`
- **Consumers:** static `artifacts-board.html` on Vercel fetches via jsDelivr / GitHub raw (`?t=` cache-bust)

Content updates: edit + push JSON only. Redeploy Vercel only when HTML/JS/CSS changes.

## GitHub Pages

Live board: https://liush2yuxjtu.github.io/artifacts-board-data/

Shell is `index.html`; data is `artifacts-data.json`. Content updates only need syncing the JSON.
