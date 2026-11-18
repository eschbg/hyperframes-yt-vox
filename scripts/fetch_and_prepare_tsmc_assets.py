import os
import urllib.request
import json
import cv2
import numpy as np

ASSETS_DIR = "assets_tsmc/images"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Curated list of historical stock/wikimedia images for TSMC documentary
IMAGE_SOURCES = [
    {
        "id": "taiwan_strait_map",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Taiwan_Strait_in_East_Asia.svg/1280px-Taiwan_Strait_in_East_Asia.svg.png",
        "desc": "Taiwan Strait map"
    },
    {
        "id": "morris_chang_young",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Morris_Chang_at_APEC_2018.jpg/800px-Morris_Chang_at_APEC_2018.jpg",
        "desc": "Morris Chang portrait"
    },
    {
        "id": "intel_andy_grove",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Andy_Grove_1997.jpg/800px-Andy_Grove_1997.jpg",
        "desc": "Andy Grove Intel CEO"
    },
    {
        "id": "jensen_huang_early",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Jensen_Huang_at_Computex_2023.jpg/800px-Jensen_Huang_at_Computex_2023.jpg",
        "desc": "Jensen Huang Nvidia"
    },
    {
        "id": "asml_euv_machine",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/ASML_High-NA_EUV_lithography_system.jpg/1280px-ASML_High-NA_EUV_lithography_system.jpg",
        "desc": "ASML EUV machine"
    },
    {
        "id": "kumamoto_aso",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Mount_Aso_crater_2012.jpg/1280px-Mount_Aso_crater_2012.jpg",
        "desc": "Mount Aso Kumamoto crater"
    },
    {
        "id": "cleanroom_wafer",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Silicon_wafer_with_microprocessor_dies.jpg/1280px-Silicon_wafer_with_microprocessor_dies.jpg",
        "desc": "Silicon wafer microprocessor dies"
    },
    {
        "id": "tim_cook",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Tim_Cook_2017_%28cropped%29.jpg/800px-Tim_Cook_2017_%28cropped%29.jpg",
        "desc": "Tim Cook Apple CEO"
    },
    {
        "id": "lehman_brothers_collapse",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Lehman_Brothers_Times_Square_by_David_Shankbone.jpg/1280px-Lehman_Brothers_Times_Square_by_David_Shankbone.jpg",
        "desc": "Lehman Brothers collapse 2008"
    },
    {
        "id": "steve_jobs_iphone",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg/800px-Steve_Jobs_Headshot_2010-CROP_%28cropped_2%29.jpg",
        "desc": "Steve Jobs Apple"
    }
]

def apply_archival_vintage_grade(input_path, output_path):
    """
    Applies high-contrast archival B&W / Sepia tint with film grain
    matching @CEOzoned and @BuiltonYou scrapbook documentary aesthetic.
    """
    img = cv2.imread(input_path)
    if img is None:
        return
    
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for dramatic lighting
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # 3. Add Film Grain
    h, w = enhanced.shape
    noise = np.random.normal(0, 10, (h, w)).astype(np.float32)
    noisy = np.clip(enhanced.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    
    # 4. Convert back to BGR and apply warm archival sepia tint
    bgr = cv2.cvtColor(noisy, cv2.COLOR_GRAY2BGR)
    # Warm sepia matrix
    sepia_b = np.clip(bgr[:, :, 0] * 0.88, 0, 255).astype(np.uint8)
    sepia_g = np.clip(bgr[:, :, 1] * 0.95, 0, 255).astype(np.uint8)
    sepia_r = np.clip(bgr[:, :, 2] * 1.05, 0, 255).astype(np.uint8)
    vintage_result = cv2.merge([sepia_b, sepia_g, sepia_r])
    
    # 5. Vignette effect
    Y, X = np.ogrid[:h, :w]
    center_y, center_x = h / 2, w / 2
    dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
    max_dist = np.sqrt(center_x**2 + center_y**2)
    vignette = 1.0 - 0.35 * (dist_from_center / max_dist)**2
    for c in range(3):
        vintage_result[:, :, c] = np.clip(vintage_result[:, :, c] * vignette, 0, 255).astype(np.uint8)
        
    cv2.imwrite(output_path, vintage_result)
    print(f"Processed vintage print: {output_path}")

def main():
    print("--- Fetching Archival Images & Processing Vintage Prints ---")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Antigravity/2.0 Documentary Bot'}
    
    import ssl
    ctx = ssl._create_unverified_context()
    for item in IMAGE_SOURCES:
        raw_path = os.path.join(ASSETS_DIR, f"{item['id']}_raw.jpg")
        aged_path = os.path.join(ASSETS_DIR, f"{item['id']}_vintage.jpg")
        
        try:
            req = urllib.request.Request(item['url'], headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                with open(raw_path, 'wb') as f:
                    f.write(resp.read())
            print(f"Downloaded: {item['id']}")
            apply_archival_vintage_grade(raw_path, aged_path)
        except Exception as e:
            print(f"Failed to fetch {item['id']}: {e}")

if __name__ == "__main__":
    main()
