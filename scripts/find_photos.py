import urllib.request, ssl, re

ctx = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

urls = [
    'https://www.wealth.com.tw/articles/489ca646-6bf4-41d3-a5aa-28340d6cfa87',
    'https://city.gvm.com.tw/article/117391'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'https://[^\s"\'<>]+\.(?:jpg|png|webp)', html)
            print(f"Results for {url}:")
            for m in set(matches):
                if 'upload' in m or 'article' in m or 'images' in m:
                    print("  ", m)
    except Exception as e:
        print(f"Error on {url}: {e}")
