import subprocess
import json

video_ids = ['ajlcizR9pv0', 'a2BqqHA3p6I', 'w_nbw1Kzw4g', 'FgWv3zpBKks']
for vid in video_ids:
    cmd = ['yt-dlp', '--dump-json', f'https://www.youtube.com/watch?v={vid}']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        d = json.loads(res.stdout)
        ch = d.get('channel')
        ch_url = d.get('channel_url')
        subs = d.get('channel_follower_count')
        ud = d.get('upload_date')
        print(f"ID: {vid} | Channel: {ch} | Subs: {subs} | Uploaded: {ud} | URL: {ch_url}")
