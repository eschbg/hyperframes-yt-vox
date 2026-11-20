import cv2
import numpy as np
import os
import subprocess

def grade_vox_cinematic(frame):
    f = frame.astype(np.float32) / 255.0
    f_contrast = 3.0 * (f ** 2) - 2.0 * (f ** 3)
    b, g, r = f_contrast[:, :, 0], f_contrast[:, :, 1], f_contrast[:, :, 2]
    
    r_graded = np.clip(r * 1.04 + 0.02 * g, 0.0, 1.0)
    g_graded = np.clip(g * 1.01, 0.0, 1.0)
    b_graded = np.clip(b * 1.05, 0.0, 1.0)
    graded = np.dstack([b_graded, g_graded, r_graded])
    
    h, w = frame.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt(((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.0 - 0.28 * (dist ** 2.2), 0.45, 1.0)
    graded = graded * vig[:, :, np.newaxis]
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def grade_tsmc_building(frame):
    f = frame.astype(np.float32) / 255.0
    f_contrast = 3.0 * (f ** 2) - 2.0 * (f ** 3)
    b, g, r = f_contrast[:, :, 0], f_contrast[:, :, 1], f_contrast[:, :, 2]
    
    r_out = np.clip(r * 1.06 + 0.02, 0.0, 1.0)
    g_out = np.clip(g * 1.02, 0.0, 1.0)
    b_out = np.clip(b * 0.95, 0.0, 1.0)
    graded = np.dstack([b_out, g_out, r_out])
    
    h, w = frame.shape[:2]
    Y, X = np.ogrid[:h, :w]
    dist = np.sqrt(((X - w / 2) / (w / 2)) ** 2 + ((Y - h / 2) / (h / 2)) ** 2)
    vig = np.clip(1.0 - 0.22 * (dist ** 2.0), 0.55, 1.0)
    graded = graded * vig[:, :, np.newaxis]
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def remove_google_earth_watermark(frame):
    h, w = frame.shape[:2]
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
    print("Generating Shot 1: Smooth Zoom-In -> Motion Freeze (3.0s-5.5s) -> Deep Zoom into Pin -> Reveal TSMC Building...")
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
    
    tmp_out = "demo-tsmc-v2/assets/video/tmp_shot1_freeze.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(tmp_out, fourcc, fps, (width, height))
    
    tsmc_graded_base = grade_tsmc_building(cv2.resize(tsmc_img, (width, height)))
    
    # Pre-extract frame 210 for clean frozen hold
    cap_earth.set(cv2.CAP_PROP_POS_FRAMES, 210)
    ret, frame_210 = cap_earth.read()
    frame_210_clean = grade_vox_cinematic(remove_google_earth_watermark(frame_210))
    
    # Target coordinate for TSMC Hsinchu on frame 210
    target_x, target_y = 350, 330
    
    for f_idx in range(total_frames):
        t = f_idx / fps
        
        # ----------------------------------------------------
        # Phase 1: Zoom from Space in to Taiwan (0.00s - 3.00s, frames 0 - 71)
        # ----------------------------------------------------
        if f_idx < 72:
            p = f_idx / 72.0
            # Smooth ease-in-out curve
            p_eased = p * p * (3.0 - 2.0 * p)
            src_fno = int(p_eased * 210)
            cap_earth.set(cv2.CAP_PROP_POS_FRAMES, src_fno)
            ret, frame = cap_earth.read()
            if not ret:
                frame = frame_210
            graded = grade_vox_cinematic(remove_google_earth_watermark(frame))
            
        # ----------------------------------------------------
        # Phase 2: DỪNG CHUYỂN ĐỘNG / FREEZE MOTION (3.00s - 5.50s, frames 72 - 131)
        # Holds steady on top-down satellite view of Taiwan/Hsinchu
        # ----------------------------------------------------
        elif f_idx < 132:
            # Subtly breathe (less than 0.5% scale) for organic alive film feel, but motion has stopped!
            hold_p = (f_idx - 72) / (132 - 72)
            subtle_scale = 1.00 + hold_p * 0.006
            M = cv2.getRotationMatrix2D((target_x, target_y), 0, subtle_scale)
            graded = cv2.warpAffine(frame_210_clean, M, (width, height), borderMode=cv2.BORDER_REFLECT)
            
        # ----------------------------------------------------
        # Phase 3: ZOOM SÂU VÀO VỊ TRÍ CHẤM / PUSH-IN ZOOM (5.50s - 6.33s, frames 132 - 151)
        # Rapidly pushes into (target_x, target_y) from 1.0x to 2.8x
        # ----------------------------------------------------
        elif f_idx < 152:
            zoom_p = (f_idx - 132) / (152 - 132)
            # Power 2 ease-in for dramatic camera rush
            zoom_p_curved = zoom_p ** 1.8
            scale = 1.006 + zoom_p_curved * 2.2 # scales up to ~3.2x
            
            M = cv2.getRotationMatrix2D((target_x, target_y), 0, scale)
            zoomed_map = cv2.warpAffine(frame_210_clean, M, (width, height), borderMode=cv2.BORDER_REFLECT)
            
            # Cross-fade to TSMC building starts halfway through the push-in (frame 142)
            if f_idx >= 142:
                dissolve_p = (f_idx - 142) / (152 - 142)
                dissolve_p = dissolve_p * dissolve_p * (3.0 - 2.0 * dissolve_p) # S-curve
                
                # TSMC building scale matches the arrival
                b_scale = 1.08 - (1.0 - dissolve_p) * 0.08
                Mb = cv2.getRotationMatrix2D((width // 2, height // 2), 0, b_scale)
                tsmc_warped = cv2.warpAffine(tsmc_graded_base, Mb, (width, height), borderMode=cv2.BORDER_REFLECT)
                graded = cv2.addWeighted(zoomed_map, 1.0 - dissolve_p, tsmc_warped, dissolve_p, 0)
            else:
                graded = zoomed_map
                
        # ----------------------------------------------------
        # Phase 4: HIỆN RA HÌNH ẢNH CÔNG TY (6.33s - 8.42s, frames 152 - 201)
        # TSMC Headquarters Building with majestic slow Ken Burns drift
        # ----------------------------------------------------
        else:
            build_p = (f_idx - 152) / (total_frames - 1 - 152)
            # Gentle architectural slow push: 1.00 -> 1.05
            scale = 1.00 + build_p * 0.05
            shift_y = int(build_p * 12)
            Mb = cv2.getRotationMatrix2D((width // 2, height // 2), 0, scale)
            Mb[1, 2] -= shift_y
            graded = cv2.warpAffine(tsmc_graded_base, Mb, (width, height), borderMode=cv2.BORDER_REFLECT)
            
            # Final 8 frames motion blur punch for cut to scene 2
            if f_idx >= 194:
                punch_p = (f_idx - 194) / 7.0
                blur_scales = [1.0, 1.0 + punch_p * 0.04, 1.0 + punch_p * 0.08]
                accum = np.zeros_like(graded, dtype=np.float32)
                for bs in blur_scales:
                    M_b = cv2.getRotationMatrix2D((width // 2, height // 2), 0, bs)
                    warped = cv2.warpAffine(graded, M_b, (width, height), borderMode=cv2.BORDER_REFLECT)
                    accum += warped.astype(np.float32)
                graded = np.clip(accum / len(blur_scales), 0, 255).astype(np.uint8)
                
        writer.write(graded)
        if f_idx % 25 == 0 or f_idx == total_frames - 1:
            print(f"Rendered frame {f_idx}/{total_frames} ({t:.2f}s)")
            
    writer.release()
    cap_earth.release()
    print("Video render complete! Encoding to final MP4 with ffmpeg...")
    
    final_mp4 = "demo-tsmc-v2/assets/video/shot1_map_veo.mp4"
    backup_mp4 = "demo-tsmc-v2/assets/video/shot1_map_veo.bak.mp4"
    if os.path.exists(final_mp4) and not os.path.exists(backup_mp4):
        os.rename(final_mp4, backup_mp4)
        
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
    print(f"[SUCCESS] Generated {final_mp4} matching user's exact camera choreography!")

if __name__ == "__main__":
    main()
