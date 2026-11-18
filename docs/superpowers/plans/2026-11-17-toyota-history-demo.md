# Toyota History Demo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render a 30-second 16:9 documentary-style Toyota history demo video.

**Architecture:** The production is asset-led: generate or source an original paper-collage visual for each historical beat, compose it into timed scenes, then render the scene sequence and a light audio bed into one MP4. A small render manifest keeps copy, timings and asset paths inspectable.

**Tech Stack:** AI image generation, FFmpeg, local image/audio assets.

**Spec:** `docs/superpowers/specs/2026-11-17-toyota-history-demo-design.md`

## Global Constraints

- Final deliverable: `output/toyota-history-demo-30s.mp4`, 1920×1080, 30 seconds.
- Use original/generated or license-safe media only; do not replicate Toyota trademarks or proprietary documents.
- Apply paper-collage documentary treatment, palette, and minimal one-idea-per-scene rule from the spec.

## Review Focus

- Verify that claims about company milestones have a cited source in the production notes.
- Verify captions remain readable against every background, especially yellow-on-paper scenes.
- Verify no scene overuses the yellow highlight color.
- Verify source artwork does not contain a Toyota logo or a photorealistic trademark badge.
- Verify the first and final frame communicate the hook and conclusion without voiceover.

---

### Task 1: Create the production manifest and verified script

**Files:**
- Create: `toyota-demo/manifest.json`
- Create: `toyota-demo/production-notes.md`

**Interfaces:**
- Produces: five scene IDs, start/end seconds, on-screen copy, asset filename, and motion direction for composition.

- [ ] **Step 1: Write the scene table**

Define exactly five entries with time boundaries `0–5`, `5–11`, `11–19`, `19–26`, and `26–30` and the copy from the approved spec.

- [ ] **Step 2: Verify historical milestones**

Record the primary or authoritative source URL beside each date/claim in `production-notes.md`.

- [ ] **Step 3: Check copy and duration allocation**

Confirm scene end times total exactly `30.0` seconds and no caption exceeds two lines at 1920×1080.

### Task 2: Create scene artwork

**Files:**
- Create: `toyota-demo/assets/scene-01.png`
- Create: `toyota-demo/assets/scene-02.png`
- Create: `toyota-demo/assets/scene-03.png`
- Create: `toyota-demo/assets/scene-04.png`
- Create: `toyota-demo/assets/scene-05.png`

**Interfaces:**
- Consumes: `toyota-demo/manifest.json` scene text and visual directions.
- Produces: five original 1920×1080 PNG scenes ready for motion composition.

- [ ] **Step 1: Generate artwork for each specified scene**

Generate the paper-collage treatment with cream paper, charcoal, muted red and mustard accents; exclude logos and real people.

- [ ] **Step 2: Inspect artwork at full frame**

Confirm required text has safe margins, the visual focal point is not covered by captions, and the yellow accent appears only on the core term.

### Task 3: Compose and render the video

**Files:**
- Create: `toyota-demo/render.ps1`
- Create: `output/toyota-history-demo-30s.mp4`

**Interfaces:**
- Consumes: manifest and five PNG scene assets.
- Produces: H.264/AAC MP4 with exactly 30 seconds of scene sequence, gentle pan/zoom, fades, and a legal audio bed.

- [ ] **Step 1: Render a test sequence**

Implement `render.ps1` to use FFmpeg with each scene duration from `manifest.json`, `zoompan` or equivalent gentle motion, and short cross-fades.

- [ ] **Step 2: Render the final MP4**

Run: `powershell -ExecutionPolicy Bypass -File toyota-demo/render.ps1`

Expected: `output/toyota-history-demo-30s.mp4` exists.

- [ ] **Step 3: Validate technical constraints**

Run: `ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of default=noprint_wrappers=1 output/toyota-history-demo-30s.mp4`

Expected: duration is `29.9–30.1`, video is 1920×1080 and H.264, audio stream exists.

### Task 4: Visual quality review

**Files:**
- Modify: `toyota-demo/production-notes.md`

**Interfaces:**
- Consumes: rendered MP4.
- Produces: documented review result and any necessary final correction.

- [ ] **Step 1: Extract representative frames at 0, 5, 11, 19, and 26 seconds**

Run FFmpeg frame extraction and inspect each frame against the spec’s readability and palette constraints.

- [ ] **Step 2: Correct any failing scene and re-render**

If any scene has clipping, unreadable type, unintended black frame, or inconsistent visual language, correct its source asset and repeat Task 3 validation.

- [ ] **Step 3: Record final evidence**

Add duration, checked timestamps, and any deviations to `toyota-demo/production-notes.md`.
