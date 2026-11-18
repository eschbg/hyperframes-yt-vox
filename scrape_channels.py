import subprocess
import json

def get_channel_videos(url):
    cmd = ['yt-dlp', '--flat-playlist', '--dump-json', f'{url}/videos']
    res = subprocess.run(cmd, capture_output=True, text=True)
    videos = []
    for line in res.stdout.strip().split('\n'):
        if line.strip():
            try:
                videos.append(json.loads(line))
            except:
                pass
    videos.sort(key=lambda x: x.get('view_count') or 0, reverse=True)
    return videos[:6]

for ch in ['https://www.youtube.com/@CEOzoned', 'https://www.youtube.com/@BuiltonYou']:
    print('==============================')
    print('TOP VIDEOS FOR:', ch)
    print('==============================')
    vids = get_channel_videos(ch)
    for v in vids:
        print(f"[{v.get('id')}] {v.get('title')} | views: {v.get('view_count')} | dur: {v.get('duration')}s")
