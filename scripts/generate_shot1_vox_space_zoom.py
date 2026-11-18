import cv2
import numpy as np
import os
import subprocess

def create_celestial_space_bg(width=1920, height=1080):
    """Creates a warm vintage celestial parchment background for outer space."""
    # Warm dark slate/bronze gradient
    Y, X = np.ogrid[:height, :width]
    dist_center = np.sqrt(((X - width/2) / (width/2))**2 + ((Y - height/2) / (height/2))**2)
    
    # Base dark bronze/slate
    # Center: [28, 24, 20], Edges: [18, 15, 12] (BGR)
    b = (28 - 10 * dist_center).clip(12, 30)
    g = (34 - 15 * dist_center).clip(15, 36)
    r = (40 - 18 * dist_center).clip(18, 42)
    bg = np.dstack([b, g, r]).astype(np.float32)
    
    # Add subtle celestial graticule circles (vintage astronomical map)
    cx, cy = width // 2, height // 2
    for radius in [180, 320, 480, 640, 800]:
        circle_mask = np.abs(np.sqrt((X - cx)**2 + (Y - cy)**2) - radius) < 1.0
        bg[circle_mask] += np.array([15.0, 25.0, 35.0]) # warm gold line
        
    # Subtle celestial star specks
    np.random.seed(42)
    num_stars = 220
    star_x = np.random.randint(0, width, num_stars)
    star_y = np.random.randint(0, height, num_stars)
    star_bright = np.random.uniform(20, 65, num_stars)
    for sx, sy, sb in zip(star_x, star_y, star_bright):
        bg[sy, sx] = np.clip(bg[sy, sx] + np.array([sb*0.6, sb*0.85, sb*1.0]), 0, 255)
        
    return bg

def apply_vox_gold_palette(frame, bg_space=None, space_blend=0.0):
    """
    Grades frame into warm Vox archival gold palette:
    Shadows: #181410 (antique dark ink)
    Midtones: #C89E48 (rich vintage gold / amber)
    Highlights: #F4EBD9 (aged cream parchment paper)
    """
    im_f = frame.astype(np.float32) / 255.0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    
    # 3-stop warm vintage gold gradient mapping
    shadow_col = np.array([16, 20, 24], dtype=np.float32) / 255.0    # dark warm bronze BGR
    mid_col    = np.array([72, 158, 200], dtype=np.float32) / 255.0  # rich gold BGR
    high_col   = np.array([217, 235, 244], dtype=np.float32) / 255.0 # warm parchment cream BGR
    
    graded = np.zeros_like(im_f)
    for c in range(3):
        low = shadow_col[c] * (1.0 - gray * 2.0) + mid_col[c] * (gray * 2.0)
        high = mid_col[c] * (2.0 - gray * 2.0) + high_col[c] * (gray * 2.0 - 1.0)
        graded[:, :, c] = np.where(gray < 0.5, low, high)
        
    # Blend 80% gold grade + 20% desaturated realism
    desat = np.repeat(gray[:, :, np.newaxis], 3, axis=2)
    out = 0.82 * graded + 0.18 * desat
    
    # If in space phase, composite onto the warm celestial space background instead of black void
    if space_blend > 0.001 and bg_space is not None:
        # Detect black space in source frame (Earth globe is bright, space is near 0)
        # Use soft threshold
        earth_mask = np.clip((gray - 0.04) * 8.0, 0.0, 1.0)
        earth_mask = cv2.GaussianBlur(earth_mask, (7, 7), 0)[:, :, np.newaxis]
        
        # Golden atmospheric limb glow around Earth
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
        dilated = cv2.dilate(earth_mask[:, :, 0], kernel, iterations=2)
        limb = np.clip(dilated - earth_mask[:, :, 0], 0.0, 1.0)[:, :, np.newaxis]
        limb_glow = limb * np.array([30/255.0, 110/255.0, 180/255.0], dtype=np.float32) # warm amber glow
        
        bg_norm = bg_space / 255.0
        composited = out * earth_mask + bg_norm * (1.0 - earth_mask) + limb_glow
        out = (1.0 - space_blend) * out + space_blend * composited
        
    return np.clip(out * 255.0, 0, 255).astype(np.uint8)

