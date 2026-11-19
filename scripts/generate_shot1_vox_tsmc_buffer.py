import cv2
import numpy as np
import os
import subprocess

def grade_vox_cinematic(frame):
    """
    High-end Vox documentary color grading:
    - Retains natural satellite ocean blues and crisp white clouds
    - Enhances landmass warmth with rich sandstone/ochre
    - Punches contrast with a smooth cinematic S-curve
    - Adds subtle warm film highlights without muddying
    """
    f = frame.astype(np.float32) / 255.0
    
    # Smooth Hermite film contrast S-curve: 3*f^2 - 2*f^3
    f_contrast = 3.0 * (f ** 2) - 2.0 * (f ** 3)
    
    b, g, r = f_contrast[:, :, 0], f_contrast[:, :, 1], f_contrast[:, :, 2]
    
    # Natural color balance: deep sapphire ocean, warm land, pure white clouds
    r_graded = np.clip(r * 1.04 + 0.02 * g, 0.0, 1.0)
    g_graded = np.clip(g * 1.01, 0.0, 1.0)
    b_graded = np.clip(b * 1.05, 0.0, 1.0)
    
    graded = np.dstack([b_graded, g_graded, r_graded])
    
    # Subtle cinematic edge vignette
    h, w = frame.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt(((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.0 - 0.28 * (dist ** 2.2), 0.45, 1.0)
    graded = graded * vig[:, :, np.newaxis]
    
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def grade_tsmc_building(frame):
    """Grades TSMC building photograph with documentary warmth and crisp architectural punch."""
    f = frame.astype(np.float32) / 255.0
    
    # Film contrast S-curve
    f_contrast = 3.0 * (f ** 2) - 2.0 * (f ** 3)
    b, g, r = f_contrast[:, :, 0], f_contrast[:, :, 1], f_contrast[:, :, 2]
    
    # Warm golden hour architectural glow
    r_out = np.clip(r * 1.06 + 0.02, 0.0, 1.0)
    g_out = np.clip(g * 1.02, 0.0, 1.0)
    b_out = np.clip(b * 0.95, 0.0, 1.0)
    
    graded = np.dstack([b_out, g_out, r_out])
    
    # Subtle corner vignette
    h, w = frame.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt(((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.0 - 0.22 * (dist ** 2.0), 0.55, 1.0)
    graded = graded * vig[:, :, np.newaxis]
    
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def remove_google_earth_watermark(frame):
    """Inpaints and cleanly erases the Google Earth watermark at Y:884-920, X:863-1057."""
    h, w = frame.shape[:2]
    # Watermark bounding box in 1080p frame
    y1, y2 = 870, 935
    x1, x2 = 845, 1075
    patch = frame[y1:y2, x1:x2]
    gray = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)
    if (gray > 165).any():
        mask = np.zeros((h, w), dtype=np.uint8)
        mask[y1:y2, x1:x2] = 255
        frame = cv2.inpaint(frame, mask, inpaintRadius=9, flags=cv2.INPAINT_TELEA)
    return frame

def main():
    print("Building Shot 01 V4: Pristine Video + TSMC Headquarters Building Buffer...")
    
    earth_vid_path = "assets_tsmc/google_earth_taoyuan.mp4.mkv"
    tsmc_img_path = "demo-tsmc-v2/assets/images/tsmc_headquarters_building.jpg"
    
    cap_earth = cv2.VideoCapture(earth_vid_path)
    tsmc_img = cv2.imread(tsmc_img_path)
    
    if not cap_earth.isOpened():
        raise RuntimeError(f"Could not open {earth_vid_path}")
    if tsmc_img is None:
        raise RuntimeError(f"Could not open {tsmc_img_path}")
        
    width, height = 1920, 1080
    fps = 24.0
    total_frames = 202 # 8.42s at 24fps
    
    tmp_out = "demo-tsmc-v2/assets/video/tmp_shot1_v4.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(tmp_out, fourcc, fps, (width, height))
    
    earth_total = int(cap_earth.get(cv2.CAP_PROP_FRAME_COUNT))
    tsmc_graded_base = grade_tsmc_building(cv2.resize(tsmc_img, (width, height)))
    
    # Pre-render frames
    for f_idx in range(total_frames):
        t = f_idx / fps
        
        # 1. Earth Zoom Phase (0.00s to 6.33s, frames 0 to 152)
        if f_idx < 160:
            if f_idx < 65: # Space rotation
                p = f_idx / 65.0
                src_fno = int(p * 80)
            elif f_idx < 128: # Plunge to Taiwan Strait
                p = (f_idx - 65) / (128 - 65)
                p_curved = p ** 1.35
                src_fno = int(80 + p_curved * (270 - 80))
            else: # Zoom into Hsinchu
                p = (f_idx - 128) / (160 - 128)
                src_fno = int(270 + p * (435 - 270))
                
            src_fno = min(src_fno, earth_total - 1)
            cap_earth.set(cv2.CAP_PROP_POS_FRAMES, src_fno)
            ret, frame = cap_earth.read()
            if not ret:
                frame = np.zeros((height, width, 3), dtype=np.uint8)
                
            # Clean watermark
            frame = remove_google_earth_watermark(frame)
            
            # Apply Vox cinematic color grading (clean, no burned-in text)
            graded = grade_vox_cinematic(frame)
        else:
            graded = np.zeros((height, width, 3), dtype=np.uint8)
            
        # 2. CẢNH ĐỆM (BUFFER SCENE): TSMC Headquarters Building (frames 148 to 201, 6.16s - 8.42s)
        if f_idx >= 148:
            buffer_p = (f_idx - 148) / (total_frames - 1 - 148) # 0.0 to 1.0
            
            # Ken Burns architectural slow push-in: scale 1.00 -> 1.08, subtle pan up
            scale = 1.00 + buffer_p * 0.07
            shift_y = int(buffer_p * 15) # gentle vertical lift
            
            M = cv2.getRotationMatrix2D((width // 2, height // 2), 0, scale)
            M[1, 2] -= shift_y
            tsmc_warped = cv2.warpAffine(tsmc_graded_base, M, (width, height), borderMode=cv2.BORDER_REFLECT)
            
            # Cross-fade dissolve: starts at 148, full TSMC by frame 164
            dissolve_alpha = np.clip((f_idx - 148) / 16.0, 0.0, 1.0)
            # Smooth S-curve for dissolve
            dissolve_alpha = dissolve_alpha * dissolve_alpha * (3 - 2 * dissolve_alpha)
            
            if f_idx < 164:
                graded = cv2.addWeighted(graded, 1.0 - dissolve_alpha, tsmc_warped, dissolve_alpha, 0)
            else:
                graded = tsmc_warped
                
            # Quick cinematic motion punch on final 8 frames for smooth cut to Scene 2 desk
            if f_idx >= 194:
                punch_p = (f_idx - 194) / 7.0
                blur_scales = [1.0, 1.0 + punch_p * 0.04, 1.0 + punch_p * 0.08]
                accum = np.zeros_like(graded, dtype=np.float32)
                for bs in blur_scales:
                    Mb = cv2.getRotationMatrix2D((width // 2, height // 2), 0, bs)
                    warped = cv2.warpAffine(graded, Mb, (width, height), borderMode=cv2.BORDER_REFLECT)
                    accum += warped.astype(np.float32)
                graded = np.clip(accum / len(blur_scales), 0, 255).astype(np.uint8)
                
        writer.write(graded)
        if f_idx % 20 == 0 or f_idx == total_frames - 1:
            print(f"Processed frame {f_idx}/{total_frames} ({t:.2f}s)")
            
    writer.release()
    cap_earth.release()
    print("Raw render complete. Encoding H.264 MP4 with FFmpeg...")
    
    final_mp4 = "demo-tsmc-v2/assets/video/shot1_map_veo.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-i", tmp_out,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-movflags", "+faststart",
        final_mp4
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_out):
        os.remove(tmp_out)
    print(f"SUCCESS: Created clean {final_mp4} with TSMC Headquarters building buffer!")

if __name__ == "__main__":
    main()
