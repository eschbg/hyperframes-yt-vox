import json
import os

total_duration = 96.888

html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>TSMC // The Semiconductor Empire (Vintage Archival Documentary)</title>
    <!-- Google Fonts: Authentic Archival Documentary Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700;800&family=Noto+Sans+JP:wght@400;600;700;900&family=Noto+Serif+JP:wght@600;700;900&family=Oswald:wght@500;600;700;900&display=swap" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

    <style>
      :root {{
        /* Unified Vintage Archival Palette */
        --desk-dark: #141210;
        --desk-mid: #1c1814;
        --desk-light: #25201a;
        --paper-cream: #f5f0e6;
        --paper-aged: #e8dfcd;
        --paper-shadow: rgba(0, 0, 0, 0.65);
        --ink-black: #1a1a1a;
        --typewriter-gray: #3a3835;
        --stamp-red: #b71c1c;
        --stamp-red-soft: rgba(183, 28, 28, 0.15);
        --highlight-gold: #e5bb54;
        --highlight-gold-soft: rgba(229, 187, 84, 0.35);
        --tech-blueprint: #1e2c38;
        --blueprint-cyan: #5dade2;
        --tape-color: rgba(245, 235, 210, 0.55);
      }}

      * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }}

      body {{
        background: #000;
        color: var(--paper-cream);
        font-family: 'Noto Serif JP', serif;
        overflow: hidden;
        -webkit-font-smoothing: antialiased;
      }}

      /* ================= UNIFIED ARCHIVAL DESK CANVAS ================= */
      #root {{
        position: relative;
        width: 1920px;
        height: 1080px;
        /* Unified continuous background across ALL scenes: Deep Antique Mahogany / Archival Leather Desk */
        background: radial-gradient(ellipse at 50% 45%, var(--desk-mid) 0%, var(--desk-dark) 70%, #0a0908 100%);
        overflow: hidden;
      }}

      /* Persistent Vintage Film Grain & Dust Scratches */
      .persistent-archival-grain {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.055;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 80;
      }}

      .persistent-vignette {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(ellipse at center, transparent 45%, rgba(10, 9, 8, 0.85) 100%);
        pointer-events: none;
        z-index: 85;
      }}

      /* ================= TOP ARCHIVAL DOSSIER BANNER ================= */
      .archival-top-bar {{
        position: absolute;
        top: 28px;
        left: 56px;
        right: 56px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 90;
        border-bottom: 1px solid rgba(229, 187, 84, 0.25);
        padding-bottom: 12px;
      }}

      .dossier-id-tag {{
        display: flex;
        align-items: center;
        gap: 14px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        letter-spacing: 2px;
        color: var(--highlight-gold);
      }}

      .dossier-badge {{
        background: rgba(229, 187, 84, 0.15);
        border: 1px solid var(--highlight-gold);
        padding: 4px 10px;
        border-radius: 2px;
        font-weight: 700;
        font-size: 11px;
      }}

      .dossier-case-title {{
        font-family: 'Courier Prime', monospace;
        font-size: 15px;
        letter-spacing: 3px;
        color: #dcd6c8;
        text-transform: uppercase;
      }}

      .dossier-status {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        letter-spacing: 2px;
        color: #a39b8c;
      }}

      /* ================= VINTAGE DOCUMENTARY SUBTITLES ================= */
      .vintage-sub-wrapper {{
        position: absolute;
        bottom: 26px;
        left: 50%;
        transform: translateX(-50%);
        width: 1720px;
        min-height: 82px;
        background: rgba(18, 16, 14, 0.94);
        border: 1px solid rgba(229, 187, 84, 0.25);
        border-left: 6px solid var(--highlight-gold);
        border-radius: 3px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px 36px;
        z-index: 100;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.85);
      }}

      .vintage-sub-text {{
        font-family: 'Noto Serif JP', serif;
        font-size: 30px;
        font-weight: 700;
        color: var(--paper-cream);
        line-height: 1.45;
        text-align: center;
        letter-spacing: 1.5px;
      }}

      .sub-gold {{
        color: var(--highlight-gold);
        text-shadow: 0 0 12px rgba(229, 187, 84, 0.4);
      }}

      .sub-red {{
        color: #e57373;
      }}

      .sub-cyan {{
        color: #80deea;
      }}

      /* ================= SHARED VINTAGE MEDIA STYLES ================= */
      /* Polaroid & Archival Photo Prints */
      .archival-polaroid {{
        background: var(--paper-cream);
        padding: 14px 14px 24px 14px;
        border-radius: 2px;
        box-shadow: 0 18px 45px var(--paper-shadow);
        border: 1px solid rgba(0, 0, 0, 0.2);
        position: relative;
        display: flex;
        flex-direction: column;
      }}

      .polaroid-img-frame {{
        width: 100%;
        overflow: hidden;
        border: 1px solid rgba(0, 0, 0, 0.15);
      }}

      .polaroid-img-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: sepia(0.22) contrast(1.08) brightness(0.95);
      }}

      .polaroid-caption {{
        margin-top: 14px;
        font-family: 'Courier Prime', monospace;
        font-size: 14px;
        color: var(--typewriter-gray);
        text-align: center;
        letter-spacing: 1.5px;
      }}

      /* Translucent Scotch / Masking Tape */
      .scotch-tape-top {{
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%) rotate(-2deg);
        width: 110px;
        height: 28px;
        background: var(--tape-color);
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(2px);
        border-left: 1px dashed rgba(0, 0, 0, 0.15);
        border-right: 1px dashed rgba(0, 0, 0, 0.15);
        z-index: 15;
      }}

      /* Archival Rubber Stamp */
      .vintage-rubber-stamp {{
        border: 3px solid var(--stamp-red);
        color: var(--stamp-red);
        font-family: 'Oswald', sans-serif;
        font-weight: 900;
        letter-spacing: 3px;
        padding: 6px 18px;
        text-transform: uppercase;
        border-radius: 3px;
        transform: rotate(-10deg);
        box-shadow: 0 4px 15px rgba(183, 28, 28, 0.25);
        background: var(--stamp-red-soft);
      }}

      /* Yellow Highlighter Marker Sweep */
      .highlighter-marker {{
        background: linear-gradient(104deg, rgba(229,187,84,0) 0.9%, rgba(229,187,84,0.65) 2.4%, rgba(229,187,84,0.55) 5.8%, rgba(229,187,84,0.65) 93%, rgba(229,187,84,0.45) 96%, rgba(229,187,84,0) 98%);
        padding: 2px 8px;
        border-radius: 2px;
        color: #1a1a1a;
      }}

      /* ================= SCENE 01: VEO 3 VIDEO LAYER (0.00s - 8.42s) ================= */
      .scene01-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
      }}

      .shot1-video-player {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: sepia(0.25) contrast(1.15) brightness(0.9);
      }}

      .shot1-overlay-dossier {{
        position: absolute;
        top: 90px;
        left: 80px;
        right: 80px;
        bottom: 120px;
        pointer-events: none;
        z-index: 20;
      }}

      .shot1-target-card {{
        position: absolute;
        top: 80px;
        right: 40px;
        background: rgba(18, 16, 14, 0.92);
        border: 1px solid var(--highlight-gold);
        border-left: 5px solid var(--stamp-red);
        padding: 16px 24px;
        border-radius: 3px;
        min-width: 420px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.85);
      }}

      .target-card-kicker {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 700;
        color: #e57373;
        letter-spacing: 2px;
      }}

      .target-card-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 26px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
        margin-top: 4px;
      }}

      .target-card-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 15px;
        color: #c9c2b5;
        margin-top: 6px;
        line-height: 1.45;
      }}

      /* ================= SCENE 02: SUPPLY CHAIN DISRUPTION POLAROIDS (8.42s - 23.57s) ================= */
      .scene02-stage {{
        position: absolute;
        top: 90px;
        left: 80px;
        right: 80px;
        bottom: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .scene02-desk-grid {{
        display: flex;
        gap: 45px;
        width: 1720px;
        justify-content: space-between;
      }}

      .scene02-card {{
        flex: 1;
        background: var(--paper-cream);
        border-radius: 3px;
        padding: 20px 20px 24px 20px;
        box-shadow: 0 20px 50px var(--paper-shadow);
        border: 1px solid rgba(0, 0, 0, 0.2);
        position: relative;
        display: flex;
        flex-direction: column;
      }}

      .scene02-photo-wrap {{
        width: 100%;
        height: 380px;
        overflow: hidden;
        border: 1px solid rgba(0, 0, 0, 0.15);
      }}

      .scene02-photo-wrap img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(0.85) sepia(0.25) contrast(1.1);
      }}

      .scene02-card-body {{
        margin-top: 18px;
      }}

      .scene02-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 700;
        color: #8c8273;
        letter-spacing: 1.5px;
      }}

      .scene02-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: var(--ink-black);
        letter-spacing: 1px;
        margin-top: 4px;
      }}

      .scene02-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 15px;
        color: #4a453e;
        line-height: 1.45;
        margin-top: 8px;
      }}

      .card-stamp-overlay {{
        position: absolute;
        top: 30px;
        right: 25px;
        z-index: 20;
      }}

      .scene02-ticker-tag {{
        margin-top: 32px;
        background: rgba(18, 16, 14, 0.95);
        border: 1px solid var(--highlight-gold);
        border-radius: 4px;
        padding: 12px 36px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      }}

      .ticker-tag-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        color: var(--highlight-gold);
        letter-spacing: 2px;
      }}

      .ticker-tag-val {{
        font-family: 'Oswald', sans-serif;
        font-size: 26px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
      }}

      /* ================= SCENE 03: TSMC DOSSIER & 90% BLUEPRINT (23.57s - 39.58s) ================= */
      .scene03-stage {{
        position: absolute;
        top: 90px;
        left: 80px;
        right: 80px;
        bottom: 120px;
        display: flex;
        gap: 50px;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .scene03-folder {{
        flex: 1.1;
        height: 720px;
        background: #182330;
        border: 2px solid rgba(93, 173, 226, 0.4);
        border-radius: 4px;
        padding: 36px;
        box-shadow: 0 25px 60px var(--paper-shadow);
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }}

      .blueprint-grid-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.12;
        background-size: 25px 25px;
        background-image: linear-gradient(to right, #5dade2 1px, transparent 1px), linear-gradient(to bottom, #5dade2 1px, transparent 1px);
        pointer-events: none;
      }}

      .blueprint-donut-wrap {{
        position: relative;
        width: 280px;
        height: 280px;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .blueprint-donut-text {{
        position: absolute;
        text-align: center;
      }}

      .blueprint-num {{
        font-family: 'Oswald', sans-serif;
        font-size: 80px;
        font-weight: 900;
        color: var(--highlight-gold);
        line-height: 1;
        text-shadow: 0 0 25px rgba(229, 187, 84, 0.45);
      }}

      .blueprint-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        color: var(--paper-cream);
        letter-spacing: 2.5px;
        margin-top: 6px;
      }}

      .blueprint-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
        margin-top: 24px;
        text-align: center;
      }}

      .blueprint-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: #aed6f1;
        margin-top: 8px;
        text-align: center;
        line-height: 1.5;
      }}

      .scene03-dossier-sheet {{
        flex: 1.25;
        height: 720px;
        background: var(--paper-cream);
        border: 1px solid rgba(0, 0, 0, 0.2);
        border-radius: 3px;
        padding: 36px 40px;
        box-shadow: 0 25px 60px var(--paper-shadow);
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }}

      .sheet-header-meta {{
        border-bottom: 2px solid #2d3748;
        padding-bottom: 12px;
        display: flex;
        justify-content: space-between;
        align-items: flex-end;
      }}

      .sheet-dossier-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 900;
        color: var(--ink-black);
        letter-spacing: 1.5px;
      }}

      .sheet-file-code {{
        font-family: 'Courier Prime', monospace;
        font-size: 13px;
        color: #64748b;
      }}

      .sheet-bars-container {{
        display: flex;
        flex-direction: column;
        gap: 22px;
        margin: 24px 0;
      }}

      .sheet-bar-item {{
        background: #ebe5d8;
        border-left: 6px solid #2d3748;
        padding: 14px 20px;
        border-radius: 2px;
      }}

      .sheet-bar-head {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
      }}

      .sheet-firm-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 20px;
        font-weight: 700;
        color: var(--ink-black);
      }}

      .sheet-firm-val {{
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 900;
        color: var(--ink-black);
      }}

      .sheet-bar-track {{
        width: 100%;
        height: 12px;
        background: rgba(0, 0, 0, 0.15);
        border-radius: 6px;
        overflow: hidden;
      }}

      .sheet-bar-fill {{
        height: 100%;
        width: 0%;
        border-radius: 6px;
      }}

      .sheet-bar-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 13px;
        color: #555048;
        margin-top: 6px;
      }}

      .sheet-citation {{
        font-family: 'Courier Prime', monospace;
        font-size: 12px;
        color: #718096;
        letter-spacing: 1px;
        text-align: right;
      }}

      /* ================= SCENE 04: JAPAN KUMAMOTO JASM (39.58s - 59.09s) ================= */
      .scene04-stage {{
        position: absolute;
        top: 90px;
        left: 80px;
        right: 80px;
        bottom: 120px;
        display: flex;
        gap: 50px;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .scene04-card {{
        flex: 1;
        height: 720px;
        background: var(--paper-cream);
        border: 1px solid rgba(0, 0, 0, 0.2);
        border-radius: 3px;
        padding: 24px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 25px 60px var(--paper-shadow);
        position: relative;
      }}

      .scene04-photo-box {{
        width: 100%;
        height: 480px;
        overflow: hidden;
        border: 1px solid rgba(0, 0, 0, 0.15);
      }}

      .scene04-photo-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: sepia(0.2) contrast(1.1);
      }}

      .scene04-meta {{
        margin-top: 20px;
      }}

      .scene04-kicker {{
        font-family: 'Courier Prime', monospace;
        font-size: 13px;
        color: #718096;
        letter-spacing: 1.5px;
      }}

      .scene04-heading {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: var(--ink-black);
        letter-spacing: 1.5px;
        margin-top: 4px;
      }}

      .scene04-desc {{
        font-family: 'Noto Serif JP', serif;
        font-size: 16px;
        color: #4a453e;
        line-height: 1.5;
        margin-top: 8px;
      }}

      .scene04-stamp-pos {{
        position: absolute;
        top: 40px;
        right: 35px;
        z-index: 25;
      }}

      /* ================= SCENE 05: 1987 FLASHBACK DOSSIER (59.09s - 82.27s) ================= */
      .scene05-stage {{
        position: absolute;
        top: 90px;
        left: 80px;
        right: 80px;
        bottom: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      /* Timeline Ruler Across Desk */
      .vintage-ruler-timeline {{
        width: 1720px;
        background: var(--paper-aged);
        border: 1px solid rgba(0, 0, 0, 0.25);
        border-radius: 4px;
        padding: 12px 36px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        position: relative;
        margin-bottom: 28px;
      }}

      .ruler-year-node {{
        font-family: 'Courier Prime', monospace;
        font-size: 20px;
        font-weight: 700;
        color: #718096;
        letter-spacing: 2px;
      }}

      .ruler-year-node.target-1987 {{
        color: var(--stamp-red);
        font-size: 26px;
        font-weight: 900;
      }}

      /* Interactive Mouse Cursor */
      .interactive-pointer {{
        position: absolute;
        top: 18px;
        left: 100px;
        width: 28px;
        height: 28px;
        pointer-events: none;
        z-index: 40;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.5));
      }}

      .scene05-cards-row {{
        display: flex;
        gap: 50px;
        width: 1720px;
      }}

      .scene05-card {{
        flex: 1;
        background: var(--paper-cream);
        border: 1px solid rgba(0, 0, 0, 0.2);
        border-radius: 3px;
        padding: 24px;
        box-shadow: 0 25px 60px var(--paper-shadow);
        position: relative;
      }}

      .scene05-img-box {{
        width: 100%;
        height: 440px;
        overflow: hidden;
        border: 1px solid rgba(0, 0, 0, 0.15);
      }}

      .scene05-img-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: grayscale(0.9) sepia(0.3) contrast(1.15);
      }}

      .scene05-meta-box {{
        margin-top: 18px;
      }}

      .scene05-meta-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 700;
        color: var(--ink-black);
        letter-spacing: 1.5px;
      }}

      .scene05-meta-desc {{
        font-family: 'Noto Serif JP', serif;
        font-size: 15px;
        color: #4a453e;
        line-height: 1.5;
        margin-top: 6px;
      }}

      /* ================= SCENE 06: MONOLITHIC TITLE REVEAL (82.27s - 96.89s) ================= */
      .scene06-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .scene06-dossier-plate {{
        background: rgba(22, 19, 16, 0.95);
        border: 2px solid var(--highlight-gold);
        border-radius: 4px;
        padding: 60px 100px;
        text-align: center;
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95);
        position: relative;
      }}

      .title-kicker-vintage {{
        font-family: 'Courier Prime', monospace;
        font-size: 16px;
        letter-spacing: 6px;
        color: var(--highlight-gold);
        text-transform: uppercase;
        margin-bottom: 20px;
      }}

      .monolithic-title-vintage {{
        font-family: 'Oswald', sans-serif;
        font-size: 130px;
        font-weight: 900;
        color: var(--paper-cream);
        letter-spacing: 8px;
        line-height: 0.95;
      }}

      .monolithic-sub-vintage {{
        font-family: 'Oswald', sans-serif;
        font-size: 42px;
        font-weight: 600;
        color: var(--highlight-gold);
        letter-spacing: 6px;
        margin-top: 16px;
        text-transform: uppercase;
      }}

      .title-hero-tag-vintage {{
        font-family: 'Noto Serif JP', serif;
        font-size: 30px;
        font-weight: 700;
        color: #dcd6c8;
        letter-spacing: 3px;
        margin-top: 36px;
      }}

      .title-clients-stamps {{
        margin-top: 45px;
        display: flex;
        gap: 32px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        font-weight: 700;
        color: #8c8273;
        letter-spacing: 3px;
      }}
    </style>
  </head>

  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{total_duration:.3f}">
      <!-- Persistent Overlays for Unified Archival Workspace -->
      <div class="persistent-vignette" data-layout-ignore></div>
      <div class="persistent-archival-grain" data-layout-ignore></div>

      <!-- Persistent Archival Top Bar -->
      <div class="archival-top-bar" data-layout-ignore>
        <div class="dossier-id-tag">
          <span class="dossier-badge">CLASSIFIED HISTORICAL DOSSIER</span>
          <span class="dossier-case-title">CASE 1987-TSMC // THE CHOKEPOINT</span>
        </div>
        <div class="dossier-status">
          SOURCE: OFFICIAL ARCHIVE RECORD // 24 FPS 1080P
        </div>
      </div>

      <!-- ================= SCENE 01: VEO 3 VIDEO LAYER (0.00s - 8.42s) ================= -->
      <video class="clip shot1-video-player" id="shot1-video" data-start="0.00" data-duration="8.42" data-track-index="1" src="assets/video/shot1_map_veo.mp4" muted playsinline></video>
      <div class="scene01-stage clip" id="scene01-stage" data-start="0.00" data-duration="8.42" data-track-index="2" data-layout-allow-overflow>
        <!-- Documentary Dossier Overlay -->
        <div class="shot1-overlay-dossier" data-layout-ignore>
          <div class="shot1-target-card" id="shot1-target-card">
            <div class="target-card-kicker">STRATEGIC CHOKEPOINT // TAIWAN STRAIT</div>
            <div class="target-card-title">台湾海峡 160KM</div>
            <div class="target-card-sub">
              新竹サイエンスパーク (Hsinchu Fab 12/20 Cluster)<br/>
              世界先端半導体供給の90%以上が集中する最前線
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 01 -->
      <div class="vintage-sub-wrapper clip" id="sub1" data-start="0.00" data-duration="8.42" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          もし明日、<span class="sub-gold">台湾海峡で戦争が勃発</span>し、たったひとつの企業が操業を停止したらどうなるでしょうか？
        </div>
      </div>
      <audio class="clip" id="vo-01" data-start="0.00" data-duration="8.42" data-track-index="3" src="assets/audio/scene_01.mp3"></audio>
      <audio class="clip" id="sfx-01-drone" data-start="0.00" data-duration="6.00" data-track-index="4" src="assets/sfx/sub_drone.wav"></audio>

      <!-- ================= SCENE 02: SUPPLY CHAIN DISRUPTION POLAROIDS (8.42s - 23.57s) ================= -->
      <div class="scene02-stage clip" id="scene02-stage" data-start="8.42" data-duration="15.15" data-track-index="1" data-layout-allow-overflow>
        <div class="scene02-desk-grid">
          <!-- Card 1: Consumer Tech (Smartphones) -->
          <div class="scene02-card" id="card-phone">
            <div class="scotch-tape-top"></div>
            <div class="card-stamp-overlay" id="stamp-phone" style="opacity: 0;">
              <div class="vintage-rubber-stamp">HALTED</div>
            </div>
            <div class="scene02-photo-wrap">
              <img src="assets/images/andy_grove_vintage.jpg" alt="Consumer Tech Microprocessor Architecture" />
            </div>
            <div class="scene02-card-body">
              <div class="scene02-tag">DOSSIER ITEM #01 // CONSUMER TECH</div>
              <div class="scene02-title">SMARTPHONES</div>
              <div class="scene02-desc">Apple iPhone (A18 Pro) · Qualcomm Snapdragon<br/>世界中の最新スマートフォン生産ラインが完全停止</div>
            </div>
          </div>

          <!-- Card 2: AI Accelerators (NVIDIA) -->
          <div class="scene02-card" id="card-ai">
            <div class="scotch-tape-top"></div>
            <div class="card-stamp-overlay" id="stamp-ai" style="opacity: 0;">
              <div class="vintage-rubber-stamp">FROZEN</div>
            </div>
            <div class="scene02-photo-wrap">
              <img src="assets/images/silicon_wafer_vintage.jpg" alt="AI GPU Chip Die" />
            </div>
            <div class="scene02-card-body">
              <div class="scene02-tag">DOSSIER ITEM #02 // FRONTIER AI</div>
              <div class="scene02-title">AI ACCELERATORS</div>
              <div class="scene02-desc">NVIDIA Blackwell / H100 · AMD MI300<br/>全フロンティアAIモデルの学習・開発が全世界で凍結</div>
            </div>
          </div>

          <!-- Card 3: Global Data Centers -->
          <div class="scene02-card" id="card-cloud">
            <div class="scotch-tape-top"></div>
            <div class="card-stamp-overlay" id="stamp-cloud" style="opacity: 0;">
              <div class="vintage-rubber-stamp">COLLAPSED</div>
            </div>
            <div class="scene02-photo-wrap">
              <img src="assets/images/hsinchu_park_vintage.jpg" alt="Global Data Center Infrastructure" />
            </div>
            <div class="scene02-card-body">
              <div class="scene02-tag">DOSSIER ITEM #03 // INFRASTRUCTURE</div>
              <div class="scene02-title">DATA CENTERS</div>
              <div class="scene02-desc">AWS · Microsoft Azure · Google Cloud<br/>世界金融・防衛・基幹通信インフラが連鎖沈黙</div>
            </div>
          </div>
        </div>

        <!-- Economic Loss Tag -->
        <div class="scene02-ticker-tag" id="scene02-ticker-tag">
          <div class="ticker-tag-lbl">GLOBAL ECONOMIC CATASTROPHE:</div>
          <div class="ticker-tag-val">-10,000,000,000,000 USD (年間1500兆円の損失)</div>
        </div>
      </div>

      <!-- Subtitle 02 -->
      <div class="vintage-sub-wrapper clip" id="sub2" data-start="8.42" data-duration="15.15" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          あなたの手元のスマートフォンは製造不能になり、<span class="sub-cyan">全世界のAI開発は完全凍結</span>。データセンターは沈黙し、世界経済は数週間で<span class="sub-red">数千兆円の壊滅的打撃</span>を受けます。
        </div>
      </div>
      <audio class="clip" id="vo-02" data-start="8.42" data-duration="15.15" data-track-index="3" src="assets/audio/scene_02.mp3"></audio>
      <audio class="clip" id="sfx-02-impact" data-start="8.60" data-duration="2.50" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SCENE 03: TSMC DOSSIER & 90% BLUEPRINT (23.57s - 39.58s) ================= -->
      <div class="scene03-stage clip" id="scene03-stage" data-start="23.57" data-duration="16.01" data-track-index="1" data-layout-allow-overflow>
        <!-- Left: Dark Blueprint Technical Schema -->
        <div class="scene03-folder" id="scene03-folder">
          <div class="blueprint-grid-overlay"></div>
          <div class="blueprint-donut-wrap">
            <svg width="280" height="280" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="42" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="11" />
              <circle id="vintage-donut-arc" cx="50" cy="50" r="42" fill="none" stroke="#e5bb54" stroke-width="11"
                stroke-dasharray="264" stroke-dashoffset="264" stroke-linecap="round"
                transform="rotate(-90 50 50)" />
            </svg>
            <div class="blueprint-donut-text">
              <div class="blueprint-num">90%</div>
              <div class="blueprint-sub">GLOBAL MONOPOLY</div>
            </div>
          </div>
          <div class="blueprint-title">最先端 3nm / 2nm プロセス供給比率</div>
          <div class="blueprint-desc">
            世界シェア90%以上をTSMCが単独供給<br/>
            代替不能な唯一無二の「チョークポイント（急所）」
          </div>
        </div>

        <!-- Right: Archival Assessment Document -->
        <div class="scene03-dossier-sheet" id="scene03-sheet">
          <div class="sheet-header-meta">
            <div class="sheet-dossier-name">
              <span class="highlighter-marker">TSMC (台湾積体電路製造)</span>
            </div>
            <div class="sheet-file-code">REPORT REF: TSMC-SHARE-1987</div>
          </div>

          <div class="sheet-bars-container">
            <!-- TSMC -->
            <div class="sheet-bar-item" style="border-left-color: var(--highlight-gold);">
              <div class="sheet-bar-head">
                <div class="sheet-firm-name">TSMC（台湾積体電路製造）</div>
                <div class="sheet-firm-val" style="color: #b78103;">90.0%</div>
              </div>
              <div class="sheet-bar-track">
                <div class="sheet-bar-fill" id="sheet-fill-tsmc" style="background: var(--highlight-gold);"></div>
              </div>
              <div class="sheet-bar-desc">Apple A18/M4、NVIDIA Blackwell、AMD Zen5の全量を受託</div>
            </div>

            <!-- Samsung -->
            <div class="sheet-bar-item" style="border-left-color: #3b82f6;">
              <div class="sheet-bar-head">
                <div class="sheet-firm-name">SAMSUNG FOUNDRY</div>
                <div class="sheet-firm-val" style="color: #2563eb;">8.0%</div>
              </div>
              <div class="sheet-bar-track">
                <div class="sheet-bar-fill" id="sheet-fill-samsung" style="background: #3b82f6;"></div>
              </div>
              <div class="sheet-bar-desc">先端プロセスの歩留まり課題に直面・自社向け優先</div>
            </div>

            <!-- Intel -->
            <div class="sheet-bar-item" style="border-left-color: #64748b;">
              <div class="sheet-bar-head">
                <div class="sheet-firm-name">INTEL IFS & OTHERS</div>
                <div class="sheet-firm-val" style="color: #475569;">2.0%</div>
              </div>
              <div class="sheet-bar-track">
                <div class="sheet-bar-fill" id="sheet-fill-intel" style="background: #64748b;"></div>
              </div>
              <div class="sheet-bar-desc">外部顧客の獲得に苦戦・巨額赤字で再編中</div>
            </div>
          </div>

          <div class="sheet-citation">
            SOURCE: TRENDFORCE INDUSTRY RESEARCH // BOSTON CONSULTING GROUP (BCG) REPORT
          </div>
        </div>
      </div>

      <!-- Subtitle 03 -->
      <div class="vintage-sub-wrapper clip" id="sub3" data-start="23.57" data-duration="16.01" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          その企業の名前は、<span class="sub-gold">TSMC（台湾積体電路製造）</span>。世界の先端半導体の90％以上を独占する、人類史上最も危険で、最も不可欠な<span class="sub-cyan">「チョークポイント（急所）」</span>です。
        </div>
      </div>
      <audio class="clip" id="vo-03" data-start="23.57" data-duration="16.01" data-track-index="3" src="assets/audio/scene_03.mp3"></audio>
      <audio class="clip" id="sfx-03-marker" data-start="24.00" data-duration="1.50" data-track-index="4" src="assets/sfx/marker_wipe.wav"></audio>

      <!-- ================= SCENE 04: JAPAN KUMAMOTO JASM (39.58s - 59.09s) ================= -->
      <div class="scene04-stage clip" id="scene04-stage" data-start="39.58" data-duration="19.51" data-track-index="1" data-layout-allow-overflow>
        <!-- Left: Kumamoto Fab Archival Photo -->
        <div class="scene04-card" id="card-jasm">
          <div class="scotch-tape-top"></div>
          <div class="scene04-stamp-pos">
            <div class="vintage-rubber-stamp">1.2兆円投入</div>
          </div>
          <div class="scene04-photo-box">
            <img src="assets/images/mount_aso_vintage.jpg" alt="Kumamoto Kikuyo JASM Fab Landscape" />
          </div>
          <div class="scene04-meta">
            <div class="scene04-kicker">KUMAMOTO, JAPAN // 2024.02</div>
            <div class="scene04-heading">JASM 熊本第1工場 開所</div>
            <div class="scene04-desc">
              のどかなキャベツ畑の真ん中に突如現れた巨大半導体拠点。<br/>
              日本政府が1兆2000億円の異例補助金を投じ、半導体復権へ賭けた歴史的プロジェクト。
            </div>
          </div>
        </div>

        <!-- Right: 93-Year-Old Morris Chang Portrait (Uncropped) -->
        <div class="scene04-card" id="card-morris-93">
          <div class="scotch-tape-top"></div>
          <div class="scene04-photo-box">
            <img src="assets/images/morris_chang_93yo.jpg" alt="Morris Chang at Kumamoto Opening Ceremony" />
          </div>
          <div class="scene04-meta">
            <div class="scene04-kicker">FOUNDER // 93 YEARS OLD</div>
            <div class="scene04-heading">モリス・チャン（張忠謀）</div>
            <div class="scene04-desc">
              「日本と台湾の半導体協力は、新たなルネサンスをもたらす」。<br/>
              政財界のトップたちが93歳の老人に深々と頭を下げた瞬間。
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 04 -->
      <div class="vintage-sub-wrapper clip" id="sub4" data-start="39.58" data-duration="19.51" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          2024年2月、日本の熊本県菊陽町。突如現れた巨大工場に、日本政府は異例の<span class="sub-gold">1兆2000億円を超える巨額補助金</span>を投じ、政財界のトップたちが<span class="sub-cyan">93歳の老人</span>に深々と頭を下げました。
        </div>
      </div>
      <audio class="clip" id="vo-04" data-start="39.58" data-duration="19.51" data-track-index="3" src="assets/audio/scene_04.mp3"></audio>
      <audio class="clip" id="sfx-04-impact" data-start="39.80" data-duration="2.50" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SCENE 05: 1987 FLASHBACK DOSSIER (59.09s - 82.27s) ================= -->
      <div class="scene05-stage clip" id="scene05-stage" data-start="59.09" data-duration="23.18" data-track-index="1" data-layout-allow-overflow>
        <!-- Vintage Ruler Timeline Across Desk -->
        <div class="vintage-ruler-timeline" id="timeline-ruler">
          <div class="ruler-year-node" id="node-2024">2024 熊本開所</div>
          <div class="ruler-year-node" id="node-2010">◀ 2010 スマホ革命</div>
          <div class="ruler-year-node" id="node-1995">◀ 1995 上場</div>
          <div class="ruler-year-node target-1987" id="node-1987">● 1987 TSMC創業</div>

          <!-- Interactive Mouse Pointer -->
          <svg class="interactive-pointer" id="mouse-pointer" viewBox="0 0 24 24" fill="#ffffff" stroke="#1a1a1a" stroke-width="1.5">
            <path d="M4 2 L4 20 L9 15 L14 22 L17 20 L12 13 L18 13 Z" />
          </svg>
        </div>

        <!-- 1987 Founding Dossier Cards Row -->
        <div class="scene05-cards-row">
          <!-- Left: 55-Year-Old Morris Chang Portrait (Uncropped) -->
          <div class="scene05-card" id="card-morris-55">
            <div class="scotch-tape-top"></div>
            <div class="scene05-img-box">
              <img src="assets/images/morris_chang_1987.jpg" alt="Morris Chang in 1987 at age 55" />
            </div>
            <div class="scene05-meta-box">
              <div class="scene05-meta-title">モリス・チャン（当時55歳）</div>
              <div class="scene05-meta-desc">
                米テキサス・インスツルメンツで出世街道を外れ、台湾政府の招聘で新竹へ渡った孤高のリーダー。
              </div>
            </div>
          </div>

          <!-- Right: 1987 Humble Fab -->
          <div class="scene05-card" id="card-fab-1987">
            <div class="scotch-tape-top"></div>
            <div class="card-stamp-overlay" id="stamp-zero" style="opacity: 0;">
              <div class="vintage-rubber-stamp">技術・資金・名声ゼロ</div>
            </div>
            <div class="scene05-img-box">
              <img src="assets/images/hsinchu_park_vintage.jpg" alt="1987 Early Hsinchu Factory Fab" />
            </div>
            <div class="scene05-meta-box">
              <div class="scene05-meta-title">1987年 新竹サイエンスパーク</div>
              <div class="scene05-meta-desc">
                「誰も見向きもしない下請け町工場」。当時の最新鋭工場に比べ、製造技術は2〜3世代遅れていた。
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 05 -->
      <div class="vintage-sub-wrapper clip" id="sub5" data-start="59.09" data-duration="23.18" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          しかし、時計の針を37年前、1987年に戻してみてください。この会社は、<span class="sub-red">技術なし、資金なし、名声なし</span>。55歳で台湾に渡った一人の男が立ち上げた<span class="sub-gold">「誰も見向きもしない下請け工場」</span>でした。
        </div>
      </div>
      <audio class="clip" id="vo-05" data-start="59.09" data-duration="23.18" data-track-index="3" src="assets/audio/scene_05.mp3"></audio>
      <audio class="clip" id="sfx-05-clock" data-start="59.20" data-duration="6.00" data-track-index="4" src="assets/sfx/clock_tick.wav"></audio>
      <audio class="clip" id="sfx-05-click" data-start="60.20" data-duration="0.50" data-track-index="5" src="assets/sfx/mouse_click.wav"></audio>
      <audio class="clip" id="sfx-05-slap" data-start="61.00" data-duration="1.20" data-track-index="6" src="assets/sfx/paper_slap.wav"></audio>

      <!-- ================= SCENE 06: MONOLITHIC TITLE REVEAL (82.27s - 96.89s) ================= -->
      <div class="scene06-stage clip" id="scene06-stage" data-start="82.27" data-duration="14.62" data-track-index="1" data-layout-allow-overflow>
        <div class="scene06-dossier-plate" id="scene06-plate">
          <div class="title-kicker-vintage" id="s6-kicker">HISTORICAL DOCUMENTARY CASE STUDY</div>
          <div class="monolithic-title-vintage" id="s6-title">TSMC</div>
          <div class="monolithic-sub-vintage" id="s6-sub">THE SEMICONDUCTOR EMPIRE</div>
          <div class="title-hero-tag-vintage" id="s6-tag">常識を覆し続けた男の狂気の逆転劇 — 1987-2024</div>
          <div class="title-clients-stamps" id="s6-clients">
            <span>[ APPLE ]</span> · <span>[ NVIDIA ]</span> · <span>[ AMD ]</span> · <span>[ QUALCOMM ]</span> · <span>[ ASML ]</span>
          </div>
        </div>
      </div>

      <!-- Subtitle 06 -->
      <div class="vintage-sub-wrapper clip" id="sub6" data-start="82.27" data-duration="14.62" data-track-index="2" data-layout-allow-overflow>
        <div class="vintage-sub-text" data-layout-ignore>
          なぜ、誰にも相手にされなかった町工場が、AppleやNVIDIA、そして米日すらひれ伏す怪物になれたのか？これは、<span class="sub-gold">常識を覆し続けた男の狂気の逆転劇</span>です。
        </div>
      </div>
      <audio class="clip" id="vo-06" data-start="82.27" data-duration="14.62" data-track-index="3" src="assets/audio/scene_06.mp3"></audio>
      <audio class="clip" id="sfx-06-impact" data-start="82.50" data-duration="3.00" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- Master Continuous Cinematic BGM Score -->
      <audio class="clip" id="bgm-master" data-start="0.00" data-duration="{total_duration:.3f}" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
    </div>

    <!-- ================= GSAP TIMELINE SCRIPT ================= -->
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // ================= SCENE 01: VEO 3 VIDEO LAYER (0.00s - 8.42s) =================
      tl.fromTo("#shot1-target-card", {{ y: 30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.8, ease: "power2.out" }}, 1.2);

      // ================= SCENE 02: SUPPLY CHAIN DISRUPTION POLAROIDS (8.42s - 23.57s) =================
      // Polaroid photo cards slam onto the desk one after another
      tl.fromTo("#card-phone", {{ y: -50, rotation: -8, opacity: 0 }}, {{ y: 0, rotation: -2, opacity: 1, duration: 0.5, ease: "back.out(1.4)" }}, 8.8);
      tl.fromTo("#card-ai", {{ y: -50, rotation: 6, opacity: 0 }}, {{ y: 0, rotation: 1, opacity: 1, duration: 0.5, ease: "back.out(1.4)" }}, 9.4);
      tl.fromTo("#card-cloud", {{ y: -50, rotation: -4, opacity: 0 }}, {{ y: 0, rotation: -1, opacity: 1, duration: 0.5, ease: "back.out(1.4)" }}, 10.0);

      // Rubber stamps slam onto cards as disruption escalates
      tl.fromTo("#stamp-phone", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.3, ease: "back.out(2.0)" }}, 12.5);
      tl.fromTo("#stamp-ai", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.3, ease: "back.out(2.0)" }}, 14.5);
      tl.fromTo("#stamp-cloud", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.3, ease: "back.out(2.0)" }}, 16.5);

      // Global Loss Tag Reveal
      tl.fromTo("#scene02-ticker-tag", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, 17.5);

      // ================= SCENE 03: TSMC DOSSIER & 90% BLUEPRINT (23.57s - 39.58s) =================
      tl.fromTo("#scene03-folder", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 23.8);
      tl.fromTo("#scene03-sheet", {{ x: 60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 24.1);

      // Radial Blueprint Donut Gauge Animation
      tl.fromTo("#vintage-donut-arc", {{ strokeDashoffset: 264 }}, {{ strokeDashoffset: 26.4, duration: 1.4, ease: "power3.out" }}, 24.4);

      // Animate Bar Charts on Dossier Sheet
      tl.to("#sheet-fill-tsmc", {{ width: "90%", duration: 1.2, ease: "power2.out" }}, 24.8);
      tl.to("#sheet-fill-samsung", {{ width: "8%", duration: 0.8, ease: "power2.out" }}, 25.4);
      tl.to("#sheet-fill-intel", {{ width: "2%", duration: 0.6, ease: "power2.out" }}, 25.7);

      // ================= SCENE 04: JAPAN KUMAMOTO JASM (39.58s - 59.09s) =================
      tl.fromTo("#card-jasm", {{ y: 40, rotation: -3, opacity: 0 }}, {{ y: 0, rotation: -1, opacity: 1, duration: 0.6, ease: "power2.out" }}, 39.8);
      tl.fromTo("#card-morris-93", {{ y: 40, rotation: 3, opacity: 0 }}, {{ y: 0, rotation: 1, opacity: 1, duration: 0.6, ease: "power2.out" }}, 40.3);

      // Slow cinematic photographic push-in on 93yo Morris Chang
      tl.to("#card-morris-93 .scene04-photo-box img", {{ scale: 1.05, duration: 16.0, ease: "none" }}, 41.0);

      // ================= SCENE 05: 1987 FLASHBACK DOSSIER (59.09s - 82.27s) =================
      tl.fromTo("#timeline-ruler", {{ y: -30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 59.2);

      // Mouse Pointer slides across timeline: 2024 -> 1987
      tl.fromTo("#mouse-pointer", {{ x: 0, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.2 }}, 59.4);
      tl.to("#mouse-pointer", {{ x: 1400, duration: 0.8, ease: "power2.inOut" }}, 59.6);
      // Mouse click bounce at 1987
      tl.to("#mouse-pointer", {{ scale: 0.8, yoyo: true, repeat: 1, duration: 0.1 }}, 60.2);

      // Dossier Cards Appear
      tl.fromTo("#card-morris-55", {{ y: 50, rotation: -3, opacity: 0 }}, {{ y: 0, rotation: -1, opacity: 1, duration: 0.6, ease: "power2.out" }}, 60.5);
      tl.fromTo("#card-fab-1987", {{ y: 50, rotation: 3, opacity: 0 }}, {{ y: 0, rotation: 1, opacity: 1, duration: 0.6, ease: "power2.out" }}, 60.9);
      tl.fromTo("#stamp-zero", {{ scale: 2.2, opacity: 0, rotation: -20 }}, {{ scale: 1.0, opacity: 1, rotation: -10, duration: 0.4, ease: "back.out(2.0)" }}, 61.5);

      // ================= SCENE 06: MONOLITHIC TITLE REVEAL (82.27s - 96.89s) =================
      tl.fromTo("#scene06-plate", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.8, ease: "power3.out" }}, 82.5);
      tl.fromTo("#s6-kicker", {{ y: -15, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 82.8);
      tl.fromTo("#s6-title", {{ scale: 1.15, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 83.2);
      tl.fromTo("#s6-sub", {{ y: 15, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 83.6);
      tl.fromTo("#s6-tag", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 84.0);
      tl.fromTo("#s6-clients", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.5, ease: "power2.out" }}, 84.5);

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open("demo-tsmc-v2/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated demo-tsmc-v2/index.html with unified vintage archival documentary aesthetic & Veo 3 integration!")
