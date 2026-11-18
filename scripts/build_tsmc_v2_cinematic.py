import json
import os

total_duration = 86.17

html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>TSMC // The Geopolitical Chokepoint (MagnatesMedia x Vox)</title>
    <!-- Google Fonts: Modern Documentary Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&family=Noto+Sans+JP:wght@400;600;700;900&family=Noto+Serif+JP:wght@600;700;900&family=Oswald:wght@500;600;700;900&display=swap" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

    <style>
      :root {{
        --bg-obsidian: #04070d;
        --gold-primary: #f5a623;
        --gold-glow: rgba(245, 166, 35, 0.45);
        --cyan-tech: #00d2ff;
        --cyan-glow: rgba(0, 210, 255, 0.45);
        --danger-red: #ff3344;
        --danger-glow: rgba(255, 51, 68, 0.55);
        --ivory-text: #f3efe6;
        --muted-gray: #828c9b;
        --border-glass: rgba(255, 255, 255, 0.12);
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
        background: var(--bg-obsidian);
        overflow: hidden;
      }}

      /* Fullscreen Cinematic Film Grain & Vignette */
      .cinematic-vignette {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(ellipse at center, transparent 45%, rgba(2, 4, 8, 0.92) 100%);
        pointer-events: none;
        z-index: 60;
      }}

      .film-grain {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.04;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 65;
      }}

      /* ================= TOP TACTICAL HUD ================= */
      .top-hud {{
        position: absolute;
        top: 32px;
        left: 56px;
        right: 56px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 70;
      }}

      .hud-left {{
        display: flex;
        align-items: center;
        gap: 16px;
      }}

      .hud-badge {{
        background: rgba(245, 166, 35, 0.12);
        border: 1px solid var(--gold-primary);
        color: var(--gold-primary);
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 5px 14px;
        border-radius: 2px;
        text-transform: uppercase;
      }}

      .hud-title {{
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
        color: var(--muted-gray);
        letter-spacing: 1.5px;
      }}

      .hud-status-dot {{
        display: inline-block;
        width: 8px;
        height: 8px;
        background: var(--danger-red);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--danger-red);
        margin-right: 6px;
        animation: pulseDot 1.4s infinite;
      }}

      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}

      /* ================= SUBTITLES (CLEAN DOCUMENTARY GLASS) ================= */
      .subtitle-container {{
        position: absolute;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 1720px;
        min-height: 80px;
        background: rgba(6, 10, 18, 0.90);
        backdrop-filter: blur(18px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 6px solid var(--gold-primary);
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px 36px;
        z-index: 100;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9);
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
        text-shadow: 0 0 14px var(--gold-glow);
      }}

      .hl-cyan {{
        color: var(--cyan-tech);
        text-shadow: 0 0 14px var(--cyan-glow);
      }}

      .hl-danger {{
        color: #ff4757;
        text-shadow: 0 0 14px var(--danger-glow);
      }}

      /* ================= SHOT 1: GEOPOLITICAL 3D MAP SCENE ================= */
      .map-viewport-3d {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        perspective: 1100px;
        perspective-origin: 50% 50%;
        overflow: hidden;
      }}

      .map-world-3d {{
        position: absolute;
        top: 50%;
        left: 50%;
        width: 2400px;
        height: 1600px;
        margin-top: -800px;
        margin-left: -1200px;
        transform-style: preserve-3d;
        will-change: transform;
      }}

      /* Layer 0: High-Res Graded Terrain */
      .map-layer-terrain {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: translateZ(0px);
        filter: contrast(1.3) brightness(0.72) saturate(0.9);
      }}

      /* Layer 1: Tactical Geopolitical Vector Overlays */
      .map-vectors-svg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        transform: translateZ(25px);
        pointer-events: none;
      }}

      /* Tactical Labels & Markers Floating in 2.5D Parallax */
      .geo-label {{
        position: absolute;
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        letter-spacing: 3px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95);
        pointer-events: none;
      }}

      .geo-label-china {{
        top: 480px;
        left: 540px;
        transform: translateZ(35px);
        font-size: 32px;
        color: rgba(255, 100, 100, 0.9);
      }}

      .geo-label-china span {{
        display: block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        color: #e57373;
        letter-spacing: 1.5px;
        margin-top: 4px;
      }}

      .geo-label-taiwan {{
        top: 720px;
        left: 1680px;
        transform: translateZ(45px);
        font-size: 36px;
        color: var(--cyan-tech);
      }}

      .geo-label-taiwan span {{
        display: block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        color: #80deea;
        letter-spacing: 2px;
        margin-top: 4px;
      }}

      .geo-median-tag {{
        top: 780px;
        left: 1140px;
        transform: translateZ(40px) rotate(-55deg);
        background: rgba(255, 51, 68, 0.2);
        border: 1px dashed var(--danger-red);
        color: #ff6b6b;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 4px 12px;
        letter-spacing: 2px;
        border-radius: 2px;
      }}

      /* Layer 3: Hsinchu Tactical Target Reticle & Telemetry Callout */
      .hsinchu-target-beacon {{
        position: absolute;
        top: 620px;
        left: 1480px;
        transform: translateZ(90px) translate(-50%, -50%);
        pointer-events: none;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .reticle-core {{
        width: 58px;
        height: 58px;
        border: 2px solid var(--danger-red);
        border-radius: 50%;
        position: relative;
        box-shadow: 0 0 25px var(--danger-red);
        animation: reticleSpin 8s linear infinite;
      }}

      @keyframes reticleSpin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      .reticle-core::before, .reticle-core::after {{
        content: '';
        position: absolute;
        background: var(--danger-red);
      }}

      .reticle-core::before {{
        top: 50%;
        left: -10px;
        right: -10px;
        height: 2px;
        transform: translateY(-50%);
      }}

      .reticle-core::after {{
        left: 50%;
        top: -10px;
        bottom: -10px;
        width: 2px;
        transform: translateX(-50%);
      }}

      .reticle-pulse-ring {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 110px;
        height: 110px;
        border: 2px dashed rgba(255, 51, 68, 0.6);
        border-radius: 50%;
        animation: pulseRing 2s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
      }}

      @keyframes pulseRing {{
        0% {{ transform: translate(-50%, -50%) scale(0.6); opacity: 1; }}
        100% {{ transform: translate(-50%, -50%) scale(1.6); opacity: 0; }}
      }}

      .target-telemetry-box {{
        margin-top: 22px;
        background: rgba(8, 12, 22, 0.94);
        border: 1px solid var(--danger-red);
        border-left: 5px solid var(--danger-red);
        padding: 14px 22px;
        border-radius: 4px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9);
        min-width: 380px;
      }}

      .telemetry-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 22px;
        font-weight: 700;
        color: #ff6b6b;
        letter-spacing: 2px;
      }}

      .telemetry-coords {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #a0aec0;
        margin-top: 4px;
        letter-spacing: 1px;
      }}

      .telemetry-stat {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 15px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 8px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 8px;
      }}

      /* Controlled Tactical Glitch Layer */
      .glitch-layer {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 55;
        opacity: 0;
        background: repeating-linear-gradient(0deg, rgba(0, 210, 255, 0.08) 0px, rgba(255, 51, 68, 0.08) 2px, transparent 4px);
      }}

      /* ================= SHOT 2: SILICON DIE & DOMINO SUPPLY DISRUPTION ================= */
      .shockwave-stage {{
        position: absolute;
        top: 100px;
        left: 60px;
        right: 60px;
        bottom: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .die-centerpiece {{
        position: relative;
        width: 220px;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }}

      .wafer-die-img {{
        width: 180px;
        height: 180px;
        border-radius: 12px;
        border: 2px solid var(--cyan-tech);
        box-shadow: 0 0 40px rgba(0, 210, 255, 0.5);
        object-fit: cover;
      }}

      .die-label {{
        position: absolute;
        bottom: -28px;
        background: #080c14;
        border: 1px solid var(--cyan-tech);
        color: var(--cyan-tech);
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 3px;
        letter-spacing: 2px;
      }}

      .shockwave-circuit-svg {{
        width: 1600px;
        height: 110px;
      }}

      .domino-sectors-row {{
        display: flex;
        gap: 40px;
        width: 1680px;
        justify-content: space-between;
      }}

      .sector-column {{
        flex: 1;
        background: rgba(10, 16, 28, 0.88);
        border: 1px solid var(--border-glass);
        border-top: 4px solid var(--cyan-tech);
        border-radius: 6px;
        padding: 26px 30px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.7);
        position: relative;
      }}

      .sector-column.disrupted {{
        border-top-color: var(--danger-red);
      }}

      .sector-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        color: var(--cyan-tech);
        letter-spacing: 2px;
        margin-bottom: 8px;
      }}

      .sector-column.disrupted .sector-tag {{
        color: #ff6b6b;
      }}

      .sector-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 34px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
        line-height: 1.1;
        margin-bottom: 12px;
      }}

      .sector-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-gray);
        line-height: 1.5;
        margin-bottom: 20px;
      }}

      .sector-alert-pill {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: rgba(0, 210, 255, 0.12);
        border: 1px solid var(--cyan-tech);
        color: var(--cyan-tech);
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 8px 16px;
        border-radius: 3px;
        letter-spacing: 1.5px;
      }}

      .sector-column.disrupted .sector-alert-pill {{
        background: rgba(255, 51, 68, 0.2);
        border-color: var(--danger-red);
        color: #ff6b6b;
      }}

      .global-damage-ticker {{
        margin-top: 36px;
        background: rgba(12, 16, 26, 0.95);
        border: 1px solid rgba(245, 166, 35, 0.5);
        border-radius: 30px;
        padding: 12px 38px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
      }}

      .ticker-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        color: var(--muted-gray);
        letter-spacing: 2px;
      }}

      .ticker-val {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: var(--gold-primary);
        letter-spacing: 1.5px;
      }}

      /* ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC ================= */
      .vox-layout-split {{
        position: absolute;
        top: 110px;
        left: 60px;
        right: 60px;
        bottom: 120px;
        display: flex;
        align-items: center;
        gap: 60px;
        z-index: 10;
      }}

      .vox-donut-box {{
        flex: 1;
        background: rgba(10, 16, 28, 0.90);
        border: 1px solid var(--border-glass);
        border-radius: 8px;
        padding: 36px;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 0 20px 50px rgba(0,0,0,0.7);
      }}

      .gauge-svg-wrap {{
        width: 300px;
        height: 300px;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
      }}

      .gauge-inner-content {{
        position: absolute;
        text-align: center;
      }}

      .gauge-big-num {{
        font-family: 'Oswald', sans-serif;
        font-size: 92px;
        font-weight: 900;
        color: var(--gold-primary);
        line-height: 1;
        text-shadow: 0 0 35px var(--gold-glow);
      }}

      .gauge-big-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        color: #cbd5e1;
        letter-spacing: 2px;
        margin-top: 4px;
      }}

      .donut-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 30px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 2px;
        margin-top: 20px;
        text-align: center;
      }}

      .donut-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-gray);
        text-align: center;
        margin-top: 8px;
        line-height: 1.45;
      }}

      .vox-bars-box {{
        flex: 1.25;
        display: flex;
        flex-direction: column;
        gap: 22px;
      }}

      .bar-row-card {{
        background: rgba(10, 16, 28, 0.88);
        border: 1px solid var(--border-glass);
        border-radius: 6px;
        padding: 22px 28px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.5);
      }}

      .bar-row-head {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
      }}

      .bar-row-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
      }}

      .bar-row-val {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 24px;
        font-weight: 700;
      }}

      .bar-track {{
        width: 100%;
        height: 12px;
        background: rgba(255, 255, 255, 0.07);
        border-radius: 6px;
        overflow: hidden;
        margin-bottom: 10px;
      }}

      .bar-fill {{
        height: 100%;
        border-radius: 6px;
        width: 0%;
      }}

      .bar-note {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 14px;
        color: var(--muted-gray);
      }}

      .vox-citation {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #64748b;
        letter-spacing: 1.2px;
        margin-top: 8px;
      }}

      /* ================= SHOT 4: CINEMATIC TSMC REVEAL ================= */
      .reveal-video-layer {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: contrast(1.22) brightness(0.60) saturate(1.1);
        z-index: 2;
      }}

      .reveal-stage {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        z-index: 25;
      }}

      .reveal-kicker {{
        background: var(--gold-primary);
        color: #04070d;
        font-family: 'Oswald', sans-serif;
        font-size: 17px;
        font-weight: 800;
        letter-spacing: 4px;
        padding: 6px 20px;
        border-radius: 2px;
        margin-bottom: 22px;
        box-shadow: 0 0 25px var(--gold-glow);
      }}

      .reveal-hero-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 140px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 10px;
        line-height: 0.92;
        text-shadow: 0 10px 50px rgba(0, 0, 0, 0.95);
      }}

      .reveal-hero-jp {{
        font-family: 'Noto Serif JP', serif;
        font-size: 42px;
        font-weight: 700;
        color: #e2e8f0;
        letter-spacing: 6px;
        margin-top: 16px;
        text-shadow: 0 4px 25px rgba(0,0,0,0.9);
      }}

      .reveal-hero-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 18px;
        font-weight: 600;
        color: var(--cyan-tech);
        letter-spacing: 4px;
        margin-top: 24px;
        border-top: 1px solid rgba(0, 210, 255, 0.4);
        padding-top: 14px;
      }}

      /* ================= SHOT 5: FOUNDRY VS IDM REVOLUTION ================= */
      .explainer-stage {{
        position: absolute;
        top: 100px;
        left: 60px;
        right: 60px;
        bottom: 120px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      /* Phase A: IDM Locked Container */
      .idm-vault-box {{
        width: 1140px;
        background: rgba(12, 18, 32, 0.92);
        border: 2px solid #2563eb;
        border-radius: 8px;
        padding: 44px;
        display: flex;
        flex-direction: column;
        align-items: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(37, 99, 235, 0.25);
      }}

      .idm-vault-badge {{
        background: #1d4ed8;
        color: #ffffff;
        font-family: 'Oswald', sans-serif;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 3px;
        padding: 6px 20px;
        border-radius: 3px;
        margin-bottom: 28px;
      }}

      .idm-flow-row {{
        display: flex;
        align-items: center;
        gap: 36px;
        width: 100%;
        justify-content: center;
      }}

      .idm-brick {{
        flex: 1;
        background: rgba(24, 34, 54, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 6px;
        padding: 30px 24px;
        text-align: center;
      }}

      .idm-brick-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
      }}

      .idm-brick-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: #94a3b8;
        margin-top: 8px;
      }}

      .idm-arrow {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 32px;
        color: #38bdf8;
      }}

      .idm-barrier-note {{
        margin-top: 30px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        color: #f87171;
        letter-spacing: 1.5px;
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 10px 24px;
        border-radius: 4px;
      }}

      /* Phase B: TSMC Pure-Play Foundry Network */
      .foundry-tree {{
        width: 1600px;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .fabless-nodes-row {{
        display: flex;
        gap: 32px;
        margin-bottom: 36px;
      }}

      .fabless-card {{
        width: 280px;
        background: rgba(12, 18, 32, 0.90);
        border: 1px solid var(--cyan-tech);
        border-radius: 6px;
        padding: 20px 24px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 210, 255, 0.2);
      }}

      .fabless-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 2px;
      }}

      .fabless-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 14px;
        color: var(--cyan-tech);
        margin-top: 4px;
      }}

      .foundry-beams-svg {{
        width: 1200px;
        height: 65px;
      }}

      .tsmc-bedrock {{
        width: 1280px;
        background: linear-gradient(135deg, rgba(20, 28, 48, 0.95) 0%, rgba(8, 12, 22, 0.98) 100%);
        border: 2px solid var(--gold-primary);
        border-radius: 8px;
        padding: 34px 50px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.85), 0 0 45px var(--gold-glow);
      }}

      .bedrock-brand {{
        display: flex;
        flex-direction: column;
      }}

      .bedrock-logo {{
        font-family: 'Oswald', sans-serif;
        font-size: 46px;
        font-weight: 900;
        color: var(--gold-primary);
        letter-spacing: 3px;
        line-height: 1;
      }}

      .bedrock-desc {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px;
        color: #cbd5e1;
        letter-spacing: 2px;
        margin-top: 6px;
      }}

      .creed-container {{
        background: rgba(245, 166, 35, 0.12);
        border: 1px solid var(--gold-primary);
        padding: 14px 28px;
        border-radius: 4px;
        text-align: right;
      }}

      .creed-kicker {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: var(--gold-primary);
        letter-spacing: 2px;
        font-weight: 700;
      }}

      .creed-heading {{
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
      <div class="cinematic-vignette" data-layout-ignore></div>
      <div class="film-grain" data-layout-ignore></div>
      <div class="glitch-layer" id="glitch-overlay" data-layout-ignore></div>

      <!-- Top Tactical HUD -->
      <div class="top-hud" data-layout-ignore>
        <div class="hud-left">
          <div class="hud-badge">MAGNATES × VOX</div>
          <div class="hud-title" id="hud-chapter-text">ACT 1 // GEOPOLITICAL CHOKEPOINT</div>
        </div>
        <div class="hud-right">
          <div><span class="hud-status-dot"></span>RISK LEVEL: DEFCON 1</div>
          <div>TAIWAN STRAIT 24°46'N 120°59'E</div>
        </div>
      </div>

      <!-- ================= SHOT 1: 3D GEOPOLITICAL MAP FLYOVER (0.00s - 8.42s) ================= -->
      <div class="map-viewport-3d clip" id="shot1-stage" data-start="0.00" data-duration="8.42" data-track-index="1" data-layout-allow-overflow>
        <div class="map-world-3d" id="map-world-3d" data-layout-ignore>
          <!-- Layer 0: High-Res Graded Tactical Map -->
          <img class="map-layer-terrain" src="assets/images/tactical_3d_map_base.jpg" alt="CSIS Taiwan Strait Strategic Map" />

          <!-- Layer 1: Geopolitical Boundaries & Strategic Lines -->
          <svg class="map-vectors-svg" viewBox="0 0 2400 1600">
            <!-- Median Line (海峡中間線) -->
            <line x1="1400" y1="320" x2="1080" y2="1200" stroke="#ff3344" stroke-width="4" stroke-dasharray="14,10" filter="drop-shadow(0 0 8px #ff3344)" />
            
            <!-- Northern Maritime Blockade Perimeter -->
            <path d="M 1250 380 Q 1550 250 1850 420" fill="none" stroke="#ff3344" stroke-width="3" stroke-dasharray="8,6" opacity="0.8" />
            <!-- Southern Maritime Blockade Perimeter -->
            <path d="M 1000 1150 Q 1280 1380 1550 1200" fill="none" stroke="#ff3344" stroke-width="3" stroke-dasharray="8,6" opacity="0.8" />

            <!-- Strategic Commercial Shipping Corridors -->
            <line x1="950" y1="200" x2="800" y2="1400" stroke="#00d2ff" stroke-width="2" stroke-dasharray="6,8" opacity="0.5" />
            <line x1="1950" y1="250" x2="1850" y2="1450" stroke="#00d2ff" stroke-width="2" stroke-dasharray="6,8" opacity="0.5" />
          </svg>

          <!-- Layer 2: 2.5D Parallax Geographic Labels -->
          <div class="geo-label geo-label-china">
            CHINA // 中国
            <span>EASTERN THEATER COMMAND (東部戦区)</span>
          </div>

          <div class="geo-label geo-label-taiwan">
            TAIWAN // 台湾
            <span>CRITICAL ISLAND CORRIDOR</span>
          </div>

          <div class="geo-label geo-median-tag">
            MEDIAN LINE // 海峡中間線 (160 KM)
          </div>

          <!-- Layer 3: Hsinchu Tactical Reticle & Telemetry Callout (Elevated at Z: 90px) -->
          <div class="hsinchu-target-beacon" id="hsinchu-beacon">
            <div class="reticle-core"></div>
            <div class="reticle-pulse-ring"></div>
            <div class="target-telemetry-box" id="hsinchu-telemetry">
              <div class="telemetry-title">TARGET // 新竹サイエンスパーク</div>
              <div class="telemetry-coords">TSMC FAB 12 / 20 CLUSTER · 24°46'N 120°59'E</div>
              <div class="telemetry-stat">
                ◆ 最先端半導体の90%以上が集中 // 海岸線からわずか160km
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 1 -->
      <div class="subtitle-container clip" id="sub1" data-start="0.00" data-duration="8.42" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          もし明日、<span class="hl-gold">台湾海峡で戦争が勃発</span>し、たったひとつの企業が操業を停止したらどうなるでしょうか？
        </div>
      </div>
      <audio class="clip" id="vo-01" data-start="0.00" data-duration="8.42" data-track-index="3" src="assets/audio/scene_01.mp3"></audio>
      <audio class="clip" id="sfx-01-drone" data-start="0.00" data-duration="6.00" data-track-index="4" src="assets/sfx/sub_riser_tension.wav"></audio>
      <audio class="clip" id="sfx-01-sonar" data-start="1.20" data-duration="2.00" data-track-index="5" src="assets/sfx/sonar_ping.wav"></audio>
      <audio class="clip" id="sfx-01-glitch" data-start="7.10" data-duration="0.30" data-track-index="6" src="assets/sfx/tactical_glitch.wav"></audio>

      <!-- ================= SHOT 2: SILICON DIE & DOMINO SUPPLY DISRUPTION (8.42s - 23.56s) ================= -->
      <div class="shockwave-stage clip" id="shot2-stage" data-start="8.42" data-duration="15.14" data-track-index="1" data-layout-allow-overflow>
        <!-- Centerpiece Silicon Die -->
        <div class="die-centerpiece" id="shot2-die">
          <img class="wafer-die-img" src="assets/images/silicon_wafer_vintage.jpg" alt="Silicon Microprocessor Die" />
          <div class="die-label">TSMC 3NM CORE</div>
        </div>

        <!-- Glowing Circuit Conduit Lines -->
        <svg class="shockwave-circuit-svg" viewBox="0 0 1600 110">
          <line x1="800" y1="0" x2="270" y2="110" stroke="#00d2ff" stroke-width="3" stroke-dasharray="8,6" />
          <line x1="800" y1="0" x2="800" y2="110" stroke="#00d2ff" stroke-width="3" stroke-dasharray="8,6" />
          <line x1="800" y1="0" x2="1330" y2="110" stroke="#00d2ff" stroke-width="3" stroke-dasharray="8,6" />
        </svg>

        <!-- 3 Domino Shockwave Columns -->
        <div class="domino-sectors-row">
          <!-- Sector 1: Smartphones -->
          <div class="sector-column" id="sector-phone">
            <div class="sector-tag">SECTOR 01 // CONSUMER TECH</div>
            <div class="sector-title">SMARTPHONES</div>
            <div class="sector-desc">Apple iPhone (A18 Pro) · Qualcomm Snapdragon 8<br/>世界中の最新スマートフォン生産ラインが完全停止</div>
            <div class="sector-alert-pill" id="pill-phone">STATUS: 70% GLOBAL SUPPLY HALTED</div>
          </div>

          <!-- Sector 2: AI & Supercomputing -->
          <div class="sector-column" id="sector-ai">
            <div class="sector-tag">SECTOR 02 // ARTIFICIAL INTELLIGENCE</div>
            <div class="sector-title">AI ACCELERATORS</div>
            <div class="sector-desc">NVIDIA H100 / Blackwell · AMD Instinct MI300<br/>全フロンティアAIモデルの学習・開発が全世界で凍結</div>
            <div class="sector-alert-pill" id="pill-ai">STATUS: 90% AI COMPUTE COLLAPSED</div>
          </div>

          <!-- Sector 3: Hyperscale Cloud -->
          <div class="sector-column" id="sector-cloud">
            <div class="sector-tag">SECTOR 03 // GLOBAL INFRASTRUCTURE</div>
            <div class="sector-title">DATA CENTERS</div>
            <div class="sector-desc">AWS · Microsoft Azure · Google Cloud<br/>世界金融・防衛・基幹通信インフラが連鎖沈黙</div>
            <div class="sector-alert-pill" id="pill-cloud">STATUS: GLOBAL GRID SILENCED</div>
          </div>
        </div>

        <!-- Massive Loss Ticker -->
        <div class="global-damage-ticker" id="shot2-ticker">
          <div class="ticker-lbl">GLOBAL ECONOMIC CATASTROPHE:</div>
          <div class="ticker-val">-10,000,000,000,000 USD (年間1500兆円の損失)</div>
        </div>
      </div>

      <!-- Subtitle for Shot 2 -->
      <div class="subtitle-container clip" id="sub2" data-start="8.42" data-duration="15.14" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          あなたの手元のスマートフォンは製造不能になり、<span class="hl-cyan">全世界のAI開発は完全凍結</span>。データセンターは沈黙し、世界経済は数週間で<span class="hl-danger">数千兆円の壊滅的打撃</span>を受けます。
        </div>
      </div>
      <audio class="clip" id="vo-02" data-start="8.42" data-duration="15.14" data-track-index="3" src="assets/audio/scene_02.mp3"></audio>
      <audio class="clip" id="sfx-02-impact" data-start="8.60" data-duration="2.50" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC (23.56s - 39.57s) ================= -->
      <div class="vox-layout-split clip" id="shot3-stage" data-start="23.56" data-duration="16.01" data-track-index="1" data-layout-allow-overflow>
        <!-- Left: Glowing 90% Donut Gauge -->
        <div class="vox-donut-box" id="shot3-donut">
          <div class="gauge-svg-wrap">
            <svg width="300" height="300" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="42" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="11" />
              <circle id="vox-donut-arc" cx="50" cy="50" r="42" fill="none" stroke="#f5a623" stroke-width="11"
                stroke-dasharray="264" stroke-dashoffset="264" stroke-linecap="round"
                transform="rotate(-90 50 50)" />
            </svg>
            <div class="gauge-inner-content">
              <div class="gauge-big-num">90%</div>
              <div class="gauge-big-lbl">GLOBAL MONOPOLY</div>
            </div>
          </div>
          <div class="donut-title">最先端 3nm / 2nm 半導体</div>
          <div class="donut-sub">世界シェア90%以上をTSMCが単独供給<br/>代替不能な唯一無二の「チョークポイント」</div>
        </div>

        <!-- Right: Market Share Comparison -->
        <div class="vox-bars-box" id="shot3-bars">
          <!-- TSMC -->
          <div class="bar-row-card" style="border-left: 6px solid var(--gold-primary);">
            <div class="bar-row-head">
              <div class="bar-row-name">TSMC（台湾積体電路製造）</div>
              <div class="bar-row-val" style="color: var(--gold-primary);">90.0%</div>
            </div>
            <div class="bar-track">
              <div class="bar-fill" id="fill-tsmc" style="background: var(--gold-primary);"></div>
            </div>
            <div class="bar-note">Apple A18/M4、NVIDIA Blackwell、AMD Zen5の全量を受託</div>
          </div>

          <!-- Samsung -->
          <div class="bar-row-card" style="border-left: 6px solid #3b82f6;">
            <div class="bar-row-head">
              <div class="bar-row-name">SAMSUNG FOUNDRY</div>
              <div class="bar-row-val" style="color: #60a5fa;">8.0%</div>
            </div>
            <div class="bar-track">
              <div class="bar-fill" id="fill-samsung" style="background: #3b82f6;"></div>
            </div>
            <div class="bar-note">先端プロセスの歩留まり課題に直面・自社向け優先</div>
          </div>

          <!-- Intel & Others -->
          <div class="bar-row-card" style="border-left: 6px solid #94a3b8;">
            <div class="bar-row-head">
              <div class="bar-row-name">INTEL IFS & OTHERS</div>
              <div class="bar-row-val" style="color: #94a3b8;">2.0%</div>
            </div>
            <div class="bar-track">
              <div class="bar-fill" id="fill-intel" style="background: #64748b;"></div>
            </div>
            <div class="bar-note">外部顧客の獲得に苦戦・巨額赤字で再編中</div>
          </div>

          <div class="vox-citation">
            SOURCE: TRENDFORCE INDUSTRY RESEARCH // BOSTON CONSULTING GROUP (BCG) REPORT
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 3 -->
      <div class="subtitle-container clip" id="sub3" data-start="23.56" data-duration="16.01" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          その企業の名前は、<span class="hl-gold">TSMC（台湾積体電路製造）</span>。世界の先端半導体の90％以上を独占する、人類史上最も危険で、最も不可欠な<span class="hl-cyan">「チョークポイント（急所）」</span>です。
        </div>
      </div>
      <audio class="clip" id="vo-03" data-start="23.56" data-duration="16.01" data-track-index="3" src="assets/audio/scene_03.mp3"></audio>

      <!-- ================= SHOT 4: CINEMATIC REVEAL TSMC (39.57s - 50.00s) ================= -->
      <video class="clip reveal-video-layer" id="shot4-video" data-start="39.57" data-duration="10.43" data-track-index="1" src="assets/video/cleanroom_litho_clip.mp4" muted playsinline></video>
      <div class="reveal-stage clip" id="shot4-stage" data-start="39.57" data-duration="10.43" data-track-index="2" data-layout-allow-overflow>
        <div class="reveal-kicker">ARCHIVAL PROFILE // 1987-2026</div>
        <div class="reveal-hero-name">TSMC</div>
        <div class="reveal-hero-jp">台湾積体電路製造</div>
        <div class="reveal-hero-tag">THE UNSEEN EMPIRE OF MODERN CIVILIZATION</div>
      </div>
      <audio class="clip" id="sfx-04-impact" data-start="40.00" data-duration="2.50" data-track-index="5" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SHOT 5: FOUNDRY VS IDM REVOLUTION (50.00s - 86.17s) ================= -->
      <div class="explainer-stage clip" id="shot5-stage" data-start="50.00" data-duration="36.17" data-track-index="1" data-layout-allow-overflow>
        <!-- Phase A: IDM Locked Box (50.00s - 66.00s) -->
        <div class="idm-vault-box" id="phase-idm" data-layout-ignore>
          <div class="idm-vault-badge">TRADITIONAL IDM MODEL (垂直統合型モデル)</div>
          <div class="idm-flow-row">
            <div class="idm-brick">
              <div class="idm-brick-title">CHIP DESIGN</div>
              <div class="idm-brick-sub">回路設計・アーキテクチャ開発</div>
            </div>
            <div class="idm-arrow">──────▶</div>
            <div class="idm-brick" style="border-color: #3b82f6;">
              <div class="idm-brick-title">FABRICATION</div>
              <div class="idm-brick-sub">巨額工場建設（1棟 1.5兆円）</div>
            </div>
          </div>
          <div class="idm-barrier-note">
            ⚠ 巨額の資本障壁：IntelやMotorolaなど巨大企業のみが独占 // 「持たざる者」は参入不能
          </div>
        </div>

        <!-- Phase B: TSMC Pure-Play Foundry Network (66.00s - 86.17s) -->
        <div class="foundry-tree" id="phase-foundry" style="opacity: 0; display: none;" data-layout-ignore>
          <!-- Fabless Client Nodes -->
          <div class="fabless-nodes-row">
            <div class="fabless-card" id="card-apple">
              <div class="fabless-name">APPLE</div>
              <div class="fabless-sub">iPhone / M-Series</div>
            </div>
            <div class="fabless-card" id="card-nvidia">
              <div class="fabless-name">NVIDIA</div>
              <div class="fabless-sub">Blackwell / H100 AI</div>
            </div>
            <div class="fabless-card" id="card-amd">
              <div class="fabless-name">AMD</div>
              <div class="fabless-sub">Zen 5 / EPYC Cloud</div>
            </div>
            <div class="fabless-card" id="card-qualcomm">
              <div class="fabless-name">QUALCOMM</div>
              <div class="fabless-sub">Snapdragon Elite</div>
            </div>
          </div>

          <!-- Connecting Beams SVG -->
          <svg class="foundry-beams-svg" viewBox="0 0 1200 65">
            <line x1="140" y1="0" x2="600" y2="65" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
            <line x1="440" y1="0" x2="600" y2="65" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
            <line x1="760" y1="0" x2="600" y2="65" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
            <line x1="1060" y1="0" x2="600" y2="65" stroke="#00d2ff" stroke-width="3" stroke-dasharray="6,4" />
          </svg>

          <!-- TSMC Foundation Platform -->
          <div class="tsmc-bedrock" id="tsmc-bedrock">
            <div class="bedrock-brand">
              <div class="bedrock-logo">TSMC PURE-PLAY FOUNDRY</div>
              <div class="bedrock-desc">世界初・純粋受託製造専業 // 自社ブランド製品ゼロ</div>
            </div>
            <div class="creed-container">
              <div class="creed-kicker">FOUNDATIONAL PLEDGE (創業の鉄則)</div>
              <div class="creed-heading">「顧客と絶対に競合しない」</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle for Shot 5 Part 1 (50.00s - 68.48s) -->
      <div class="subtitle-container clip" id="sub5-p1" data-start="50.00" data-duration="18.48" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          当時の半導体業界は、自社で設計し、自社の巨大工場で製造する<span class="hl-cyan">「IDM」垂直統合モデル</span>が常識でした。工場建設には数千億円が必要で、持たざる者に勝ち目はありません。
        </div>
      </div>
      <audio class="clip" id="vo-10" data-start="50.00" data-duration="18.48" data-track-index="3" src="assets/audio/scene_10.mp3"></audio>

      <!-- Subtitle for Shot 5 Part 2 (68.48s - 17.69s) -->
      <div class="subtitle-container clip" id="sub5-p2" data-start="68.48" data-duration="17.69" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          モリス・チャンは決断します。「自社ブランドのチップは一切作らない。製造だけに特化する」。これが世界初<span class="hl-gold">「純粋受託製造（ファウンドリ）」</span>の誕生でした。
        </div>
      </div>
      <audio class="clip" id="vo-11" data-start="68.48" data-duration="17.69" data-track-index="3" src="assets/audio/scene_11.mp3"></audio>

      <!-- Master Tension BGM Score -->
      <audio class="clip" id="bgm-master" data-start="0.00" data-duration="{total_duration:.2f}" data-track-index="25" src="assets/audio/cinematic_score.mp3"></audio>
    </div>

    <!-- ================= GSAP TIMELINE SCRIPT ================= -->
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // ================= SHOT 1: GEOPOLITICAL 3D MAP FLYOVER (0.00s - 8.42s) =================
      // Initial 3D Camera Rig: High-Altitude Tactical Bird's-Eye View
      tl.set("#map-world-3d", {{
        transformPerspective: 1100,
        rotateX: 38,
        rotateY: -7,
        rotateZ: -12,
        scale: 0.95,
        x: 120,
        y: -40,
        z: -80
      }});

      // Target Beacon Entrance
      tl.fromTo("#hsinchu-beacon", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.8, ease: "back.out(1.8)" }}, 1.2);
      tl.fromTo("#hsinchu-telemetry", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 1.6);

      // 3D Camera Dive & Parallax Sweep into Hsinchu Science Park (1.6s to 7.0s)
      tl.to("#map-world-3d", {{
        rotateX: 18,
        rotateY: -2,
        rotateZ: -4,
        scale: 2.35,
        x: -780,
        y: -310,
        z: 220,
        duration: 5.4,
        ease: "power2.inOut"
      }}, 1.6);

      // Controlled Tactical Glitch at 7.10s (overlay flash and chromatic shift on container)
      tl.to("#glitch-overlay", {{ opacity: 0.85, duration: 0.08, yoyo: true, repeat: 3, ease: "rough" }}, 7.1);
      tl.fromTo("#shot1-stage", 
        {{ filter: "drop-shadow(0px 0 transparent)" }}, 
        {{ filter: "drop-shadow(-6px 0 rgba(255,51,68,0.8)) drop-shadow(6px 0 rgba(0,210,255,0.8))", duration: 0.08, yoyo: true, repeat: 2 }}, 
        7.12
      );

      // ================= SHOT 2: SILICON DIE & DOMINO SUPPLY DISRUPTION (8.42s - 23.56s) =================
      tl.fromTo("#shot2-die", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }}, 8.6);
      
      // Cascading Domino Columns
      tl.fromTo("#sector-phone", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.2);
      tl.fromTo("#sector-ai", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.7);
      tl.fromTo("#sector-cloud", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 10.2);

      // Disruption triggers as voiceover escalates
      tl.to("#sector-phone", {{ className: "+=disrupted" }}, 12.5);
      tl.to("#sector-ai", {{ className: "+=disrupted" }}, 14.5);
      tl.to("#sector-cloud", {{ className: "+=disrupted" }}, 16.5);

      // Global Damage Ticker
      tl.fromTo("#shot2-ticker", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, 17.5);

      // ================= SHOT 3: VOX 90% MONOPOLY INFOGRAPHIC (23.56s - 39.57s) =================
      tl.fromTo("#shot3-donut", {{ x: -50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 23.8);
      tl.fromTo("#shot3-bars", {{ x: 50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 24.1);

      // Animate Radial Donut Gauge (stroke-dashoffset from 264 to 26.4 for 90%)
      tl.fromTo("#vox-donut-arc", {{ strokeDashoffset: 264 }}, {{ strokeDashoffset: 26.4, duration: 1.4, ease: "power3.out" }}, 24.3);

      // Animate Bar Charts
      tl.to("#fill-tsmc", {{ width: "90%", duration: 1.2, ease: "power2.out" }}, 24.6);
      tl.to("#fill-samsung", {{ width: "8%", duration: 0.8, ease: "power2.out" }}, 25.2);
      tl.to("#fill-intel", {{ width: "2%", duration: 0.6, ease: "power2.out" }}, 25.5);

      // ================= SHOT 4: CINEMATIC REVEAL TSMC (39.57s - 50.00s) =================
      tl.fromTo("#shot4-stage .reveal-kicker", {{ y: -20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 39.8);
      tl.fromTo("#shot4-stage .reveal-hero-name", {{ scale: 1.3, opacity: 0, filter: "blur(12px)" }}, {{ scale: 1.0, opacity: 1, filter: "blur(0px)", duration: 0.7, ease: "power3.out" }}, 40.1);
      tl.fromTo("#shot4-stage .reveal-hero-jp", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 40.6);
      tl.fromTo("#shot4-stage .reveal-hero-tag", {{ scale: 0.95, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 41.0);

      // ================= SHOT 5: FOUNDRY VS IDM REVOLUTION (50.00s - 86.17s) =================
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
      tl.fromTo("#tsmc-bedrock", {{ y: 50, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.7, ease: "back.out(1.4)" }}, 66.2);
      
      // Fabless clients connect in cascade
      tl.fromTo("#card-apple", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.0);
      tl.fromTo("#card-nvidia", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.3);
      tl.fromTo("#card-amd", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.6);
      tl.fromTo("#card-qualcomm", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 67.9);

      // Creed badge illuminates with golden pulse
      tl.fromTo(".creed-container", {{ scale: 0.9, boxShadow: "0 0 0 rgba(245, 166, 35, 0)" }}, {{ scale: 1.05, boxShadow: "0 0 35px rgba(245, 166, 35, 0.6)", duration: 0.6, ease: "back.out(1.8)" }}, 72.0);

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open("demo-tsmc-v2/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Regenerated demo-tsmc-v2/index.html with authentic 3D CSIS Geopolitical Map & Parallax!")
