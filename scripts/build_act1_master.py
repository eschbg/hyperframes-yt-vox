import json
import os

# Total Act 1 duration
total_duration = 96.888

# Master HTML for TSMC Act 1 (MagnatesMedia x Vox x Archival Documentary)
html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <title>TSMC // The Semiconductor Empire (Act 1 Master)</title>
    <!-- Google Fonts: Modern Documentary Typography -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&family=Noto+Sans+JP:wght@400;600;700;900&family=Noto+Serif+JP:wght@600;700;900&family=Oswald:wght@500;600;700;900&display=swap" rel="stylesheet" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>

    <style>
      :root {{
        --bg-charcoal: #11151b;
        --bg-paper: #e9e1d2;
        --tech-blue: #315e78;
        --tech-blue-glow: rgba(49, 94, 120, 0.5);
        --info-yellow: #e5bb54;
        --info-yellow-glow: rgba(229, 187, 84, 0.45);
        --crisis-red: #c34c45;
        --crisis-red-glow: rgba(195, 76, 69, 0.55);
        --neutral-white: #f1f1ed;
        --muted-gray: #8892a0;
        --border-glass: rgba(255, 255, 255, 0.12);
      }}

      * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }}

      body {{
        background: #000;
        color: var(--neutral-white);
        font-family: 'Inter', 'Noto Sans JP', sans-serif;
        overflow: hidden;
        -webkit-font-smoothing: antialiased;
      }}

      #root {{
        position: relative;
        width: 1920px;
        height: 1080px;
        background: var(--bg-charcoal);
        overflow: hidden;
      }}

      /* Fullscreen Cinematic Overlays */
      .cinematic-vignette {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(ellipse at center, transparent 40%, rgba(17, 21, 27, 0.88) 95%);
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

      .glitch-layer {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 68;
        opacity: 0;
        background: repeating-linear-gradient(0deg, rgba(49, 94, 120, 0.12) 0px, rgba(195, 76, 69, 0.12) 2px, transparent 4px);
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
        background: rgba(229, 187, 84, 0.12);
        border: 1px solid var(--info-yellow);
        color: var(--info-yellow);
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
        background: var(--crisis-red);
        border-radius: 50%;
        box-shadow: 0 0 10px var(--crisis-red);
        margin-right: 6px;
        animation: pulseDot 1.4s infinite;
      }}

      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}

      /* ================= SUBTITLES (PREMIUM GLASS DOCUMENTARY) ================= */
      .subtitle-container {{
        position: absolute;
        bottom: 28px;
        left: 50%;
        transform: translateX(-50%);
        width: 1720px;
        min-height: 80px;
        background: rgba(17, 21, 27, 0.92);
        backdrop-filter: blur(18px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 6px solid var(--info-yellow);
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
        color: var(--info-yellow);
        text-shadow: 0 0 14px var(--info-yellow-glow);
      }}

      .hl-cyan {{
        color: #48cae4;
        text-shadow: 0 0 14px rgba(72, 202, 228, 0.45);
      }}

      .hl-danger {{
        color: var(--crisis-red);
        text-shadow: 0 0 14px var(--crisis-red-glow);
      }}

      /* ================= SCENE 01: SATELLITE GEOPOLITICAL MAP ================= */
      .scene01-viewport {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        perspective: 1200px;
        perspective-origin: 50% 50%;
        overflow: hidden;
        background: var(--bg-charcoal);
      }}

      .scene01-map-plane {{
        position: absolute;
        top: 50%;
        left: 50%;
        width: 2800px;
        height: 1800px;
        margin-top: -900px;
        margin-left: -1400px;
        transform-style: preserve-3d;
        will-change: transform;
      }}

      .map-img-terrain {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        transform: translateZ(0px);
        filter: contrast(1.22) brightness(0.85);
      }}

      .map-svg-overlays {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        transform: translateZ(25px);
        pointer-events: none;
      }}

      /* Radar Sweep Cone */
      .radar-cone-rotator {{
        position: absolute;
        top: 800px;
        left: 1350px;
        width: 900px;
        height: 900px;
        margin-top: -450px;
        margin-left: -450px;
        transform: translateZ(35px);
        pointer-events: none;
        animation: radarSpin 7s linear infinite;
      }}

      @keyframes radarSpin {{
        from {{ transform: translateZ(35px) rotate(0deg); }}
        to {{ transform: translateZ(35px) rotate(360deg); }}
      }}

      /* Geographic Tactical Labels */
      .tactical-geo-label {{
        position: absolute;
        font-family: 'Oswald', sans-serif;
        font-weight: 700;
        letter-spacing: 3px;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.95);
        pointer-events: none;
      }}

      .label-china {{
        top: 780px;
        left: 560px;
        transform: translateZ(40px);
        font-size: 32px;
        color: rgba(229, 115, 115, 0.95);
      }}

      .label-china span {{
        display: block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        color: #ef9a9a;
        letter-spacing: 1.5px;
        margin-top: 4px;
      }}

      .label-taiwan {{
        top: 860px;
        left: 1750px;
        transform: translateZ(45px);
        font-size: 38px;
        color: #48cae4;
      }}

      .label-taiwan span {{
        display: block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        color: #90e0ef;
        letter-spacing: 2px;
        margin-top: 4px;
      }}

      .label-median-line {{
        top: 920px;
        left: 1300px;
        transform: translateZ(38px) rotate(-62deg);
        background: rgba(195, 76, 69, 0.25);
        border: 1px dashed var(--crisis-red);
        color: #ff8a80;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 4px 14px;
        letter-spacing: 2px;
        border-radius: 2px;
      }}

      /* Hsinchu Target Reticle & Telemetry */
      .hsinchu-beacon-rig {{
        position: absolute;
        top: 640px;
        left: 1610px;
        transform: translateZ(85px) translate(-50%, -50%);
        pointer-events: none;
        display: flex;
        flex-direction: column;
        align-items: center;
      }}

      .hsinchu-reticle-circle {{
        width: 64px;
        height: 64px;
        border: 2px solid var(--crisis-red);
        border-radius: 50%;
        position: relative;
        box-shadow: 0 0 25px var(--crisis-red);
        animation: reticleSpin 9s linear infinite;
      }}

      @keyframes reticleSpin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      .hsinchu-reticle-circle::before, .hsinchu-reticle-circle::after {{
        content: '';
        position: absolute;
        background: var(--crisis-red);
      }}

      .hsinchu-reticle-circle::before {{
        top: 50%;
        left: -12px;
        right: -12px;
        height: 2px;
        transform: translateY(-50%);
      }}

      .hsinchu-reticle-circle::after {{
        left: 50%;
        top: -12px;
        bottom: -12px;
        width: 2px;
        transform: translateX(-50%);
      }}

      .hsinchu-pulse-ring {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 120px;
        height: 120px;
        border: 2px dashed rgba(195, 76, 69, 0.7);
        border-radius: 50%;
        animation: pulseRing 2.2s cubic-bezier(0.2, 0.8, 0.2, 1) infinite;
      }}

      @keyframes pulseRing {{
        0% {{ transform: translate(-50%, -50%) scale(0.5); opacity: 1; }}
        100% {{ transform: translate(-50%, -50%) scale(1.7); opacity: 0; }}
      }}

      .hsinchu-telemetry-panel {{
        margin-top: 24px;
        background: rgba(17, 21, 27, 0.95);
        border: 1px solid var(--crisis-red);
        border-left: 6px solid var(--crisis-red);
        padding: 16px 24px;
        border-radius: 4px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.9);
        min-width: 420px;
      }}

      .telemetry-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #ff8a80;
        letter-spacing: 2px;
      }}

      .telemetry-coords {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        color: #a0aec0;
        margin-top: 4px;
        letter-spacing: 1.5px;
      }}

      .telemetry-stat {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        font-weight: 700;
        color: #ffffff;
        margin-top: 8px;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 8px;
      }}

      /* ================= SCENE 02: DOMINO SUPPLY DISRUPTION ================= */
      .scene02-stage {{
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

      .scene02-die {{
        position: relative;
        width: 220px;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }}

      .scene02-die img {{
        width: 180px;
        height: 180px;
        border-radius: 12px;
        border: 2px solid var(--tech-blue);
        box-shadow: 0 0 40px var(--tech-blue-glow);
        object-fit: cover;
      }}

      .die-chip-label {{
        position: absolute;
        bottom: -28px;
        background: #0d131a;
        border: 1px solid var(--tech-blue);
        color: #64b5f6;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 4px 14px;
        border-radius: 3px;
        letter-spacing: 2px;
      }}

      .scene02-svg-conduit {{
        width: 1600px;
        height: 100px;
      }}

      .scene02-domino-row {{
        display: flex;
        gap: 40px;
        width: 1680px;
        justify-content: space-between;
      }}

      .domino-column {{
        flex: 1;
        background: rgba(17, 21, 27, 0.90);
        border: 1px solid var(--border-glass);
        border-top: 5px solid var(--tech-blue);
        border-radius: 6px;
        padding: 26px 30px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.7);
        position: relative;
      }}

      .domino-column.disrupted {{
        border-top-color: var(--crisis-red);
      }}

      .domino-sector-tag {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        color: #64b5f6;
        letter-spacing: 2px;
        margin-bottom: 8px;
      }}

      .domino-column.disrupted .domino-sector-tag {{
        color: #ff8a80;
      }}

      .domino-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 34px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
        line-height: 1.1;
        margin-bottom: 12px;
      }}

      .domino-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-gray);
        line-height: 1.5;
        margin-bottom: 20px;
      }}

      .domino-alert-pill {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: rgba(49, 94, 120, 0.2);
        border: 1px solid var(--tech-blue);
        color: #90caf9;
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 700;
        padding: 8px 16px;
        border-radius: 3px;
        letter-spacing: 1.5px;
      }}

      .domino-column.disrupted .domino-alert-pill {{
        background: rgba(195, 76, 69, 0.22);
        border-color: var(--crisis-red);
        color: #ff8a80;
      }}

      .scene02-ticker {{
        margin-top: 36px;
        background: rgba(17, 21, 27, 0.95);
        border: 1px solid var(--info-yellow);
        border-radius: 30px;
        padding: 12px 38px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.8);
      }}

      .ticker-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        font-weight: 700;
        color: var(--info-yellow);
        letter-spacing: 2px;
      }}

      .ticker-val {{
        font-family: 'Oswald', sans-serif;
        font-size: 26px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
      }}

      /* ================= SCENE 03: TSMC REVEAL & VOX 90% GAUGE ================= */
      .scene03-split-stage {{
        position: absolute;
        top: 110px;
        left: 100px;
        right: 100px;
        bottom: 130px;
        display: flex;
        gap: 60px;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .scene03-donut-box {{
        flex: 1;
        background: rgba(17, 21, 27, 0.92);
        border: 1px solid var(--border-glass);
        border-top: 4px solid var(--info-yellow);
        border-radius: 6px;
        padding: 40px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
      }}

      .gauge-svg-wrap {{
        position: relative;
        width: 280px;
        height: 280px;
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
        font-size: 78px;
        font-weight: 900;
        color: var(--info-yellow);
        line-height: 1;
        text-shadow: 0 0 25px var(--info-yellow-glow);
      }}

      .gauge-big-lbl {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        color: var(--neutral-white);
        letter-spacing: 2.5px;
        margin-top: 6px;
      }}

      .donut-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
        margin-top: 24px;
        text-align: center;
      }}

      .donut-sub {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-gray);
        margin-top: 8px;
        text-align: center;
        line-height: 1.5;
      }}

      .scene03-bars-box {{
        flex: 1.25;
        background: rgba(17, 21, 27, 0.92);
        border: 1px solid var(--border-glass);
        border-radius: 6px;
        padding: 40px;
        display: flex;
        flex-direction: column;
        gap: 24px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
      }}

      .bar-row-card {{
        background: rgba(24, 30, 40, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 4px;
        padding: 16px 22px;
      }}

      .bar-row-head {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
      }}

      .bar-row-name {{
        font-family: 'Oswald', sans-serif;
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
      }}

      .bar-row-val {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 900;
        letter-spacing: 1px;
      }}

      .bar-track {{
        width: 100%;
        height: 14px;
        background: rgba(0, 0, 0, 0.45);
        border-radius: 7px;
        overflow: hidden;
      }}

      .bar-fill {{
        height: 100%;
        width: 0%;
        border-radius: 7px;
      }}

      .bar-note {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 13px;
        color: var(--muted-gray);
        margin-top: 8px;
      }}

      .vox-citation {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        color: #64748b;
        letter-spacing: 1.5px;
        margin-top: 10px;
        text-align: right;
      }}

      /* ================= SCENE 04: JAPAN KUMAMOTO JASM & 93YO MORRIS CHANG ================= */
      .scene04-stage {{
        position: absolute;
        top: 100px;
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
        background: rgba(17, 21, 27, 0.94);
        border: 1px solid var(--border-glass);
        border-radius: 6px;
        padding: 24px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 25px 60px rgba(0,0,0,0.85);
        position: relative;
      }}

      .card-photo-frame {{
        width: 100%;
        height: 480px;
        border-radius: 4px;
        overflow: hidden;
        position: relative;
        border: 1px solid rgba(255, 255, 255, 0.1);
      }}

      .card-photo-frame img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
      }}

      .card-info-box {{
        margin-top: 20px;
        display: flex;
        flex-direction: column;
      }}

      .card-kicker {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        color: var(--info-yellow);
        text-transform: uppercase;
      }}

      .card-heading {{
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1.5px;
        margin-top: 4px;
      }}

      .card-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 16px;
        color: var(--muted-gray);
        line-height: 1.5;
        margin-top: 8px;
      }}

      .subsidy-badge-banner {{
        position: absolute;
        top: -24px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(17, 21, 27, 0.98);
        border: 2px solid var(--info-yellow);
        padding: 10px 32px;
        border-radius: 30px;
        display: flex;
        align-items: center;
        gap: 16px;
        box-shadow: 0 10px 35px var(--info-yellow-glow);
        z-index: 25;
      }}

      .subsidy-badge-text {{
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 900;
        color: var(--info-yellow);
        letter-spacing: 2px;
      }}

      /* ================= SCENE 05: 1987 FLASHBACK ARCHIVE DESK ================= */
      .scene05-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        background: var(--bg-paper);
        color: #1a1e24;
        z-index: 10;
        overflow: hidden;
      }}

      .scene05-paper-bg {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.35;
        pointer-events: none;
      }}

      .scene05-timeline-bar {{
        position: absolute;
        top: 40px;
        left: 80px;
        right: 80px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(0, 0, 0, 0.15);
        border-radius: 30px;
        padding: 10px 32px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        z-index: 20;
      }}

      .timeline-step {{
        font-family: 'Oswald', sans-serif;
        font-size: 22px;
        font-weight: 700;
        color: #718096;
        letter-spacing: 2px;
      }}

      .timeline-step.active {{
        color: #c53030;
        font-size: 28px;
        font-weight: 900;
      }}

      .scene05-content-row {{
        position: absolute;
        top: 130px;
        left: 80px;
        right: 80px;
        bottom: 130px;
        display: flex;
        gap: 60px;
        align-items: center;
      }}

      .scene05-card-left, .scene05-card-right {{
        flex: 1;
        background: #ffffff;
        border: 1px solid rgba(0, 0, 0, 0.15);
        border-radius: 4px;
        padding: 24px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        position: relative;
      }}

      .scene05-photo-box {{
        width: 100%;
        height: 480px;
        border: 1px solid rgba(0, 0, 0, 0.12);
        overflow: hidden;
      }}

      .scene05-photo-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: sepia(0.2) contrast(1.1);
      }}

      .archival-red-stamp {{
        position: absolute;
        top: 40px;
        right: 40px;
        border: 3px solid var(--crisis-red);
        color: var(--crisis-red);
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 900;
        letter-spacing: 3px;
        padding: 6px 18px;
        text-transform: uppercase;
        transform: rotate(-12deg);
        background: rgba(255, 255, 255, 0.85);
        box-shadow: 0 4px 15px rgba(195, 76, 69, 0.2);
      }}

      .archival-info-meta {{
        margin-top: 18px;
        font-family: 'Noto Serif JP', serif;
      }}

      .archival-meta-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 28px;
        font-weight: 700;
        color: #1a202c;
        letter-spacing: 1.5px;
      }}

      .archival-meta-desc {{
        font-family: 'Noto Sans JP', sans-serif;
        font-size: 15px;
        color: #4a5568;
        margin-top: 6px;
        line-height: 1.5;
      }}

      /* ================= SCENE 06: MONOLITHIC TITLE REVEAL ================= */
      .scene06-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        background: var(--bg-charcoal);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 10;
      }}

      .title-kicker {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 6px;
        color: var(--info-yellow);
        text-transform: uppercase;
        margin-bottom: 20px;
      }}

      .monolithic-title {{
        font-family: 'Oswald', sans-serif;
        font-size: 140px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 8px;
        line-height: 0.95;
        text-shadow: 0 0 60px rgba(255, 255, 255, 0.25);
      }}

      .monolithic-subtitle {{
        font-family: 'Oswald', sans-serif;
        font-size: 44px;
        font-weight: 600;
        color: var(--info-yellow);
        letter-spacing: 6px;
        margin-top: 14px;
        text-transform: uppercase;
      }}

      .title-hero-tag {{
        font-family: 'Noto Serif JP', serif;
        font-size: 32px;
        font-weight: 700;
        color: #cbd5e1;
        letter-spacing: 4px;
        margin-top: 36px;
      }}

      .title-clients-line {{
        margin-top: 50px;
        display: flex;
        gap: 36px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px;
        font-weight: 700;
        color: #64748b;
        letter-spacing: 3px;
      }}
    </style>
  </head>

  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{total_duration:.3f}">
      <!-- Persistent Overlays -->
      <div class="cinematic-vignette" data-layout-ignore></div>
      <div class="film-grain" data-layout-ignore></div>
      <div class="glitch-layer" id="glitch-overlay" data-layout-ignore></div>

      <!-- Top Tactical HUD -->
      <div class="top-hud" data-layout-ignore>
        <div class="hud-left">
          <div class="hud-badge">MAGNATES × VOX</div>
          <div class="hud-title" id="hud-chapter-text">ACT 1 // THE GEOPOLITICAL BOTTLENECK</div>
        </div>
        <div class="hud-right">
          <div><span class="hud-status-dot"></span>RISK LEVEL: DEFCON 1</div>
          <div>TAIWAN STRAIT 24°46'N 120°59'E</div>
        </div>
      </div>

      <!-- ================= SCENE 01: SATELLITE GEOPOLITICAL MAP (0.00s - 8.42s) ================= -->
      <div class="scene01-viewport clip" id="scene01-stage" data-start="0.00" data-duration="8.42" data-track-index="1" data-layout-allow-overflow>
        <div class="scene01-map-plane" id="scene01-map-plane" data-layout-ignore>
          <!-- Seamless High-Res Graded Satellite Map (2800x1800) -->
          <img class="map-img-terrain" src="assets/images/tactical_3d_map_base.jpg" alt="CSIS Taiwan Strait Geopolitical Map" />

          <!-- Tactical Geopolitical Vector Overlays -->
          <svg class="map-svg-overlays" viewBox="0 0 2800 1800">
            <!-- Median Line (海峡中間線) -->
            <line x1="1620" y1="380" x2="1240" y2="1420" stroke="#c34c45" stroke-width="4" stroke-dasharray="14,10" filter="drop-shadow(0 0 8px #c34c45)" />
            <!-- Commercial Shipping Corridors -->
            <line x1="1050" y1="200" x2="880" y2="1600" stroke="#315e78" stroke-width="2" stroke-dasharray="6,8" opacity="0.6" />
            <line x1="2100" y1="250" x2="1980" y2="1650" stroke="#315e78" stroke-width="2" stroke-dasharray="6,8" opacity="0.6" />
          </svg>

          <!-- Rotating Radar Sweep Cone -->
          <div class="radar-cone-rotator">
            <svg width="900" height="900" viewBox="0 0 900 900">
              <defs>
                <linearGradient id="radarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#c34c45" stop-opacity="0.35" />
                  <stop offset="100%" stop-color="#c34c45" stop-opacity="0" />
                </linearGradient>
              </defs>
              <path d="M 450 450 L 900 450 A 450 450 0 0 1 768 768 Z" fill="url(#radarGrad)" />
              <circle cx="450" cy="450" r="440" fill="none" stroke="#c34c45" stroke-width="1.5" stroke-dasharray="8,6" opacity="0.4" />
            </svg>
          </div>

          <!-- Tactical Labels -->
          <div class="tactical-geo-label label-china">
            CHINA // 中国
            <span>EASTERN THEATER COMMAND (東部戦区)</span>
          </div>

          <div class="tactical-geo-label label-taiwan">
            TAIWAN // 台湾
            <span>CRITICAL ISLAND CORRIDOR</span>
          </div>

          <div class="tactical-geo-label label-median-line">
            MEDIAN LINE // 海峡中間線 (160 KM)
          </div>

          <!-- Hsinchu Target Reticle & Telemetry Callout -->
          <div class="hsinchu-beacon-rig" id="hsinchu-beacon">
            <div class="hsinchu-reticle-circle"></div>
            <div class="hsinchu-pulse-ring"></div>
            <div class="hsinchu-telemetry-panel" id="hsinchu-telemetry">
              <div class="telemetry-title">TARGET // 新竹サイエンスパーク</div>
              <div class="telemetry-coords">TSMC FAB 12 / 20 CLUSTER · 24°46'N 120°59'E</div>
              <div class="telemetry-stat">
                ◆ 最先端半導体の90%以上が集中 // 海岸線からわずか160km
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 01 -->
      <div class="subtitle-container clip" id="sub1" data-start="0.00" data-duration="8.42" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          もし明日、<span class="hl-gold">台湾海峡で戦争が勃発</span>し、たったひとつの企業が操業を停止したらどうなるでしょうか？
        </div>
      </div>
      <audio class="clip" id="vo-01" data-start="0.00" data-duration="8.42" data-track-index="3" src="assets/audio/scene_01.mp3"></audio>
      <audio class="clip" id="sfx-01-drone" data-start="0.00" data-duration="6.00" data-track-index="4" src="assets/sfx/sub_drone.wav"></audio>
      <audio class="clip" id="sfx-01-sonar" data-start="1.20" data-duration="2.00" data-track-index="5" src="assets/sfx/sonar_ping.wav"></audio>
      <audio class="clip" id="sfx-01-glitch" data-start="7.10" data-duration="0.30" data-track-index="6" src="assets/sfx/tactical_glitch.wav"></audio>

      <!-- ================= SCENE 02: DOMINO SUPPLY DISRUPTION (8.42s - 23.57s) ================= -->
      <div class="scene02-stage clip" id="scene02-stage" data-start="8.42" data-duration="15.15" data-track-index="1" data-layout-allow-overflow>
        <!-- Centerpiece Silicon Die -->
        <div class="scene02-die" id="scene02-die">
          <img src="assets/images/silicon_wafer_vintage.jpg" alt="TSMC Advanced Silicon Die" />
          <div class="die-chip-label">TSMC 3NM CORE</div>
        </div>

        <!-- Glowing Circuit Conduit Lines -->
        <svg class="scene02-svg-conduit" viewBox="0 0 1600 100">
          <line x1="800" y1="0" x2="270" y2="100" stroke="#315e78" stroke-width="3" stroke-dasharray="8,6" />
          <line x1="800" y1="0" x2="800" y2="100" stroke="#315e78" stroke-width="3" stroke-dasharray="8,6" />
          <line x1="800" y1="0" x2="1330" y2="100" stroke="#315e78" stroke-width="3" stroke-dasharray="8,6" />
        </svg>

        <!-- 3 Domino Sectors Row -->
        <div class="scene02-domino-row">
          <!-- Sector 1: Smartphones -->
          <div class="domino-column" id="sector-phone">
            <div class="domino-sector-tag">SECTOR 01 // CONSUMER TECH</div>
            <div class="domino-title">SMARTPHONES</div>
            <div class="domino-desc">Apple iPhone (A18 Pro) · Qualcomm Snapdragon 8<br/>世界中の最新スマートフォン生産ラインが完全停止</div>
            <div class="domino-alert-pill">STATUS: 70% GLOBAL SUPPLY HALTED</div>
          </div>

          <!-- Sector 2: AI & Accelerators -->
          <div class="domino-column" id="sector-ai">
            <div class="domino-sector-tag">SECTOR 02 // ARTIFICIAL INTELLIGENCE</div>
            <div class="domino-title">AI ACCELERATORS</div>
            <div class="domino-desc">NVIDIA H100 / Blackwell · AMD Instinct MI300<br/>全フロンティアAIモデルの学習・開発が全世界で凍結</div>
            <div class="domino-alert-pill">STATUS: 90% AI COMPUTE COLLAPSED</div>
          </div>

          <!-- Sector 3: Data Centers -->
          <div class="domino-column" id="sector-cloud">
            <div class="domino-sector-tag">SECTOR 03 // GLOBAL INFRASTRUCTURE</div>
            <div class="domino-title">DATA CENTERS</div>
            <div class="domino-desc">AWS · Microsoft Azure · Google Cloud<br/>世界金融・防衛・基幹通信インフラが連鎖沈黙</div>
            <div class="domino-alert-pill">STATUS: GLOBAL GRID SILENCED</div>
          </div>
        </div>

        <!-- Global Economic Loss Ticker -->
        <div class="scene02-ticker" id="scene02-ticker">
          <div class="ticker-lbl">GLOBAL ECONOMIC CATASTROPHE:</div>
          <div class="ticker-val">-10,000,000,000,000 USD (年間1500兆円の損失)</div>
        </div>
      </div>

      <!-- Subtitle 02 -->
      <div class="subtitle-container clip" id="sub2" data-start="8.42" data-duration="15.15" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          あなたの手元のスマートフォンは製造不能になり、<span class="hl-cyan">全世界のAI開発は完全凍結</span>。データセンターは沈黙し、世界経済は数週間で<span class="hl-danger">数千兆円の壊滅的打撃</span>を受けます。
        </div>
      </div>
      <audio class="clip" id="vo-02" data-start="8.42" data-duration="15.15" data-track-index="3" src="assets/audio/scene_02.mp3"></audio>
      <audio class="clip" id="sfx-02-impact" data-start="8.60" data-duration="2.50" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SCENE 03: TSMC REVEAL & VOX 90% GAUGE (23.57s - 39.58s) ================= -->
      <div class="scene03-split-stage clip" id="scene03-stage" data-start="23.57" data-duration="16.01" data-track-index="1" data-layout-allow-overflow>
        <!-- Left: Glowing 90% Donut Gauge -->
        <div class="scene03-donut-box" id="scene03-donut">
          <div class="gauge-svg-wrap">
            <svg width="280" height="280" viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="42" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="11" />
              <circle id="vox-donut-arc" cx="50" cy="50" r="42" fill="none" stroke="#e5bb54" stroke-width="11"
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
        <div class="scene03-bars-box" id="scene03-bars">
          <!-- TSMC -->
          <div class="bar-row-card" style="border-left: 6px solid var(--info-yellow);">
            <div class="bar-row-head">
              <div class="bar-row-name">TSMC（台湾積体電路製造）</div>
              <div class="bar-row-val" style="color: var(--info-yellow);">90.0%</div>
            </div>
            <div class="bar-track">
              <div class="bar-fill" id="fill-tsmc" style="background: var(--info-yellow);"></div>
            </div>
            <div class="bar-note">Apple A18/M4、NVIDIA Blackwell、AMD Zen5の全量を受託</div>
          </div>

          <!-- Samsung -->
          <div class="bar-row-card" style="border-left: 6px solid var(--tech-blue);">
            <div class="bar-row-head">
              <div class="bar-row-name">SAMSUNG FOUNDRY</div>
              <div class="bar-row-val" style="color: #64b5f6;">8.0%</div>
            </div>
            <div class="bar-track">
              <div class="bar-fill" id="fill-samsung" style="background: var(--tech-blue);"></div>
            </div>
            <div class="bar-note">先端プロセスの歩留まり課題に直面・自社向け優先</div>
          </div>

          <!-- Intel & Others -->
          <div class="bar-row-card" style="border-left: 6px solid #64748b;">
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

      <!-- Subtitle 03 -->
      <div class="subtitle-container clip" id="sub3" data-start="23.57" data-duration="16.01" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          その企業の名前は、<span class="hl-gold">TSMC（台湾積体電路製造）</span>。世界の先端半導体の90％以上を独占する、人類史上最も危険で、最も不可欠な<span class="hl-cyan">「チョークポイント（急所）」</span>です。
        </div>
      </div>
      <audio class="clip" id="vo-03" data-start="23.57" data-duration="16.01" data-track-index="3" src="assets/audio/scene_03.mp3"></audio>
      <audio class="clip" id="sfx-03-marker" data-start="24.00" data-duration="1.50" data-track-index="4" src="assets/sfx/marker_wipe.wav"></audio>

      <!-- ================= SCENE 04: JAPAN KUMAMOTO JASM & 93YO MORRIS CHANG (39.58s - 59.09s) ================= -->
      <div class="scene04-stage clip" id="scene04-stage" data-start="39.58" data-duration="19.51" data-track-index="1" data-layout-allow-overflow>
        <!-- Floating 1.2 Trillion Yen Subsidy Badge -->
        <div class="subsidy-badge-banner" id="scene04-subsidy-badge">
          <div class="subsidy-badge-text">日本政府 異例の巨額補助金 // 1兆2000億円投下</div>
        </div>

        <!-- Left: Kumamoto Fab Landscape -->
        <div class="scene04-card" id="scene04-card-fab">
          <div class="card-photo-frame">
            <img src="assets/images/mount_aso_vintage.jpg" alt="Kumamoto Kikuyo JASM Fab Landscape" />
          </div>
          <div class="card-info-box">
            <div class="card-kicker">KUMAMOTO, JAPAN // 2024年2月開所</div>
            <div class="card-heading">JASM 熊本第1工場</div>
            <div class="card-desc">
              のどかなキャベツ畑の真ん中に突如現れた巨大半導体拠点。<br/>
              ソニー・デンソーとの合弁により、日本のサプライチェーンを再構築。
            </div>
          </div>
        </div>

        <!-- Right: 93-Year-Old Morris Chang Portrait (Uncropped) -->
        <div class="scene04-card" id="scene04-card-morris">
          <div class="card-photo-frame">
            <img src="assets/images/morris_chang_93yo.jpg" alt="Morris Chang at Kumamoto Opening Ceremony" />
          </div>
          <div class="card-info-box">
            <div class="card-kicker">FOUNDER & VISIONARY // 93 YEARS OLD</div>
            <div class="card-heading">モリス・チャン（張忠謀）</div>
            <div class="card-desc">
              「日本と台湾の半導体協力は、新たなルネサンスをもたらす」。<br/>
              日本の政財界トップが深々と頭を下げた、半導体界の巨人。
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 04 -->
      <div class="subtitle-container clip" id="sub4" data-start="39.58" data-duration="19.51" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          2024年2月、日本の熊本県菊陽町。突如現れた巨大工場に、日本政府は異例の<span class="hl-gold">1兆2000億円を超える巨額補助金</span>を投じ、政財界のトップたちが<span class="hl-cyan">93歳の老人</span>に深々と頭を下げました。
        </div>
      </div>
      <audio class="clip" id="vo-04" data-start="39.58" data-duration="19.51" data-track-index="3" src="assets/audio/scene_04.mp3"></audio>
      <audio class="clip" id="sfx-04-impact" data-start="39.80" data-duration="2.50" data-track-index="4" src="assets/sfx/impact_boom.wav"></audio>

      <!-- ================= SCENE 05: 1987 FLASHBACK ARCHIVE DESK (59.09s - 82.27s) ================= -->
      <div class="scene05-stage clip" id="scene05-stage" data-start="59.09" data-duration="23.18" data-track-index="1" data-layout-allow-overflow>
        <img class="scene05-paper-bg" src="assets/images/clean_paper_bg.jpg" alt="Vintage Archival Paper Texture" />

        <!-- Reverse Timeline Header -->
        <div class="scene05-timeline-bar" id="scene05-timeline">
          <div class="timeline-step" id="t-2024">2024 熊本開所</div>
          <div class="timeline-step">◀ 2010 スマホ革命</div>
          <div class="timeline-step">◀ 1995 上場</div>
          <div class="timeline-step active" id="t-1987">● 1987 TSMC創業</div>
        </div>

        <!-- Archival Desk Dossier Cards -->
        <div class="scene05-content-row">
          <!-- Left: 55-Year-Old Morris Chang Portrait (Uncropped) -->
          <div class="scene05-card-left" id="card-morris-1987">
            <div class="scene05-photo-box">
              <img src="assets/images/morris_chang_1987.jpg" alt="Morris Chang in 1987 at age 55" />
            </div>
            <div class="archival-info-meta">
              <div class="archival-meta-title">モリス・チャン（当時55歳）</div>
              <div class="archival-meta-desc">
                米テキサス・インスツルメンツで出世街道を外れ、台湾政府の招聘で新竹へ渡った孤高のリーダー。
              </div>
            </div>
          </div>

          <!-- Right: Early 1987 Hsinchu Fab Factory -->
          <div class="scene05-card-right" id="card-fab-1987">
            <div class="archival-red-stamp">技術・資金・名声ゼロ</div>
            <div class="scene05-photo-box">
              <img src="assets/images/hsinchu_park_vintage.jpg" alt="1987 Early Hsinchu Factory Fab" />
            </div>
            <div class="archival-info-meta">
              <div class="archival-meta-title">1987年 新竹サイエンスパーク</div>
              <div class="archival-meta-desc">
                「誰も見向きもしない下請け町工場」。当時の最新鋭工場に比べ、製造技術は2〜3世代遅れていた。
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Subtitle 05 -->
      <div class="subtitle-container clip" id="sub5" data-start="59.09" data-duration="23.18" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          しかし、時計の針を37年前、1987年に戻してみてください。この会社は、<span class="hl-danger">技術なし、資金なし、名声なし</span>。55歳で台湾に渡った一人の男が立ち上げた<span class="hl-gold">「誰も見向きもしない下請け工場」</span>でした。
        </div>
      </div>
      <audio class="clip" id="vo-05" data-start="59.09" data-duration="23.18" data-track-index="3" src="assets/audio/scene_05.mp3"></audio>
      <audio class="clip" id="sfx-05-clock" data-start="59.20" data-duration="6.00" data-track-index="4" src="assets/sfx/clock_tick.wav"></audio>
      <audio class="clip" id="sfx-05-slap" data-start="60.50" data-duration="1.20" data-track-index="5" src="assets/sfx/paper_slap.wav"></audio>

      <!-- ================= SCENE 06: MONOLITHIC TITLE REVEAL (82.27s - 96.89s) ================= -->
      <div class="scene06-stage clip" id="scene06-stage" data-start="82.27" data-duration="14.62" data-track-index="1" data-layout-allow-overflow>
        <div class="title-kicker" id="s6-kicker">MAGNATESMEDIA × VOX DOCUMENTARY</div>
        <div class="monolithic-title" id="s6-title">TSMC</div>
        <div class="monolithic-subtitle" id="s6-sub">THE SEMICONDUCTOR EMPIRE</div>
        <div class="title-hero-tag" id="s6-tag">常識を覆し続けた男の狂気の逆転劇 — 1987-2024</div>
        <div class="title-clients-line" id="s6-clients">
          <span>APPLE</span> · <span>NVIDIA</span> · <span>AMD</span> · <span>QUALCOMM</span> · <span>ASML</span>
        </div>
      </div>

      <!-- Subtitle 06 -->
      <div class="subtitle-container clip" id="sub6" data-start="82.27" data-duration="14.62" data-track-index="2" data-layout-allow-overflow>
        <div class="subtitle-text" data-layout-ignore>
          なぜ、誰にも相手にされなかった町工場が、AppleやNVIDIA、そして米日すらひれ伏す怪物になれたのか？これは、<span class="hl-gold">常識を覆し続けた男の狂気の逆転劇</span>です。
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

      // ================= SCENE 01: SATELLITE GEOPOLITICAL MAP (0.00s - 8.42s) =================
      // Full-bleed initial 3D tactical camera: Scale 1.35 covers all edges completely!
      tl.set("#scene01-map-plane", {{
        transformPerspective: 1200,
        rotateX: 16,
        rotateY: -3,
        rotateZ: -5,
        scale: 1.35,
        x: 80,
        y: -30,
        z: -50
      }});

      // Beacon and Telemetry entrance
      tl.fromTo("#hsinchu-beacon", {{ scale: 0.4, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.8, ease: "back.out(1.8)" }}, 1.2);
      tl.fromTo("#hsinchu-telemetry", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 1.6);

      // Camera Dive towards Hsinchu Science Park (1.6s to 7.0s)
      tl.to("#scene01-map-plane", {{
        rotateX: 12,
        rotateY: -1,
        rotateZ: -2,
        scale: 2.25,
        x: -740,
        y: -280,
        z: 160,
        duration: 5.4,
        ease: "power2.inOut"
      }}, 1.6);

      // Controlled tactical glitch before transition
      tl.to("#glitch-overlay", {{ opacity: 0.85, duration: 0.08, yoyo: true, repeat: 3, ease: "rough" }}, 7.1);

      // ================= SCENE 02: DOMINO SUPPLY DISRUPTION (8.42s - 23.57s) =================
      tl.fromTo("#scene02-die", {{ scale: 0.7, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.6, ease: "back.out(1.5)" }}, 8.6);
      
      // Cascading Domino Columns
      tl.fromTo("#sector-phone", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.2);
      tl.fromTo("#sector-ai", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 9.7);
      tl.fromTo("#sector-cloud", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 10.2);

      // Domino Disruption triggers
      tl.to("#sector-phone", {{ className: "+=disrupted" }}, 12.5);
      tl.to("#sector-ai", {{ className: "+=disrupted" }}, 14.5);
      tl.to("#sector-cloud", {{ className: "+=disrupted" }}, 16.5);

      // Global Loss Ticker
      tl.fromTo("#scene02-ticker", {{ scale: 0.9, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, 17.5);

      // ================= SCENE 03: TSMC REVEAL & VOX 90% GAUGE (23.57s - 39.58s) =================
      tl.fromTo("#scene03-donut", {{ x: -50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 23.8);
      tl.fromTo("#scene03-bars", {{ x: 50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 24.1);

      // Animate Radial Donut Gauge (stroke-dashoffset from 264 to 26.4 for 90%)
      tl.fromTo("#vox-donut-arc", {{ strokeDashoffset: 264 }}, {{ strokeDashoffset: 26.4, duration: 1.4, ease: "power3.out" }}, 24.3);

      // Animate Bar Charts
      tl.to("#fill-tsmc", {{ width: "90%", duration: 1.2, ease: "power2.out" }}, 24.6);
      tl.to("#fill-samsung", {{ width: "8%", duration: 0.8, ease: "power2.out" }}, 25.2);
      tl.to("#fill-intel", {{ width: "2%", duration: 0.6, ease: "power2.out" }}, 25.5);

      // ================= SCENE 04: JAPAN KUMAMOTO JASM & 93YO MORRIS CHANG (39.58s - 59.09s) =================
      tl.fromTo("#scene04-subsidy-badge", {{ y: -30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "back.out(1.6)" }}, 39.8);
      tl.fromTo("#scene04-card-fab", {{ x: -50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 40.2);
      tl.fromTo("#scene04-card-morris", {{ x: 50, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, 40.6);

      // Slow cinematic push-in on Morris Chang 93yo
      tl.to("#scene04-card-morris .card-photo-frame img", {{ scale: 1.06, duration: 16.0, ease: "none" }}, 41.0);

      // ================= SCENE 05: 1987 FLASHBACK ARCHIVE DESK (59.09s - 82.27s) =================
      tl.fromTo("#scene05-timeline", {{ y: -20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 59.3);
      tl.fromTo("#card-morris-1987", {{ y: 40, opacity: 0, rotation: -2 }}, {{ y: 0, opacity: 1, rotation: -1, duration: 0.6, ease: "power2.out" }}, 59.8);
      tl.fromTo("#card-fab-1987", {{ y: 40, opacity: 0, rotation: 2 }}, {{ y: 0, opacity: 1, rotation: 1, duration: 0.6, ease: "power2.out" }}, 60.3);
      tl.fromTo(".archival-red-stamp", {{ scale: 1.8, opacity: 0, rotation: -25 }}, {{ scale: 1.0, opacity: 1, rotation: -12, duration: 0.4, ease: "back.out(2.0)" }}, 61.0);

      // ================= SCENE 06: MONOLITHIC TITLE REVEAL (82.27s - 96.89s) =================
      tl.fromTo("#s6-kicker", {{ y: -20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power2.out" }}, 82.5);
      tl.fromTo("#s6-title", {{ scale: 1.3, opacity: 0, filter: "blur(14px)" }}, {{ scale: 1.0, opacity: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }}, 82.8);
      tl.fromTo("#s6-sub", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 83.4);
      tl.fromTo("#s6-tag", {{ scale: 0.95, opacity: 0 }}, {{ scale: 1.0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 83.8);
      tl.fromTo("#s6-clients", {{ y: 15, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 84.4);

      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open("demo-tsmc-v2/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Generated demo-tsmc-v2/index.html adhering 100% to Master Production Brief Act 1!")
