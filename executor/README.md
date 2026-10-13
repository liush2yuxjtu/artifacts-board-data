# Artifacts Board — executor app

Self-contained runner for the Artifacts 看板 (never call it "Archifax").

- Data (source of truth): `/home/box/agent-data/docs/artifacts-data.json`
- Remote repo: https://github.com/liush2yuxjtu/artifacts-board-data (main)
- Live board (primary): https://liush2yuxjtu.github.io/artifacts-board-data/
- Legacy shell (keep, do not delete yet): https://artifacts-board.vercel.app
- Workflow/HITL rules: `/home/box/agent-data/docs/ARTIFACTS-BOARD-WORKFLOW.md`
- Airtable mirror: base `appoOASxNv8XKlrvQ` (ChatGPT Work Hub) → table `tbl2otewAXooKZSKm` "Agent Handoff / Artifacts", key `card_id`
- Full handoff: `/home/box/agent-data/docs/HANDOFF-2026-10-13.md`

## Usage
```bash
B=/home/box/agent-data/executor-apps/artifacts-board/board
$B list            # all cards; `$B list blocked` to filter (done|progress|human|blocked)
$B show c22
$B set c22 col done          # fields: col title detail next human stamp
$B sync            # push JSON to GitHub (needs git push auth on box); Pages updates itself
$B verify          # check Pages 200 + remote JSON updated/count
$B airtable-payload  # JSON records for Airtable upsert (use user-Airtable MCP, match on card_id)
```
Rules: card edits = JSON only + sync; never `vercel --prod` for card changes; shell HTML edits go to `docs/artifacts-board.html` → repo `index.html`.
