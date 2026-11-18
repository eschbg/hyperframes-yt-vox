import os
import shutil

# Ensure directory structure
os.makedirs("demo-tsmc-v2/assets/audio", exist_ok=True)
os.makedirs("demo-tsmc-v2/assets/images", exist_ok=True)
os.makedirs("demo-tsmc-v2/assets/video", exist_ok=True)
os.makedirs("demo-tsmc-v2/assets/sfx", exist_ok=True)

# Copy VO files
vo_map = {
    "scene_01.mp3": "assets_tsmc/audio/scene_01.mp3",
    "scene_02.mp3": "assets_tsmc/audio/scene_02.mp3",
    "scene_03.mp3": "assets_tsmc/audio/scene_03.mp3",
    "scene_10.mp3": "assets_tsmc/audio/scene_10.mp3",
    "scene_11.mp3": "assets_tsmc/audio/scene_11.mp3",
}

for dst_name, src_path in vo_map.items():
    if os.path.exists(src_path):
        shutil.copy(src_path, os.path.join("demo-tsmc-v2/assets/audio", dst_name))

# Copy BGM
if os.path.exists("demo-tsmc/assets/audio/act1_cinematic_score.mp3"):
    shutil.copy("demo-tsmc/assets/audio/act1_cinematic_score.mp3", "demo-tsmc-v2/assets/audio/cinematic_score.mp3")

# Copy SFX
sfx_files = ["sub_drone.wav", "impact_boom.wav", "marker_wipe.wav", "mouse_click.wav"]
for s in sfx_files:
    for src in [f"assets_tsmc/sfx/{s}", f"demo-tsmc/assets/sfx/{s}"]:
        if os.path.exists(src):
            shutil.copy(src, os.path.join("demo-tsmc-v2/assets/sfx", s))
            break

# Copy Videos
vids = ["taiwan_strait_hook.mp4", "cleanroom_litho_clip.mp4", "cleanroom_wafer_clip.mp4"]
for v in vids:
    src = f"demo-tsmc/assets/{v}"
    if os.path.exists(src):
        shutil.copy(src, os.path.join("demo-tsmc-v2/assets/video", v))

print("Assets staged successfully for demo-tsmc-v2!")
