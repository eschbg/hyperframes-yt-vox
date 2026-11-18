import json

with open('assets_tsmc/scenes_manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for s in data:
    if s.get('act') == 1:
        print(f"Scene {s.get('index')}: duration={s.get('duration')}s, time_range={s.get('time_range')}")
        print(f"  VO: {s.get('vo')}")
        print(f"  Visual: {s.get('visual')}")
        print(f"  Telop: {s.get('telop')}")
        print(f"  SFX: {s.get('sfx')}")
        print("-" * 50)
