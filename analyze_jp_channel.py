import subprocess
import json

video_ids = ['sr8mORYPzZ4', 'PWLey1yuoL0', 'GvLlfAkFJjk', 'IRNa81jyFyk', 'ToIzQheeZR0', 'LZ5KZlDE2Zo']

videos_full = []
for vid in video_ids:
    cmd = ['yt-dlp', '--dump-json', f'https://www.youtube.com/watch?v={vid}']
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if res.returncode == 0:
        d = json.loads(res.stdout)
        info = {
            'id': vid,
            'title': d.get('title'),
            'view_count': d.get('view_count'),
            'like_count': d.get('like_count'),
            'duration': d.get('duration'),
            'upload_date': d.get('upload_date'),
            'description': d.get('description', '')[:300]
        }
        videos_full.append(info)
        print(f"[{vid}] {info['title']}")
        print(f"  Views: {info['view_count']:,} | Likes: {info['like_count']} | Duration: {info['duration']}s ({info['duration']//60}m) | Date: {info['upload_date']}")

with open('jp_videos_full.json', 'w', encoding='utf-8') as f:
    json.dump(videos_full, f, ensure_ascii=False, indent=2)
