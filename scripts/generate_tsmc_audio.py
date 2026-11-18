import os
import re
import asyncio
import subprocess
import edge_tts

VOICE = "ja-JP-KeitaNeural"
OUTPUT_DIR = "assets_tsmc/audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("scripts/tsmc_script_jp.md", "r", encoding="utf-8") as f:
    content = f.read()

acts = re.split(r"## 第(\d)幕", content)
scenes = []
scene_idx = 1

for i in range(1, len(acts), 2):
    act_num = int(acts[i])
    act_body = acts[i+1]
    rows = re.findall(r"\|\s*\*\*([0-9:]+\s*-\s*[0-9:]+)\*\*\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|", act_body)
    for time_range, vo, visual, telop, sfx in rows:
        vo_clean = vo.strip().replace("<br>", " ").replace("\n", " ")
        scenes.append({
            "index": scene_idx,
            "act": act_num,
            "time_range": time_range.strip(),
            "vo": vo_clean,
            "visual": visual.strip(),
            "telop": telop.strip(),
            "sfx": sfx.strip()
        })
        scene_idx += 1

print(f"Total scenes parsed: {len(scenes)}")

async def generate_scene_audio(scene):
    idx = f"{scene['index']:02d}"
    mp3_path = os.path.join(OUTPUT_DIR, f"scene_{idx}.mp3")
    vtt_path = os.path.join(OUTPUT_DIR, f"scene_{idx}.vtt")
    
    # edge-tts communicate
    communicate = edge_tts.Communicate(scene['vo'], VOICE, rate="-4%", pitch="+0Hz")
    submaker = edge_tts.SubMaker()
    
    with open(mp3_path, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
                
    srt_content = submaker.get_srt()
    vtt_content = "WEBVTT\n\n" + re.sub(r'(\d{2}:\d{2}:\d{2}),(\d{3})', r'\1.\2', srt_content)
    with open(vtt_path, "w", encoding="utf-8") as f:
        f.write(vtt_content)
    
    # get duration via ffprobe
    res = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", mp3_path
    ], capture_output=True, text=True)
    duration = float(res.stdout.strip()) if res.stdout.strip() else 0.0
    print(f"Scene {idx} (Act {scene['act']}) generated: {duration:.2f}s | {scene['vo'][:25]}...")
    scene["audio_file"] = f"scene_{idx}.mp3"
    scene["duration"] = duration

async def main():
    print(f"--- Starting Edge-TTS Generation with {VOICE} ---")
    for sc in scenes:
        await generate_scene_audio(sc)
    
    # Save scene manifest
    import json
    with open("assets_tsmc/scenes_manifest.json", "w", encoding="utf-8") as f:
        json.dump(scenes, f, ensure_ascii=False, indent=2)
    print("All scenes generated and manifest saved to assets_tsmc/scenes_manifest.json!")

if __name__ == "__main__":
    asyncio.run(main())
