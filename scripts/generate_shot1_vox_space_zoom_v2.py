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
    
    # Natural color enhancement: deep navy ocean, warm land, pure white clouds
    r_graded = np.clip(r * 1.04 + 0.02 * g, 0.0, 1.0)
    g_graded = np.clip(g * 1.01, 0.0, 1.0)
    b_graded = np.clip(b * 1.06, 0.0, 1.0)
    
    graded = np.dstack([b_graded, g_graded, r_graded])
    
    # Subtle cinematic edge vignette
    h, w = frame.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt(((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.0 - 0.28 * (dist ** 2.2), 0.4, 1.0)
    graded = graded * vig[:, :, np.newaxis]
    
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def grade_cleanroom_amber(frame):
    """Grades cleanroom footage into authentic golden-amber semiconductor lithography glow."""
    f = frame.astype(np.float32) / 255.0
    b, g, r = f[:, :, 0], f[:, :, 1], f[:, :, 2]
    
    # Warm amber shift (lithography yellow/amber light)
    r_out = np.clip(r * 1.15 + 0.05, 0.0, 1.0)
    g_out = np.clip(g * 1.02 + 0.02, 0.0, 1.0)
    b_out = np.clip(b * 0.75, 0.0, 1.0)
    
    amber = np.dstack([b_out, g_out, r_out])
    return np.clip(amber * 255.0, 0, 255).astype(np.uint8)

def remove_google_earth_watermark(frame):
    """Inpaints and masks out the Google Earth logo at bottom center."""
    h, w = frame.shape[:2]
    patch = frame[h - 95:h - 25, w // 2 - 170:w // 2 + 170]
    if (patch > 180).any():
        mask = np.zeros((h, w), dtype=np.uint8)
        mask[h - 95:h - 25, w // 2 - 170:w // 2 + 170] = 255
        frame = cv2.inpaint(frame, mask, inpaintRadius=7, flags=cv2.INPAINT_TELEA)
    return frame

def main():
    print("Building Shot 01 V3: Clean Video (No OpenCV text, no ???? marks, logo removed, cleanroom buffer)...")
    
    earth_vid_path = "assets_tsmc/google_earth_taoyuan.mp4.mkv"
    fab_vid_path = "assets_tsmc/cleanroom_fab.mp4.mkv"
    
    cap_earth = cv2.VideoCapture(earth_vid_path)
    cap_fab = cv2.VideoCapture(fab_vid_path)
    
    if not cap_earth.isOpened():
        raise RuntimeError(f"Could not open {earth_vid_path}")
    if not cap_fab.isOpened():
        raise RuntimeError(f"Could not open {fab_vid_path}")
        
    width, height = 1920, 1080
    fps = 24.0
    total_frames = 202 # 8.42s at 24fps
    
    tmp_out = "demo-tsmc-v2/assets/video/tmp_shot1_v3.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(tmp_out, fourcc, fps, (width, height))
    
    earth_total = int(cap_earth.get(cv2.CAP_PROP_FRAME_COUNT))
    fab_fps = cap_fab.get(cv2.CAP_PROP_FPS)
    
    for f_idx in range(total_frames):
        t = f_idx / fps
        
        # 1. Earth Zoom Phase (0.00s to 6.58s, frames 0 to 160)
        if f_idx < 162:
            if f_idx < 65: # Space rotation
                p = f_idx / 65.0
                src_fno = int(p * 80)
            elif f_idx < 128: # Plunge to Taiwan Strait
                p = (f_idx - 65) / (128 - 65)
                p_curved = p ** 1.35
                src_fno = int(80 + p_curved * (270 - 80))
            else: # Zoom into Hsinchu
                p = (f_idx - 128) / (162 - 128)
                src_fno = int(270 + p * (435 - 270))
                
            src_fno = min(src_fno, earth_total - 1)
            cap_earth.set(cv2.CAP_PROP_POS_FRAMES, src_fno)
            ret, frame = cap_earth.read()
            if not ret:
                frame = np.zeros((height, width, 3), dtype=np.uint8)
                
            # Remove watermark
            frame = remove_google_earth_watermark(frame)
            
            # Apply Vox cinematic color grading (rich blues, crisp clouds, warm land)
            graded = grade_vox_cinematic(frame)
            
            # Draw ONLY tactical vector graphic lines (NO TEXT - all text will be sharp HTML):
            # Dynamic Red dashed line down Taiwan Strait (frames 68 to 128)
            if 68 <= f_idx < 128:
                ts_p = (f_idx - 68) / (128 - 68)
                p_start = (760, 280)
                p_end = (980, 840)
                line_len = int(np.sqrt((p_end[0] - p_start[0])**2 + (p_end[1] - p_start[1])**2))
                cur_dist = min(line_len, int(ts_p * line_len * 1.5))
                ux = (p_end[0] - p_start[0]) / line_len
                uy = (p_end[1] - p_start[1]) / line_len
                
                dash = 16
                for d in range(0, cur_dist, dash * 2):
                    pt1 = (int(p_start[0] + d * ux), int(p_start[1] + d * uy))
                    pt2 = (int(p_start[0] + min(cur_dist, d + dash) * ux), int(p_start[1] + min(cur_dist, d + dash) * uy))
                    cv2.line(graded, pt1, pt2, (40, 40, 225), 3, cv2.LINE_AA)
                    
            # Tactical Targeting Reticle on Hsinchu (frames 128 to 162)
            elif 128 <= f_idx < 162:
                tx, ty = 960, 530
                reticle_s = max(40, int(75 - ((f_idx - 128) / 30.0) * 35))
                c_red = (40, 40, 225)
                # Corner brackets
                cv2.line(graded, (tx - reticle_s, ty - reticle_s), (tx - reticle_s + 20, ty - reticle_s), c_red, 3)
                cv2.line(graded, (tx - reticle_s, ty - reticle_s), (tx - reticle_s, ty - reticle_s + 20), c_red, 3)
                cv2.line(graded, (tx + reticle_s, ty - reticle_s), (tx + reticle_s - 20, ty - reticle_s), c_red, 3)
                cv2.line(graded, (tx + reticle_s, ty - reticle_s), (tx + reticle_s, ty - reticle_s + 20), c_red, 3)
                cv2.line(graded, (tx - reticle_s, ty + reticle_s), (tx - reticle_s + 20, ty + reticle_s), c_red, 3)
                cv2.line(graded, (tx - reticle_s, ty + reticle_s), (tx - reticle_s, ty + reticle_s - 20), c_red, 3)
                cv2.line(graded, (tx + reticle_s, ty + reticle_s), (tx + reticle_s - 20, ty + reticle_s), c_red, 3)
                cv2.line(graded, (tx + reticle_s, ty + reticle_s), (tx + reticle_s, ty + reticle_s - 20), c_red, 3)
                cv2.circle(graded, (tx, ty), 3, c_red, -1)
                
        # 2. CẢNH ĐỆM (BUFFER SCENE): TSMC Cleanroom Fab (frames 158 to 201)
        if f_idx >= 158:
            buffer_p = (f_idx - 158) / (total_frames - 1 - 158)
            fab_fno = int((0.5 + buffer_p * 2.2) * fab_fps)
            cap_fab.set(cv2.CAP_PROP_POS_FRAMES, fab_fno)
            ret_fab, fab_frame = cap_fab.read()
            if ret_fab:
                fab_resized = cv2.resize(fab_frame, (width, height))
                fab_graded = grade_cleanroom_amber(fab_resized)
                
                push_scale = 1.0 + buffer_p * 0.08
                M_push = cv2.getRotationMatrix2D((width // 2, height // 2), 0, push_scale)
                fab_graded = cv2.warpAffine(fab_graded, M_push, (width, height))
                
                # Cross-fade dissolve into buffer scene
                blend_alpha = np.clip((buffer_p - 0.0) / 0.25, 0.0, 1.0)
                graded = cv2.addWeighted(graded, 1.0 - blend_alpha, fab_graded, blend_alpha, 0)
                
                # Radial motion punch at final 10 frames
                if f_idx >= 190:
                    punch_p = (f_idx - 190) / 11.0
                    blur_scales = [1.0, 1.0 + punch_p * 0.08, 1.0 + punch_p * 0.16]
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
    cap_fab.release()
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
    print(f"SUCCESS: Created clean {final_mp4}")

if __name__ == "__main__":
    main()
