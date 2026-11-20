---
name: vox-doc-video-production
description: Use when creating, scripting, animating, or producing YouTube historical documentary, tech investigation, or business drama videos in Vox × MagnatesMedia style using HyperFrames or HTML/CSS/GSAP.
---

# Vox × MagnatesMedia Video Production Guide

## Overview

This skill defines the complete production pipeline for long-form (18–20 minute) investigative historical, tech, and business documentary videos built on **HyperFrames** (HTML5 + CSS3 + GSAP).

---

## 1. Timeline & Duration Architecture (18–20 Minute Standard)

A common pitfall is producing a rapid 9–10 minute video when the target was 18–20 minutes because voiceover sentences were packed without cinematic breathing room.

### The Pacing Formula
For an **18 to 20 minute video** across **~30 to 32 scenes**:
- **Average Scene Duration:** `35.0s – 40.0s` (31 scenes × ~36.5s = **~18m45s**).
- **Scene Breakdown Anatomy:**
  1. **Pre-roll Beat (1.2s – 2.0s):** Initial silence / visual reveal / subtle SFX before the narrator speaks.
  2. **Voiceover Narration (20.0s – 28.0s):** Authoritative narration explaining the drama, context, and conflict (~130–160 Japanese characters / ~45–60 Vietnamese words).
  3. **Post-roll Hold / Dramatic Beat (8.5s – 12.5s):** Crucial hold time after speech ends to let the infographic, action stamp, or document soak in while BGM swells.

### Japanese Script Density Guidelines (ja-JP-KeitaNeural)
- **Speaking Rate:** ~280–300 mora/characters per minute (use `rate="-4%"` for weighty documentary cadence).
- **Total Characters for 18–20 mins:** `~4,200 – 4,800 characters` across 30 scenes.

---

## 2. Audio Engineering & Loudness Standards

Voiceover must stand out with clarity, while background music creates an atmospheric bed without competing with dialogue.

| Track Type | Peak Level | Mean (RMS) Level | Relative Balance | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Voiceover (VO)** | `-2.0 dB` to `-3.0 dB` | `~ -20.0 dB` | **Primary Anchor (0 dB)** | Full-bodied, crisp, broadcast standard. |
| **BGM Master** | `-18.0 dB` to `-19.0 dB` | `~ -34.0 dB` | **-13 dB to -14 dB below VO** | Atmospheric bed, never masks speech. |
| **SFX (Foley/Stamps)** | `-11.0 dB` to `-14.0 dB` | `~ -24.0 dB` to `-28.0 dB` | Attenuate by 30% | Punchy without ear-piercing harshness. |

### Audio Processing with FFmpeg
```bash
# Normalize VO file to target peak (-2.5 dB)
ffmpeg -y -i input_vo.wav -af "volume=-2.5dB" -c:a libmp3lame -b:a 192k scene_01.mp3

# Attenuate BGM to stay under dialogue (-18.2 dB peak)
ffmpeg -y -i raw_bgm.mp3 -af "volume=-8.5dB" -c:a libmp3lame -b:a 192k cinematic_score.mp3
```

---

## 3. HyperFrames HTML & Timeline Structure

### Root Composition Declaration
```html
<div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="1126.62">
```

### Scene Stage Element Pattern
Each scene must be a direct top-level stage in the timeline:
```html
<!-- SCENE 10: FOUNDRY SPLIT (327.80s - 368.10s, dur 40.30s) -->
<div class="act2-stage clip" id="scene10-stage" data-start="327.80" data-duration="40.30" data-track-index="1" data-layout-allow-overflow>
  <div class="act2-top-bar">
    <div class="act2-top-kicker"><span class="vox-pill-badge">ACT II</span> FOUNDRY REVOLUTION</div>
    <div class="act2-top-time">1987 // HSINCHU, TAIWAN</div>
  </div>
  
  <!-- Visual Content Container -->
  <div class="s10-container">
    ...
  </div>

  <!-- Lower-Third Telop -->
  <div class="act2-telop-card" id="s10-telop">
    <div class="act2-telop-badge gold">FOUNDRY REVOLUTION</div>
    <h2 class="act2-telop-title">狂気のアイデア</h2>
    <p class="act2-telop-sub">「自社製品を作らない」専業受託製造 (Pure-play Foundry)</p>
  </div>
</div>

<!-- Audio Clips: Separate Track Indices to Avoid Collision -->
<audio class="clip" id="vo-10" data-start="329.80" data-duration="25.80" data-track-index="3" src="assets/audio/scene_10.mp3"></audio>
<audio class="clip" id="sfx-10-marker" data-start="331.00" data-duration="0.40" data-track-index="4" src="assets/sfx/marker_wipe.wav"></audio>
```

### Continuous BGM Looping Architecture
Instead of one overstretched file that cuts off, loop the master score in discrete segments:
```html
<!-- Track Index 25: Master Soundtrack Chain -->
<audio class="clip" id="bgm-loop-00" data-start="0.00" data-duration="96.88" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
<audio class="clip" id="bgm-loop-01" data-start="96.88" data-duration="96.88" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
<audio class="clip" id="bgm-loop-02" data-start="193.76" data-duration="96.88" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
```

---

## 4. GSAP Choreography Best Practices

```javascript
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });

// Choreography template for each scene:
// 1. Stage Fade In at start
tl.to("#scene10-stage", { opacity: 1, duration: 0.5, ease: "power2.out" }, 327.80);

// 2. Visual Content Entrance
tl.fromTo("#scene10-stage .s10-left-fabless", { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }, 328.30);
tl.fromTo("#scene10-stage .act2-telop-card", { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }, 328.40);

// 3. Dramatic Action Stamp Slams Down
tl.fromTo("#s10-stamp", { scale: 2.5, opacity: 0 }, { scale: 1.0, opacity: 1, duration: 0.35, ease: "back.out(2.0)" }, 329.50);

// 4. Yellow Highlighter Sweeps Key Metric
tl.fromTo("#scene10-stage .vox-highlight-box", { scaleX: 0 }, { scaleX: 1, duration: 0.4, ease: "power2.out" }, 330.50);

// 5. Stage Clean Fade Out before next scene
tl.to("#scene10-stage", { opacity: 0, duration: 0.6, ease: "power2.in" }, 367.50);

window.__timelines["main"] = tl;
tl.seek(0);
```

---

## 5. Pre-Render Validation Checklist

Before presenting or rendering:
1. `npx hyperframes lint <project-dir>`: Must output **0 error(s)**.
2. Verify no overlapping clips on the same track index (`Audible clips overlap on Studio track X`).
3. Verify all `<audio>` files exist on disk and have non-zero size.
4. Check that BGM volume is at `-18.2 dB` peak, never masking narrator speech.