def add_motion_blur_zoom(img, zoom_center=(960, 540), strength=0.15):
    """Creates a radial whip zoom motion blur toward zoom_center."""
    h, w = img.shape[:2]
    cx, cy = zoom_center
    
    # Average of several zoomed scales
    scales = [1.0, 1.0 + strength * 0.25, 1.0 + strength * 0.5, 1.0 + strength * 0.75, 1.0 + strength]
    blurred = np.zeros_like(img, dtype=np.float32)
    
    for s in scales:
        M = cv2.getRotationMatrix2D((cx, cy), 0, s)
        warped = cv2.warpAffine(img, M, (w, h), borderMode=cv2.BORDER_REFLECT)
        blurred += warped.astype(np.float32)
        
    blurred /= len(scales)
    return np.clip(blurred, 0, 255).astype(np.uint8)

def main():
    print("Generating Shot 01: Outer Space -> Spinning Earth -> Hsinchu -> Silicon Wafer Morph...")
    
    src_video = "assets_tsmc/google_earth_taoyuan.mp4.mkv"
    wafer_img_path = "demo-tsmc-v2/assets/images/silicon_wafer_vintage.jpg"
    
    cap = cv2.VideoCapture(src_video)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open {src_video}")
        
    wafer_raw = cv2.imread(wafer_img_path)
    if wafer_raw is None:
        raise RuntimeError(f"Could not read {wafer_img_path}")
        
    # Resize and grade wafer image to 1920x1080
    wafer_full = cv2.resize(wafer_raw, (1920, 1080), interpolation=cv2.INTER_CUBIC)
    wafer_graded = apply_vox_gold_palette(wafer_full)
    
    total_out_frames = 202 # 8.42s at 24fps
    out_fps = 24.0
    width, height = 1920, 1080
    
    celestial_bg = create_celestial_space_bg(width, height)
    
    # Temporary raw AVI/MP4 writer
    tmp_out = "demo-tsmc-v2/assets/video/tmp_shot1_zoom.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(tmp_out, fourcc, out_fps, (width, height))
    
    src_total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Source frames: {src_total}, Target frames: {total_out_frames}")
    
    # Keyframe timing curve for the 202 frames:
    # Phase 1: Frames 0..58 (0.00s..2.42s): Orbit in outer space, Earth globe rotating (src frames 0 -> 70)
    # Phase 2: Frames 58..125 (2.42s..5.21s): Stratospheric plunge to Taiwan Strait (src frames 70 -> 240)
    # Phase 3: Frames 125..172 (5.21s..7.17s): Precision lock onto Hsinchu (src frames 240 -> 440)
    # Phase 4: Frames 172..201 (7.17s..8.42s): Extreme hyper-zoom into Hsinchu Fab & morph into Silicon Wafer Die
    
    for f_idx in range(total_out_frames):
        t = f_idx / out_fps
        progress = f_idx / (total_out_frames - 1)
        
        # Calculate source frame index using non-linear easing
        if f_idx < 58: # Space orbit
            p = f_idx / 58.0
            src_fno = int(0 + p * 70)
            space_blend = max(0.0, 1.0 - p * 0.4)
        elif f_idx < 125: # Atmospheric plunge
            p = (f_idx - 58) / (125 - 58)
            # ease-in curve
            p_eased = p ** 1.3
            src_fno = int(70 + p_eased * (240 - 70))
            space_blend = max(0.0, 0.6 * (1.0 - p))
        elif f_idx < 172: # Hsinchu approach
            p = (f_idx - 125) / (172 - 125)
            src_fno = int(240 + p * (440 - 240))
            space_blend = 0.0
        else: # Final hyper-zoom & wafer blend
            src_fno = min(445, 440 + int((f_idx - 172) * 0.5))
            space_blend = 0.0
            
        src_fno = min(src_fno, src_total - 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, src_fno)
        ret, frame = cap.read()
        if not ret:
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
        # Ensure 1920x1080
        if frame.shape[0] != height or frame.shape[1] != width:
            frame = cv2.resize(frame, (width, height))
            
        # Color grade to Vox vintage gold
        graded = apply_vox_gold_palette(frame, bg_space=celestial_bg, space_blend=space_blend)
        
        # Phase 4: Extreme hyper-zoom and morph into silicon wafer die
        if f_idx >= 168:
            morph_p = (f_idx - 168) / (total_out_frames - 1 - 168) # 0.0 to 1.0
            
            # Zoom center at Hsinchu target area (approx x=980, y=520)
            target_cx, target_cy = 980, 520
            
            # Exponential zoom on the landscape
            scale = 1.0 + (morph_p ** 1.8) * 3.5
            M = cv2.getRotationMatrix2D((target_cx, target_cy), 0, scale)
            zoomed_land = cv2.warpAffine(graded, M, (width, height), borderMode=cv2.BORDER_REFLECT)
            
            # Zoom on the wafer die from scale 0.5 to 1.8
            wafer_scale = 0.6 + (morph_p ** 1.5) * 1.4
            Mw = cv2.getRotationMatrix2D((width//2, height//2), 0, wafer_scale)
            zoomed_wafer = cv2.warpAffine(wafer_graded, Mw, (width, height), borderMode=cv2.BORDER_REFLECT)
            
            # Cross-fade blend
            blend_alpha = np.clip((morph_p - 0.2) / 0.8, 0.0, 1.0)
            # Add dynamic radial motion blur
            combined = cv2.addWeighted(zoomed_land, 1.0 - blend_alpha, zoomed_wafer, blend_alpha, 0)
            graded = add_motion_blur_zoom(combined, (width//2, height//2), strength=morph_p * 0.35)
            
        # ================= GRAPHIC OVERLAYS & TELEMETRY =================
        # 1. Outer Space Phase (0.0s - 2.5s)
        if f_idx < 62:
            alt_km = int(35786 - (f_idx / 62.0) * (35786 - 12000))
            # Retro coordinate HUD box
            cv2.putText(graded, "ORBITAL TELEMETRY // ASIA-PACIFIC SECTOR", (80, 140), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (72, 158, 200), 2, cv2.LINE_AA)
            cv2.putText(graded, f"ALTITUDE: {alt_km:,} KM  |  ORBIT: GEO-STATIONARY 120.5E", (80, 175), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.65, (200, 220, 235), 1, cv2.LINE_AA)
            # Rotating reticle in corner
            cv2.circle(graded, (1820, 120), 28, (72, 158, 200), 2)
            cv2.line(graded, (1820, 85), (1820, 155), (72, 158, 200), 1)
            cv2.line(graded, (1785, 120), (1855, 120), (72, 158, 200), 1)
            
        # 2. Taiwan Strait Phase (2.5s - 5.5s, frames 60 to 135)
        if 58 <= f_idx < 140:
            ts_p = (f_idx - 58) / (140 - 58)
            # Draw red dashed median line across Taiwan Strait
            start_pt = (780, 260)
            end_pt = (1080, 820)
            line_len = int(np.sqrt((end_pt[0]-start_pt[0])**2 + (end_pt[1]-start_pt[1])**2))
            
            # Animate line drawing
            cur_dist = min(line_len, int(ts_p * line_len * 1.4))
            unit_x = (end_pt[0] - start_pt[0]) / line_len
            unit_y = (end_pt[1] - start_pt[1]) / line_len
            
            # Draw dashes
            dash_size = 18
            for d in range(0, cur_dist, dash_size * 2):
                p1 = (int(start_pt[0] + d * unit_x), int(start_pt[1] + d * unit_y))
                p2 = (int(start_pt[0] + min(cur_dist, d + dash_size) * unit_x), 
                      int(start_pt[1] + min(cur_dist, d + dash_size) * unit_y))
                cv2.line(graded, p1, p2, (38, 38, 192), 3, cv2.LINE_AA) # Stamp red in BGR
                
            # Strait callout text
            if f_idx > 80:
                cv2.rectangle(graded, (760, 480), (1160, 530), (20, 18, 16), -1)
                cv2.rectangle(graded, (760, 480), (1160, 530), (72, 158, 200), 2)
                cv2.putText(graded, "TAIWAN STRAIT // 台湾海峡 160KM", (775, 514),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (217, 235, 244), 2, cv2.LINE_AA)
                            
        # 3. Precision Lock on Hsinchu (5.2s - 7.5s, frames 125 to 180)
        if 125 <= f_idx < 185:
            # Target crosshair coordinates (moving slightly with camera zoom)
            target_x = 980
            target_y = 520
            
            # Animated reticle clamp
            reticle_size = max(42, int(85 - ((f_idx - 125) / 55.0) * 43))
            
            # Red targeting bracket corners
            c_red = (38, 38, 200) # BGR red
            c_gold = (72, 158, 200)
            
            # Top-left corner
            cv2.line(graded, (target_x - reticle_size, target_y - reticle_size), 
                             (target_x - reticle_size + 24, target_y - reticle_size), c_red, 3)
            cv2.line(graded, (target_x - reticle_size, target_y - reticle_size), 
                             (target_x - reticle_size, target_y - reticle_size + 24), c_red, 3)
            # Top-right corner
            cv2.line(graded, (target_x + reticle_size, target_y - reticle_size), 
                             (target_x + reticle_size - 24, target_y - reticle_size), c_red, 3)
            cv2.line(graded, (target_x + reticle_size, target_y - reticle_size), 
                             (target_x + reticle_size, target_y - reticle_size + 24), c_red, 3)
            # Bottom-left corner
            cv2.line(graded, (target_x - reticle_size, target_y + reticle_size), 
                             (target_x - reticle_size + 24, target_y + reticle_size), c_red, 3)
            cv2.line(graded, (target_x - reticle_size, target_y + reticle_size), 
                             (target_x - reticle_size, target_y + reticle_size - 24), c_red, 3)
            # Bottom-right corner
            cv2.line(graded, (target_x + reticle_size, target_y + reticle_size), 
                             (target_x + reticle_size - 24, target_y + reticle_size), c_red, 3)
            cv2.line(graded, (target_x + reticle_size, target_y + reticle_size), 
                             (target_x + reticle_size, target_y + reticle_size - 24), c_red, 3)
            # Center reticle dot
            cv2.circle(graded, (target_x, target_y), 4, c_red, -1)
            
            # Callout card next to reticle
            card_x1, card_y1 = target_x + reticle_size + 20, target_y - 45
            card_x2, card_y2 = card_x1 + 430, card_y1 + 95
            cv2.rectangle(graded, (card_x1, card_y1), (card_x2, card_y2), (18, 16, 14), -1)
            cv2.rectangle(graded, (card_x1, card_y1), (card_x2, card_y2), c_red, 2)
            cv2.putText(graded, "TARGET: HSINCHU SCIENCE PARK", (card_x1 + 16, card_y1 + 28),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, c_gold, 2, cv2.LINE_AA)
            cv2.putText(graded, "LAT 24.7738 N  |  LON 120.9983 E", (card_x1 + 16, card_y1 + 54),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (217, 235, 244), 1, cv2.LINE_AA)
            cv2.putText(graded, "TSMC FAB 12 / 20 CLUSTER [90% OF ADVANCED DIE]", (card_x1 + 16, card_y1 + 78),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.48, (60, 200, 240), 1, cv2.LINE_AA)
                        
        # 4. Final Hyper-Dive Speed Streaks (7.4s - 8.42s, frames 178 to 201)
        if f_idx >= 178:
            streak_p = (f_idx - 178) / (201 - 178)
            # Add dynamic radial light ring
            ring_r = int(streak_p * 600)
            cv2.circle(graded, (width//2, height//2), ring_r, (72, 158, 200), int(2 + streak_p * 6))
            # Text flash in final frames
            if f_idx >= 190:
                cv2.putText(graded, "ENTERING 3NM / 2NM CLEANROOM FAB...", (width//2 - 280, height//2 + 180),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (217, 235, 244), 2, cv2.LINE_AA)
                            
        writer.write(graded)
        if f_idx % 20 == 0 or f_idx == total_out_frames - 1:
            print(f"Processed frame {f_idx}/{total_out_frames} ({t:.2f}s)")
            
    writer.release()
    cap.release()
    print("Raw video generation complete. Encoding H.264 MP4 with FFmpeg...")
    
    final_mp4 = "demo-tsmc-v2/assets/video/shot1_map_veo.mp4"
    # Overwrite final_mp4 with high quality web-optimized H.264
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
    print(f"SUCCESS: Created {final_mp4}")

if __name__ == "__main__":
    main()
