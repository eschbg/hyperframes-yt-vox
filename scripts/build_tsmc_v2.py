import json
import os

total_duration = 86.17

html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>TSMC // The Silicon Empire (MagnatesMedia x Vox)</title>
    <!-- Google Fonts: Modern Documentary Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;600;700;800&family=Noto+Sans+JP:wght@400;600;700;900&family=Noto+Serif+JP:wght@600;700;900&family=Oswald:wght@500;600;700&display=swap" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

    <style>
      :root {{
        --bg-dark: #07090e;
        --bg-card: rgba(13, 18, 30, 0.85);
        --bg-card-border: rgba(255, 255, 255, 0.09);
        --gold-primary: #f5a623;
        --gold-glow: rgba(245, 166, 35, 0.45);
        --cyan-tech: #00d2ff;
        --cyan-glow: rgba(0, 210, 255, 0.45);
        --ivory-text: #f3efe6;
        --muted-text: #8c96a5;
        --danger-accent: #e63946;
        --danger-glow: rgba(230, 57, 70, 0.5);
      }}

      * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }}

      body {{
        background: #000;
        color: var(--ivory-text);
        font-family: 'Inter', 'Noto Sans JP', sans-serif;
        overflow: hidden;
        -webkit-font-smoothing: antialiased;
      }}

      #root {{
        position: relative;
        width: 1920px;
        height: 1080px;
        background: radial-gradient(circle at 50% 45%, #101626 0%, #07090e 75%);
        overflow: hidden;
      }}

      /* Subtle Ambient Digital Grid */
      .ambient-grid {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
          linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
        background-size: 80px 80px;
        pointer-events: none;
        z-index: 1;
      }}

      /* Global Letterbox Vignette for High-End Cinematic Look */
      .cinematic-vignette {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(ellipse at center, transparent 55%, rgba(4, 6, 10, 0.85) 100%);
        pointer-events: none;
        z-index: 50;
      }}

      /* ================= TOP BRANDING & CHAPTER HUD ================= */
      .top-hud {{
        position: absolute;
        top: 36px;
        left: 60px;
        right: 60px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 60;
      }}

      .hud-left {{
        display: flex;
        align-items: center;
        gap: 16px;
      }}

      .channel-pill {{
        background: rgba(245, 166, 35, 0.12);
        border: 1px solid var(--gold-primary);
        color: var(--gold-primary);
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 5px 14px;
        border-radius: 3px;
        text-transform: uppercase;
      }}

      .chapter-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 20px;
        font-weight: 600;
        letter-spacing: 3px;
        color: #d1d7e0;
        text-transform: uppercase;
      }}

      .hud-right {{
        display: flex;
        align-items: center;
        gap: 24px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: var(--muted-text);
        letter-spacing: 1.5px;
      }}

      .hud-status-dot {{
        display: inline-block;
        width: 8px;
        height: 8px;
        background: var(--danger-accent);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--danger-accent);
        margin-right: 6px;
        animation: pulseDot 1.5s infinite;
      }}

      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(0.85); }}
      }}

      /* ================= SUBTITLES (CLEAN GLASSMORPHIC HUD) ================= */
      .subtitle-pill {{
        position: absolute;
        bottom: 34px;
        left: 50%;
        transform: translateX(-50%);
        width: 1720px;
        min-height: 82px;
        background: rgba(9, 13, 22, 0.88);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 6px solid var(--gold-primary);
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px 40px;
        z-index: 100;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.85);
      }}

      .subtitle-text {{
        font-family: 'Noto Serif JP', serif;
        font-size: 31px;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.45;
        text-align: center;
        letter-spacing: 1.5px;
      }}

      .hl-gold {{
        color: var(--gold-primary);
        text-shadow: 0 0 12px var(--gold-glow);
      }}

      .hl-cyan {{
        color: var(--cyan-tech);
        text-shadow: 0 0 12px var(--cyan-glow);
      }}

      .hl-danger {{
        color: #ff5252;
        text-shadow: 0 0 12px var(--danger-glow);
      }}

      /* ================= GENERIC SHOT STAGE ================= */
      .shot-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
      }}

      /* ================= SHOT 1: TAIWAN STRAIT RADAR MAP ================= */
      .shot1-video-bg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: contrast(1.25) brightness(0.68) saturate(0.85);
        transform-origin: center center;
        z-index: 2;
      }}

      .radar-overlay {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 1100px;
        height: 1100px;
        pointer-events: none;
        z-index: 5;
      }}

      .radar-sweep {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: conic-gradient(from 0deg at 50% 50%, rgba(0, 210, 255, 0.25) 0deg, rgba(0, 210, 255, 0.0) 60deg, transparent 360deg);
        transform-origin: center center;
      }}

      .radar-rings {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        border: 1px solid rgba(0, 210, 255, 0.25);
        box-shadow: 
          inset 0 0 0 160px rgba(0, 210, 255, 0.015),
          inset 0 0 0 320px rgba(0, 210, 255, 0.015),
          inset 0 0 0 480px rgba(0, 210, 255, 0.015);
      }}

      .target-ping {{
        position: absolute;
        top: 480px;
        left: 980px;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .ping-crosshair {{
        width: 64px;
        height: 64px;
        border: 2px solid var(--danger-accent);
        border-radius: 50%;
        position: relative;
        box-shadow: 0 0 20px var(--danger-accent);
      }}

      .ping-crosshair::before, .ping-crosshair::after {{
        content: '';
        position: absolute;
        background: var(--danger-accent);
      }}

      .ping-crosshair::before {{
        top: 50%;
        left: -12px;
        right: -12px;
        height: 2px;
        transform: translateY(-50%);
      }}

      .ping-crosshair::after {{
        left: 50%;
        top: -12px;
        bottom: -12px;
        width: 2px;
        transform: translateX(-50%);
      }}

      .target-card {{
        margin-top: 18px;
        background: rgba(14, 18, 28, 0.92);
        border: 1px solid var(--danger-accent);
        padding: 12px 20px;
        border-radius: 4px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8);
        text-align: center;
      }}

      .target-card-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 20px;
        font-weight: 700;
        color: #ff6b6b;
        letter-spacing: 2px;
      }}

      .target-card-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #d1d7e0;
        margin-top: 4px;
      }}

      /* ================= SHOT 2: SILICON DIE & DOMINO SUPPLY CHAIN ================= */
      .domino-stage {{
        position: absolute;
        top: 140px;
        left: 80px;
        right: 80px;
        height: 740px;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 10;
      }}

      .center-chokepoint-hub {{
        display: flex;
        align-items: center;
        gap: 32px;
        margin-top: 20px;
      }}

      .wafer-core {{
        width: 170px;
        height: 170px;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 35%, #00d2ff 0%, #004e8c 60%, #071728 100%);
        border: 3px solid var(--cyan-tech);
        box-shadow: 0 0 50px rgba(0, 210, 255, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
      }}

      .wafer-core-icon {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 18px;
        font-weight: 800;
        color: #ffffff;
        text-align: center;
        letter-spacing: 1px;
        line-height: 1.3;
      }}

      .branch-cards-row {{
        display: flex;
        gap: 36px;
        margin-top: 60px;
        width: 100%;
        justify-content: center;
      }}

      .domino-card {{
        width: 520px;
        background: var(--bg-card);
        border: 1px solid var(--bg-card-border);
        border-radius: 8px;
        padding: 30px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6);
        position: relative;
        overflow: hidden;
      }}

      .domino-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: var(--cyan-tech);
      }}

      .domino-card.disrupted::before {{
        background: var(--danger-accent);
      }}

      .card-header-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        color: var(--cyan-tech);
        letter-spacing: 2px;
        margin-bottom: 12px;
      }}

      .card-title-main {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
        margin-bottom: 12px;
      }}

      .card-client-list {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 17px;
        color: var(--muted-text);
        line-height: 1.5;
        margin-bottom: 24px;
      }}

      .card-status-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: rgba(0, 210, 255, 0.12);
        border: 1px solid var(--cyan-tech);
        color: var(--cyan-tech);
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        font-weight: 700;
        padding: 8px 16px;
        border-radius: 4px;
        letter-spacing: 1.5px;
      }}

      .domino-card.disrupted .card-status-badge {{
        background: rgba(230, 57, 70, 0.18);
        border-color: var(--danger-accent);
        color: #ff6b6b;
      }}

      .metric-ticker-bar {{
        margin-top: 45px;
        background: rgba(14, 20, 32, 0.95);
        border: 1px solid rgba(245, 166, 35, 0.4);
        padding: 14px 40px;
        border-radius: 40px;
        display: flex;
        align-items: center;
        gap: 24px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
      }}

      .metric-ticker-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        color: var(--muted-text);
        letter-spacing: 2px;
      }}

      .metric-ticker-value {{
        font-family: 'Oswald', sans-serif;
        font-size: 34px;
        font-weight: 700;
        color: var(--gold-primary);
        letter-spacing: 1px;
      }}

      /* ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC ================= */
      .vox-split-stage {{
        position: absolute;
        top: 130px;
        left: 80px;
        right: 80px;
        height: 760px;
        display: flex;
        gap: 60px;
        align-items: center;
        z-index: 10;
      }}

      .vox-gauge-col {{
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        background: var(--bg-card);
        border: 1px solid var(--bg-card-border);
        border-radius: 12px;
        padding: 40px;
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
        position: relative;
      }}

      .gauge-svg-box {{
        width: 320px;
        height: 320px;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .gauge-center-text {{
        position: absolute;
        text-align: center;
      }}

      .gauge-number {{
        font-family: 'Oswald', sans-serif;
        font-size: 88px;
        font-weight: 900;
        color: var(--gold-primary);
        line-height: 1;
        text-shadow: 0 0 30px var(--gold-glow);
      }}

      .gauge-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        color: #d1d7e0;
        letter-spacing: 2px;
        margin-top: 6px;
      }}

      .gauge-footer-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 2px;
        margin-top: 24px;
        text-align: center;
      }}

      .gauge-footer-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-text);
        text-align: center;
        margin-top: 10px;
        line-height: 1.5;
      }}

      .vox-data-col {{
        flex: 1.2;
        display: flex;
        flex-direction: column;
        gap: 20px;
      }}

      .vox-stat-card {{
        background: var(--bg-card);
        border: 1px solid var(--bg-card-border);
        border-left: 6px solid var(--cyan-tech);
        border-radius: 8px;
        padding: 24px 30px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
      }}

      .stat-card-title {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
      }}

      .stat-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
      }}

      .stat-share {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 24px;
        font-weight: 700;
        color: var(--cyan-tech);
      }}

      .stat-progress-bg {{
        width: 100%;
        height: 12px;
        background: rgba(255, 255, 255, 0.08);
        border-radius: 6px;
        overflow: hidden;
        margin-bottom: 10px;
      }}

      .stat-progress-fill {{
        height: 100%;
        background: linear-gradient(90deg, #0088cc, var(--cyan-tech));
        border-radius: 6px;
        width: 0%;
      }}

      .stat-note {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 14px;
        color: var(--muted-text);
      }}

      .citation-hud {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #717d8e;
        letter-spacing: 1.2px;
        margin-top: 10px;
        padding-left: 10px;
      }}

      /* ================= SHOT 4: CINEMATIC TSMC REVEAL ================= */
      .shot4-video-bg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: contrast(1.2) brightness(0.65) saturate(1.1);
        z-index: 2;
      }}

      .reveal-hud {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        z-index: 20;
      }}

      .reveal-badge {{
        background: var(--gold-primary);
        color: #07090e;
        font-family: 'Oswald', sans-serif;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 4px;
        padding: 6px 22px;
        border-radius: 3px;
        margin-bottom: 24px;
        box-shadow: 0 0 25px var(--gold-glow);
      }}

      .reveal-title-large {{
        font-family: 'Oswald', sans-serif;
        font-size: 130px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 8px;
        line-height: 0.95;
        text-shadow: 0 10px 50px rgba(0, 0, 0, 0.9);
      }}

      .reveal-title-jp {{
        font-family: 'Noto Serif JP', serif;
        font-size: 42px;
        font-weight: 700;
        color: #e5ebf5;
        letter-spacing: 6px;
        margin-top: 18px;
        text-shadow: 0 4px 20px rgba(0,0,0,0.8);
      }}

      .reveal-subtitle-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 19px;
        font-weight: 600;
        color: var(--cyan-tech);
        letter-spacing: 4px;
        margin-top: 24px;
        border-top: 1px solid rgba(0, 210, 255, 0.4);
        padding-top: 16px;
      }}

      /* ================= SHOT 5: FOUNDRY VS IDM REVOLUTION ================= */
      .foundry-stage {{
        position: absolute;
        top: 130px;
        left: 60px;
        right: 60px;
        height: 760px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      /* Phase A: IDM Locked Box */
      .idm-locked-box {{
        width: 1100px;
        background: rgba(15, 23, 42, 0.92);
        border: 2px solid #2563eb;
        border-radius: 12px;
        padding: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(37, 99, 235, 0.25);
        position: relative;
      }}

      .idm-header-badge {{
        background: #1d4ed8;
        color: #ffffff;
        font-family: 'Oswald', sans-serif;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 3px;
        padding: 6px 20px;
        border-radius: 4px;
        margin-bottom: 24px;
      }}

      .idm-inner-flow {{
        display: flex;
        align-items: center;
        gap: 36px;
        width: 100%;
        justify-content: center;
      }}

      .idm-module {{
        flex: 1;
        background: rgba(30, 41, 59, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 8px;
        padding: 30px 24px;
        text-align: center;
      }}

      .idm-module-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
      }}

      .idm-module-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: #94a3b8;
        margin-top: 8px;
      }}

      .idm-link-arrow {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 32px;
        color: #38bdf8;
      }}

      .idm-lock-note {{
        margin-top: 28px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px;
        color: #f87171;
        letter-spacing: 1.5px;
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 10px 24px;
        border-radius: 4px;
      }}

      /* Phase B: TSMC Pure-Play Foundry Model */
      .foundry-network {{
        width: 1600px;
        display: flex;
        flex-direction: column;
        align-items: center;
        position: relative;
      }}

      .fabless-clients-row {{
        display: flex;
        gap: 32px;
        margin-bottom: 40px;
      }}

      .client-chip {{
        width: 280px;
        background: rgba(15, 23, 42, 0.90);
        border: 1px solid var(--cyan-tech);
        border-radius: 8px;
        padding: 20px 24px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 210, 255, 0.2);
      }}

      .client-chip-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 2px;
      }}

      .client-chip-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 14px;
        color: var(--cyan-tech);
        margin-top: 4px;
        letter-spacing: 1px;
      }}

      .foundry-conduits-svg {{
        width: 1200px;
        height: 70px;
      }}

      .tsmc-core-platform {{
        width: 1280px;
        background: linear-gradient(135deg, rgba(20, 28, 48, 0.95) 0%, rgba(10, 14, 26, 0.98) 100%);
        border: 2px solid var(--gold-primary);
        border-radius: 12px;
        padding: 34px 50px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 50px var(--gold-glow);
      }}

      .platform-brand {{
        display: flex;
        flex-direction: column;
      }}

      .platform-logo {{
        font-family: 'Oswald', sans-serif;
        font-size: 48px;
        font-weight: 900;
        color: var(--gold-primary);
        letter-spacing: 3px;
        line-height: 1;
      }}

      .platform-desc {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px;
        color: #d1d7e0;
        letter-spacing: 2px;
        margin-top: 6px;
      }}

      .platform-creed-box {{
        background: rgba(245, 166, 35, 0.12);
        border: 1px solid var(--gold-primary);
        padding: 14px 28px;
        border-radius: 6px;
        text-align: right;
      }}

      .creed-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: var(--gold-primary);
        letter-spacing: 2px;
        font-weight: 700;
      }}

      .creed-main {{
        font-family: 'Noto Serif JP', serif;
        font-size: 28px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 2px;
        margin-top: 4px;
      }}
    </style>
  </head>

  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{total_duration:.2f}">
      <div class="ambient-grid" data-layout-ignore></div>
      <div class="cinematic-vignette" data-layout-ignore></div>

      <!-- Global Top HUD -->
      <div class="top-hud" data-layout-ignore>
        <div class="hud-left">
          <div class="channel-pill">MAGNATES × VOX</div>
          <div class="chapter-title" id="hud-chapter-text">ACT 1 // GEOPOLITICAL CHOKEPOINT</div>
        </div>
        <div class="hud-right">
          <div><span class="hud-status-dot"></span>RISK LEVEL: CRITICAL</div>
          <div>HSINCHU 24°46'N 120°59'E</div>
        </div>
      </div>

      <!-- ================= SHOT 1: TAIWAN STRAIT RADAR MAP (0.00s - 8.42s) ================= -->
      <video class="clip shot1-video-bg" id="shot1-map" data-start="0.00" data-duration="8.42" data-track-index="1" src="assets/video/taiwan_strait_hook.mp4" muted playsinline></video>
      <div class="shot-stage clip" id="shot1-stage" data-start="0.00" data-duration="8.42" data-track-index="2" data-layout-allow-overflow>
        <div class="radar-overlay" id="shot1-radar" data-layout-ignore>
          <div class="radar-sweep" id="shot1-sweep"></div>
          <div class="radar-rings"></div>
          <div class="target-ping" id="shot1-ping">
            <div class="ping-crosshair"></div>
            <div class="target-card">
              <div class="target-card-title">HSINCHU FAB CLUSTER</div>
              <div class="target-card-sub">台湾・新竹サイエンスパーク // TSMC FAB 12 / 20</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 1 -->
      <div class="subtitle-pill clip" id="sub1" data-start="0.00" data-duration="8.42" data-track-index="3" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          もし明日、<span class="hl-gold">台湾海峡で戦争が勃発</span>し、たったひとつの企業が操業を停止したらどうなるでしょうか？
        </div>
      </div>
      <audio class="clip" id="vo-01" data-start="0.00" data-duration="8.42" data-track-index="4" src="assets/audio/scene_01.mp3"></audio>
      <audio class="clip" id="sfx-01-drone" data-start="0.00" data-duration="5.00" data-track-index="5" src="assets/sfx/sub_drone.wav"></audio>

      <!-- ================= SHOT 2: SILICON DIE & DOMINO SUPPLY CHAIN (8.42s - 23.56s) ================= -->
      <div class="shot-stage clip" id="shot2-stage" data-start="8.42" data-duration="15.14" data-track-index="2" data-layout-allow-overflow>
        <div class="domino-stage" id="shot2-container" data-layout-ignore>
          <div class="center-chokepoint-hub" id="shot2-hub">
            <div class="wafer-core">
              <div class="wafer-core-icon">SILICON<br/>CHOKEPOINT</div>
            </div>
          </div>

          <div class="branch-cards-row">
            <!-- Card 1: Smartphones -->
            <div class="domino-card" id="card-phone">
              <div class="card-header-tag">SECTOR 01 // CONSUMER TECH</div>
              <div class="card-title-main">SMARTPHONES</div>
              <div class="card-client-list">Apple iPhone (A18 Pro) · Qualcomm Snapdragon 8<br/>全世界の最新スマートフォン供給が完全停止</div>
              <div class="card-status-badge" id="badge-phone">STATUS: 70% GLOBAL SUPPLY HALT</div>
            </div>

            <!-- Card 2: AI Accelerators -->
            <div class="domino-card" id="card-ai">
              <div class="card-header-tag">SECTOR 02 // ARTIFICIAL INTELLIGENCE</div>
              <div class="card-title-main">AI ACCELERATORS</div>
              <div class="card-client-list">NVIDIA H100 / Blackwell · AMD Instinct MI300<br/>全フロンティアAIモデルの学習・開発が凍結</div>
              <div class="card-status-badge" id="badge-ai">STATUS: 90% AI COMPUTE COLLAPSE</div>
            </div>

            <!-- Card 3: Hyperscale Cloud -->
            <div class="domino-card" id="card-cloud">
              <div class="card-header-tag">SECTOR 03 // GLOBAL INFRASTRUCTURE</div>
              <div class="card-title-main">DATA CENTERS</div>
              <div class="card-client-list">AWS · Microsoft Azure · Google Cloud<br/>世界金融・防衛・通信インフラが沈黙</div>
              <div class="card-status-badge" id="badge-cloud">STATUS: GLOBAL GRID SILENCE</div>
            </div>
          </div>

          <!-- Bottom Metric Ticker -->
          <div class="metric-ticker-bar" id="shot2-metric">
            <div class="metric-ticker-label">ESTIMATED GLOBAL ANNUAL LOSS:</div>
            <div class="metric-ticker-value">10,000,000,000,000 USD (約1500兆円消失)</div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 2 -->
      <div class="subtitle-pill clip" id="sub2" data-start="8.42" data-duration="15.14" data-track-index="3" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          あなたの手元のスマートフォンは製造不能になり、<span class="hl-cyan">全世界のAI開発は完全凍結</span>。データセンターは沈黙し、世界経済は数週間で<span class="hl-danger">数千兆円の壊滅的打撃</span>を受けます。
        </div>
      </div>
      <audio class="clip" id="vo-02" data-start="8.42" data-duration="15.14" data-track-index="4" src="assets/audio/scene_02.mp3"></audio>
      <audio class="clip" id="sfx-02-impact" data-start="8.60" data-duration="2.00" data-track-index="5" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC (23.56s - 39.57s) ================= -->
      <div class="shot-stage clip" id="shot3-stage" data-start="23.56" data-duration="16.01" data-track-index="2" data-layout-allow-overflow>
        <div class="vox-split-stage" id="shot3-container" data-layout-ignore>
          <!-- Left: Big 90% Gauge -->
          <div class="vox-gauge-col" id="shot3-gauge-col">
            <div class="gauge-svg-box">
              <svg width="320" height="320" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="42" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="11" />
                <circle id="gauge-arc" cx="50" cy="50" r="42" fill="none" stroke="#f5a623" stroke-width="11"
                  stroke-dasharray="264" stroke-dashoffset="264" stroke-linecap="round"
                  transform="rotate(-90 50 50)" />
              </svg>
              <div class="gauge-center-text">
                <div class="gauge-number" id="gauge-num">90%</div>
                <div class="gauge-sub">GLOBAL SHARE</div>
              </div>
            </div>
            <div class="gauge-footer-title">最先端 3nm / 2nm 半導体</div>
            <div class="gauge-footer-desc">世界シェア90%以上をTSMC単独が寡占供給<br/>代替不能な唯一無二の急所</div>
          </div>

          <!-- Right: Market Share Comparison Breakdown -->
          <div class="vox-data-col" id="shot3-data-col">
            <!-- TSMC -->
            <div class="vox-stat-card" style="border-left-color: var(--gold-primary);">
              <div class="stat-card-title">
                <div class="stat-name">TSMC（台湾積体電路製造）</div>
                <div class="stat-share" style="color: var(--gold-primary);">90.0%</div>
              </div>
              <div class="stat-progress-bg">
                <div class="stat-progress-fill" id="bar-tsmc" style="background: var(--gold-primary);"></div>
              </div>
              <div class="stat-note">Apple A18/M4、NVIDIA Blackwell、AMD Zen5の全量受託</div>
            </div>

            <!-- Samsung -->
            <div class="vox-stat-card" style="border-left-color: #3b82f6;">
              <div class="stat-card-title">
                <div class="stat-name">SAMSUNG FOUNDRY</div>
                <div class="stat-share" style="color: #60a5fa;">8.0%</div>
              </div>
              <div class="stat-progress-bg">
                <div class="stat-progress-fill" id="bar-samsung" style="background: #3b82f6;"></div>
              </div>
              <div class="stat-note">先端歩留まりの課題に直面・自社向け優先</div>
            </div>

            <!-- Intel & Others -->
            <div class="vox-stat-card" style="border-left-color: #94a3b8;">
              <div class="stat-card-title">
                <div class="stat-name">INTEL IFS & OTHERS</div>
                <div class="stat-share" style="color: #94a3b8;">2.0%</div>
              </div>
              <div class="stat-progress-bg">
                <div class="stat-progress-fill" id="bar-intel" style="background: #64748b;"></div>
              </div>
              <div class="stat-note">外部顧客の獲得に苦戦・巨額赤字で再建中</div>
            </div>

            <div class="citation-hud">
              SOURCE: TRENDFORCE INDUSTRY RESEARCH // BCG CHOKEPOINT ASSESSMENT REPORT
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 3 -->
      <div class="subtitle-pill clip" id="sub3" data-start="23.56" data-duration="16.01" data-track-index="3" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          その企業の名前は、<span class="hl-gold">TSMC（台湾積体電路製造）</span>。世界の先端半導体の90％以上を独占する、人類史上最も危険で、最も不可欠な<span class="hl-cyan">「チョークポイント（急所）」</span>です。
        </div>
      </div>
      <audio class="clip" id="vo-03" data-start="23.56" data-duration="16.01" data-track-index="4" src="assets/audio/scene_03.mp3"></audio>

      <!-- ================= SHOT 4: CINEMATIC TSMC REVEAL (39.57s - 50.00s) ================= -->
      <video class="clip shot4-video-bg" id="shot4-bg-video" data-start="39.57" data-duration="10.43" data-track-index="1" src="assets/video/cleanroom_litho_clip.mp4" muted playsinline></video>
      <div class="shot-stage clip" id="shot4-stage" data-start="39.57" data-duration="10.43" data-track-index="2" data-layout-allow-overflow>
        <div class="reveal-hud" id="shot4-hud" data-layout-ignore>
          <div class="reveal-badge">ARCHIVAL PROFILE // 1987-2026</div>
          <div class="reveal-title-large">TSMC</div>
          <div class="reveal-title-jp">台湾積体電路製造</div>
          <div class="reveal-subtitle-tag">THE UNSEEN EMPIRE OF MODERN CIVILIZATION</div>
        </div>
      </div>

      <audio class="clip" id="sfx-04-impact" data-start="40.00" data-duration="2.50" data-track-index="5" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SHOT 5: FOUNDRY VS IDM REVOLUTION (50.00s - 86.17s) ================= -->
      <div class="shot-stage clip" id="shot5-stage" data-start="50.00" data-duration="36.17" data-track-index="2" data-layout-allow-overflow>
        <div class="foundry-stage" data-layout-ignore>
          <!-- Phase A: IDM Locked Box (50.00s - 66.00s) -->
          <div class="idm-locked-box" id="phase-idm">
            <div class="idm-header-badge">TRADITIONAL IDM MODEL (垂直統合型モデル)</div>
            <div class="idm-inner-flow">
              <div class="idm-module">
                <div class="idm-module-title">CHIP DESIGN</div>
                <div class="idm-module-sub">回路設計・アーキテクチャ開発</div>
              </div>
              <div class="idm-link-arrow">──────▶</div>
              <div class="idm-module" style="border-color: #3b82f6;">
                <div class="idm-module-title">FABRICATION</div>
                <div class="idm-module-sub">巨額工場建設（1棟 1.5兆円）</div>
              </div>
            </div>
            <div class="idm-lock-note">
              ⚠ 参入障壁：莫大な工場投資が必要 // 「工場を持たない天才」は参入不可能
            </div>
          </div>

          <!-- Phase B: TSMC Pure-Play Foundry Network (66.00s - 86.17s) -->
          <div class="foundry-network" id="phase-foundry" style="opacity: 0; display: none;">
            <!-- Top Fabless Clients -->
            <div class="fabless-clients-row">
              <div class="client-chip" id="client-apple">
                <div class="client-chip-name">APPLE</div>
                <div class="client-chip-sub">iPhone / Mac M-Series</div>
              </div>
              <div class="client-chip" id="client-nvidia">
                <div class="client-chip-name">NVIDIA</div>
                <div class="client-chip-sub">Blackwell / H100 AI</div>
              </div>
              <div class="client-chip" id="client-amd">
                <div class="client-chip-name">AMD</div>
                <div class="client-chip-sub">Zen 5 / EPYC Cloud</div>
              </div>
              <div class="client-chip" id="client-qualcomm">
                <div class="client-chip-name">QUALCOMM</div>
                <div class="client-chip-sub">Snapdragon Elite</div>
              </div>
            </div>

            <!-- Conduit SVG lines -->
            <svg class="foundry-conduits-svg" viewBox="0 0 1200 70">
              <line x1="140" y1="0" x2="600" y2="70" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
              <line x1="440" y1="0" x2="600" y2="70" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
              <line x1="760" y1="0" x2="600" y2="70" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
              <line x1="1060" y1="0" x2="600" y2="70" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
            </svg>

            <!-- Bottom TSMC Foundation Platform -->
            <div class="tsmc-core-platform" id="tsmc-platform">
              <div class="platform-brand">
                <div class="platform-logo">TSMC PURE-PLAY FOUNDRY</div>
                <div class="platform-desc">世界初・純粋受託製造専業 // 自社ブランド製品ゼロ</div>
              </div>
              <div class="platform-creed-box">
                <div class="creed-tag">FOUNDATIONAL PLEDGE (創業の鉄則)</div>
                <div class="creed-main">「顧客と絶対に競合しない」</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 5 Part 1 (50.00s - 68.48s) -->
      <div class="subtitle-pill clip" id="sub5-p1" data-start="50.00" data-duration="18.48" data-track-index="3" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          当時の半導体業界は、自社で設計し、自社の巨大工場で製造する<span class="hl-cyan">「IDM」垂直統合モデル</span>が常識でした。工場建設には数千億円が必要で、持たざる者に勝ち目はありません。
        </div>
      </div>
      <audio class="clip" id="vo-10" data-start="50.00" data-duration="18.48" data-track-index="4" src="assets/audio/scene_10.mp3"></audio>

      <!-- Subtitle for Shot 5 Part 2 (68.48s - 17.69s) -->
      <div class="subtitle-pill clip" id="sub5-p2" data-start="68.48" data-duration="17.69" data-track-index="3" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          モリス・チャンは決断します。「自社ブランドのチップは一切作らない。製造だけに特化する」。これが世界初<span class="hl-gold">「純粋受託製造（ファウンドリ）」</span>の誕生でした。
        </div>
      </div>
      <audio class="clip" id="vo-11" data-start="68.48" data-duration="17.69" data-track-index="4" src="assets/audio/scene_11.mp3"></audio>

      <!-- Master Tension BGM Score -->
      <audio class="clip" id="bgm-master" data-start="0.00" data-duration="{total_duration:.2f}" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
    </div>

    <!-- ================= GSAP TIMELINE SCRIPT ================= -->
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // ================= SHOT 1: TAIWAN STRAIT RADAR MAP (0.00s - 8.42s) =================
      tl.fromTo("#shot1-map", {{ scale: 1.0, filter: "contrast(1.25) brightness(0.40)" }}, {{ scale: 1.08, filter: "contrast(1.25) brightness(0.68)", duration: 8.42, ease: "none" }}, 0.0);
      tl.to("#shot1-sweep", {{ rotate: 360 * 2, duration: 8.42, ease: "none" }}, 0.0);
      tl.fromTo("#shot1-ping", {{ scale: 0.6, opacity: 0 }}, {{ scale: 1.0, opacity: 1.0, duration: 0.7, ease: "back.out(1.8)" }}, 1.2);

      // ================= SHOT 2: SILICON DIE & DOMINO SUPPLY CHAIN (8.42s - 23.56s) =================
      tl.fromTo("#shot2-hub", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }}, 8.6);
      
      // Cascading Domino Cards
      tl.fromTo("#card-phone", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.2);
      tl.fromTo("#card-ai", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.7);
      tl.fromTo("#card-cloud", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 10.2);

      // Disruption triggers as voiceover escalates
      tl.to("#card-phone", {{ borderColor: "var(--danger-accent)", duration: 0.4 }}, 12.5);
      tl.to("#card-phone", {{ className: "+=disrupted" }}, 12.5);
      tl.to("#card-ai", {{ borderColor: "var(--danger-accent)", duration: 0.4 }}, 14.5);
      tl.to("#card-ai", {{ className: "+=disrupted" }}, 14.5);
      tl.to("#card-cloud", {{ borderColor: "var(--danger-accent)", duration: 0.4 }}, 16.5);
      tl.to("#card-cloud", {{ className: "+=disrupted" }}, 16.5);

      // Metric Ticker Bar
      tl.fromTo("#shot2-metric", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, 17.5);

      // ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC (23.56s - 39.57s) =================
      tl.fromTo("#shot3-gauge-col", {{ x: -50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 23.8);
      tl.fromTo("#shot3-data-col", {{ x: 50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 24.1);

      // Animate Radial Donut Gauge (stroke-dashoffset from 264 to 264 * (1 - 0.90) = 26.4)
      tl.fromTo("#gauge-arc", {{ strokeDashoffset: 264 }}, {{ strokeDashoffset: 26.4, duration: 1.4, ease: "power3.out" }}, 24.3);

      // Animate Bar Charts
      tl.to("#bar-tsmc", {{ width: "90%", duration: 1.2, ease: "power2.out" }}, 24.6);
      tl.to("#bar-samsung", {{ width: "8%", duration: 0.8, ease: "power2.out" }}, 25.2);
      tl.to("#bar-intel", {{ width: "2%", duration: 0.6, ease: "power2.out" }}, 25.5);

      // Deep camera push into 90% monopoly
      tl.to("#shot3-container", {{ scale: 1.05, duration: 5.0, ease: "none" }}, 29.0);

      // ================= SHOT 4: CINEMATIC TSMC REVEAL (39.57s - 50.00s) =================
      tl.fromTo("#shot4-hud .reveal-badge", {{ y: -20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 39.8);
      tl.fromTo("#shot4-hud .reveal-title-large", {{ scale: 1.3, opacity: 0, filter: "blur(12px)" }}, {{ scale: 1.0, opacity: 1, filter: "blur(0px)", duration: 0.7, ease: "power3.out" }}, 40.1);
      tl.fromTo("#shot4-hud .reveal-title-jp", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 40.6);
      tl.fromTo("#shot4-hud .reveal-subtitle-tag", {{ scale: 0.95, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 41.0);

      // ================= SHOT 5: FOUNDRY VS IDM REVOLUTION (50.00s - 86.17s) =================
      // Update HUD Chapter Text
      tl.call(() => {{
        const el = document.getElementById("hud-chapter-text");
        if (el) el.innerText = "ACT 2 // THE FOUNDRY REVOLUTION";
      }}, null, 50.0);

      // Phase A: IDM Locked Box entrance
      tl.fromTo("#phase-idm", {{ scale: 0.92, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 50.3);
      tl.to("#phase-idm", {{ scale: 1.04, duration: 14.0, ease: "none" }}, 51.0);

      // Phase Transition: Break IDM box and reveal TSMC Foundry Network at 66.00s
      tl.to("#phase-idm", {{ scale: 0.85, opacity: 0, duration: 0.5, ease: "power2.in" }}, 65.5);
      tl.call(() => {{
        const idm = document.getElementById("phase-idm");
        const fnd = document.getElementById("phase-foundry");
        if (idm) idm.style.display = "none";
        if (fnd) fnd.style.display = "flex";
      }}, null, 66.0);

      tl.fromTo("#phase-foundry", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4 }}, 66.0);
      tl.fromTo("#tsmc-platform", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }}, 66.2);
      
      // Fabless clients connect in cascade
      tl.fromTo("#client-apple", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.0);
      tl.fromTo("#client-nvidia", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.3);
      tl.fromTo("#client-amd", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.6);
      tl.fromTo("#client-qualcomm", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.9);

      // Creed badge illuminates with golden pulse
      tl.fromTo(".platform-creed-box", {{ scale: 0.9, boxShadow: "0 0 0 rgba(245, 166, 35, 0)" }}, {{ scale: 1.05, boxShadow: "0 0 35px rgba(245, 166, 35, 0.6)", duration: 0.6, ease: "back.out(1.8)" }}, 72.0);

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open("demo-tsmc-v2/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated clean modern MagnatesMedia x Vox composition in demo-tsmc-v2/index.html!")
