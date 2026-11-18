import os
import urllib.request
import ssl
import cv2
import numpy as np

OUTPUT_DIR = "assets_tsmc/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

IMAGE_MAP = {
    "morris_chang": "https://upload.wikimedia.org/wikipedia/commons/4/47/11.21_2020_APEC%E6%9A%A8%E7%B6%93%E6%BF%9F%E9%A0%98%E8%A2%96%E6%9C%83%E8%AD%B0%E6%9C%83%E5%BE%8C%E8%A8%98%E8%80%85%E6%9C%83_%2850628253717%29_%28cropped2%29.jpg",
    "andy_grove": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Intel_Inside_%283607903903%29_%28cropped%29.jpg",
    "jensen_huang": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Jensen_Huang_Stanford_2026-04-30_010_%28cropped%29.jpg/1280px-Jensen_Huang_Stanford_2026-04-30_010_%28cropped%29.jpg",
    "mount_aso": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/20140516%E9%98%BF%E8%98%87%E5%B1%B1%E5%BA%83%E5%9F%9F.jpg/1280px-20140516%E9%98%BF%E8%98%87%E5%B1%B1%E5%BA%83%E5%9F%9F.jpg",
    "tim_cook": "https://upload.wikimedia.org/wikipedia/commons/1/10/Tim_Cook_in_New_York_City_-_2026_%28cropped%29.jpg",
    "steve_jobs": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Steve_Jobs_Headshot_2010_%28cropped_6%29.jpg/1280px-Steve_Jobs_Headshot_2010_%28cropped_6%29.jpg",
    "lehman_brothers": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Lehman_Brothers_Times_Square_by_David_Shankbone.jpg/1280px-Lehman_Brothers_Times_Square_by_David_Shankbone.jpg",
    "hsinchu_park": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Taiwan_Photon_Source_2013.jpg/1280px-Taiwan_Photon_Source_2013.jpg",
    "silicon_wafer": "https://upload.wikimedia.org/wikipedia/commons/f/ff/ICC_2008_Poland_Silicon_Wafer_1_edit.png"
}

def apply_archival_vintage_grade(input_path, output_path):
    img = cv2.imread(input_path)
    if img is None:
        print(f"Warning: Could not read image {input_path}")
        return
    
    # 1. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. CLAHE for punchy dramatic historical documentary contrast
    clahe = cv2.createCLAHE(clipLimit=2.8, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)
    
    # 3. Add Film Grain
    h, w = enhanced.shape
    noise = np.random.normal(0, 12, (h, w)).astype(np.float32)
    noisy = np.clip(enhanced.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    
    # 4. Archival warm tone
    bgr = cv2.cvtColor(noisy, cv2.COLOR_GRAY2BGR)
    sepia_b = np.clip(bgr[:, :, 0] * 0.88, 0, 255).astype(np.uint8)
    sepia_g = np.clip(bgr[:, :, 1] * 0.96, 0, 255).astype(np.uint8)
    sepia_r = np.clip(bgr[:, :, 2] * 1.06, 0, 255).astype(np.uint8)
    vintage_result = cv2.merge([sepia_b, sepia_g, sepia_r])
    
    # 5. Subtle Vignette
    Y, X = np.ogrid[:h, :w]
    center_y, center_x = h / 2, w / 2
    dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    vignette = 1.0 - 0.32 * (dist_from_center / max_dist)**2
    for c in range(3):
        vintage_result[:, :, c] = np.clip(vintage_result[:, :, c] * vignette, 0, 255).astype(np.uint8)
        
    cv2.imwrite(output_path, vintage_result)
    print(f"Gradded vintage print: {output_path}")

ctx = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8'
}

for name, url in IMAGE_MAP.items():
    raw_path = os.path.join(OUTPUT_DIR, f"{name}_raw.jpg")
    vintage_path = os.path.join(OUTPUT_DIR, f"{name}_vintage.jpg")
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
            with open(raw_path, 'wb') as f:
                f.write(resp.read())
        print(f"Downloaded: {name}")
        apply_archival_vintage_grade(raw_path, vintage_path)
    except Exception as e:
        print(f"Failed {name}: {e}")
