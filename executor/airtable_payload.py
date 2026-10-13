# Emits Airtable records (fields by name) for table tbl2otewAXooKZSKm in base appoOASxNv8XKlrvQ. Upsert key: card_id.
import json
d=json.load(open('/home/box/agent-data/docs/artifacts-data.json'))
out=[]
for c in d['cards']:
  out.append({"card_id":c['id'],"title":c['title'],"status":c['col'],
   "owner":"ny (user)" if c['col']=='human' or (c.get('human') and c['human']!='无') else "Grok Bot",
   "blocker":c.get('human','') if c['col'] in('blocked','human') else '',
   "last_update":c.get('stamp') or d['updated'],
   "source_url":"https://liush2yuxjtu.github.io/artifacts-board-data/",
   "notes":f"detail: {c.get('detail','')}\nnext: {c.get('next','')}\nhuman: {c.get('human','')}"})
print(json.dumps(out,ensure_ascii=False))
