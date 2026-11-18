import json
import os

with open("assets_tsmc/scenes_manifest.json", "r", encoding="utf-8") as f:
    scenes = json.load(f)

# Select Act 1 (Scenes 1 - 6)
act1_scenes = [s for s in scenes if s["act"] == 1]

# Calculate timing
current_time = 0.0
scene_timings = []
for s in act1_scenes:
    dur = s["duration"]
    scene_timings.append({
        "scene": s,
        "start": current_time,
        "duration": dur
    })
    current_time += dur

total_duration = current_time
print(f"Act 1 Total Duration: {total_duration:.2f}s")

# Mapping metadata for Act 1 using the 3-Zone Modular HUD (WW1 / NHK Documentary Standard)
scene_meta = {
    1: {
        "chapter": "序章 // 台湾海峡有事",
        "title": "台湾海峡の危機「世界が止まる日」",
        "subtitle": "新竹サイエンスパーク 24°48'N 120°59'E // 警戒レベル：DEFCON 1",
        "ref_code": "REF-01",
        "ref_title": "CHOKEPOINT ANALYSIS",
        "stamp": "TOP SECRET",
        "ribbon": "◆ 台湾海峡有事 ── 最先端半導体の90%を生み出す新竹サイエンスパークの危機"
    },
    2: {
        "chapter": "第1章 // 被害試算",
        "title": "世界経済損失10兆ドルのシミュレーション",
        "subtitle": "TSMC操業停止がもたらす世界同時麻痺 // 被害額：年間1500兆円の消失",
        "ref_code": "REF-02",
        "ref_title": "CRISIS MATRIX 2024",
        "left": "assets/images/crisis_matrix_dossier.jpg",
        "stamp": "SIMULATION",
        "ribbon": "◆ 台湾海峡有事の試算 ── TSMC停止時の世界経済損失：推計年間10兆ドル（約1500兆円）／ 世界のAI・スマホが完全麻痺"
    },
    3: {
        "chapter": "第2章 // 急所の独占",
        "title": "最先端3nm/2nm世界シェア90%の独占",
        "subtitle": "ASML極端紫外線(EUV)露光装置 · 1台350億円 // 人類史上最も危険なチョークポイント",
        "ref_code": "REF-03",
        "ref_title": "SUB-3NM MONOPOLY",
        "left": "assets/images/chokepoint_90pct_blueprint.jpg",
        "stamp": "90% 独占",
        "ribbon": "◆ 究極の急所 ── 最先端3nm/2nmの90%以上をTSMCが独占・Apple A18 / NVIDIA Blackwellの全量を受託"
    },
    4: {
        "chapter": "第3章 // 国家の跪き",
        "title": "日本政府の巨額補助金：1.2兆円の決断",
        "subtitle": "2024年2月 熊本・菊陽町 JASM第1工場開所 // 国家が93歳の老人に頭を下げた日",
        "ref_code": "REF-04",
        "ref_title": "METI STRATEGY 2024",
        "left": "assets/images/morris_chang_93yo_framed_720x455.jpg",
        "caption_left": "創業者モリス・チャン（93歳）",
        "right": "assets/images/mount_aso_vintage.jpg",
        "caption_right": "熊本・阿蘇山麓 JASM第1工場",
        "stamp": "1.2 TRILLION ¥",
        "ribbon": "【熊本 JASM第1工場】総投資額 1.2兆円 / 日本政府支援 4,760億円 ── 国家が93歳の老人に頭を下げた日"
    },
    5: {
        "chapter": "第4章 // 1987年の賭け",
        "title": "1987年 新竹の片隅「資本ゼロ・名声ゼロ」の町工場",
        "subtitle": "設立時・55歳モリス・チャンの孤立無援の挑戦 // 世界初「純粋受託製造」の誕生",
        "ref_code": "REF-05",
        "ref_title": "FOUNDING DOSSIER",
        "left": "assets/images/morris_chang_1987_framed_1070x480.jpg",
        "caption_left": "1987年設立時 · 55歳の挑戦",
        "stamp": "FOUNDING 1987",
        "ribbon": "◆ 1987年 新竹 ── 資本ゼロ・名声ゼロから始まった世界初「純粋受託製造（ファウンドリ）」の挑戦"
    },
    6: {
        "chapter": "第5章 // 巨人の衝突",
        "title": "IDM 対 ファウンドリ「持たざる者」への武器",
        "subtitle": "インテルCEO アンディ・グローブ 対 TSMC モリス・チャン // 半導体民主化の夜明け",
        "ref_code": "REF-06",
        "ref_title": "PARADIGM SHIFT",
        "left": "assets/images/andy_grove_vintage.jpg",
        "caption_left": "インテルCEO アンディ・グローブ",
        "right": "assets/images/morris_chang_1987_framed_720x455.jpg",
        "caption_right": "受託製造の祖 モリス・チャン",
        "stamp": "PARADIGM SHIFT",
        "ribbon": "◆ ファウンドリモデル誕生 ── 「工場を持たない天才たち」に武器を与えた半導体の民主化"
    }
}

sfx_map = {
    1: {"file": "assets/sfx/sub_drone.wav", "dur": 0.8},
    2: {"file": "assets/sfx/paper_slap.wav", "dur": 0.5},
    3: {"file": "assets/sfx/marker_wipe.wav", "dur": 0.4},
    4: {"file": "assets/sfx/impact_boom.wav", "dur": 0.8},
    5: {"file": "assets/sfx/clock_tick.wav", "dur": 0.3},
    6: {"file": "assets/sfx/impact_boom.wav", "dur": 0.8}
}

html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>【完全解説】18分でわかるTSMCの全歴史 - 第1幕 (Drama-Doc)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&family=Montserrat:ital,wght@0,700;1,700;1,900&family=Noto+Serif+JP:wght@600;700;900&family=Oswald:wght@600;700&display=swap"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>

    <style>
      :root {{
        --yellow-hl: #f0a500;
        --dark-paper: #161513;
        --dark-box: #1b1916;
        --stamp-red: #c0392b;
        --hud-red: #ff3333;
        --font-headline: 'Oswald', 'Noto Serif JP', sans-serif;
        --font-archival: 'Courier Prime', 'Courier New', monospace;
      }}

      * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }}

      body {{
        background-color: #0b0a09;
        font-family: var(--font-headline);
        overflow: hidden;
        margin: 0;
      }}

      #root {{
        width: 1920px;
        height: 1080px;
        position: relative;
        background: #141311;
        overflow: hidden;
        user-select: none;
      }}

      .clip {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }}

      .bg-img {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: sepia(22%) contrast(1.10) brightness(0.96);
      }}

      .vignette-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, rgba(0,0,0,0) 45%, rgba(40,30,18,0.3) 80%, rgba(18,12,6,0.55) 100%);
        mix-blend-mode: multiply;
        z-index: 85;
      }}

      .scene-stage {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        transform-origin: 50% 48%;
        will-change: transform;
      }}

      /* ================= 10s HOOK HUD ================= */
      .hook-video-layer {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        object-fit: cover;
        filter: contrast(1.18) brightness(0.92);
        z-index: 60;
      }}

      .hook-hud-container {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        z-index: 65;
        pointer-events: none;
        background: radial-gradient(circle at 50% 50%, rgba(0,0,0,0.15) 30%, rgba(0,0,0,0.7) 100%);
      }}

      .cinematic-bar-top {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 75px;
        background: #000;
        z-index: 70;
      }}

      .cinematic-bar-bottom {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 75px;
        background: #000;
        z-index: 70;
      }}

      .hook-alert-tag {{
        position: absolute;
        top: 110px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(220, 20, 20, 0.9);
        color: #fff;
        font-family: 'Oswald', sans-serif;
        font-size: 24px;
        font-weight: 700;
        letter-spacing: 5px;
        padding: 6px 28px;
        border-radius: 2px;
        box-shadow: 0 0 25px rgba(255, 0, 0, 0.7);
        text-transform: uppercase;
      }}

      .hook-title-block {{
        position: absolute;
        top: 420px;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 1600px;
      }}

      .hook-title-main {{
        font-family: 'Oswald', 'Noto Serif JP', sans-serif;
        font-size: 92px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 6px;
        text-shadow: 0 10px 40px rgba(0,0,0,0.9), 0 0 30px rgba(255,50,50,0.6);
        line-height: 1.1;
        margin-bottom: 16px;
      }}

      .hook-title-sub {{
        font-family: 'Noto Serif JP', serif;
        font-size: 38px;
        font-weight: 700;
        color: #f5d061;
        letter-spacing: 3px;
        text-shadow: 0 6px 20px rgba(0,0,0,0.9);
      }}

      .radar-crosshair {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        border: 2px dashed rgba(255, 60, 60, 0.35);
        border-radius: 50%;
        pointer-events: none;
      }}

      /* ================= 3-ZONE MODULAR HUD: ZONE 1 (TOP-LEFT CONTEXT ANCHOR) ================= */
      .doc-header-anchor {{
        position: absolute;
        top: 34px;
        left: 60px;
        z-index: 35;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        pointer-events: none;
      }}

      .doc-header-row {{
        display: flex;
        align-items: center;
        gap: 14px;
      }}

      .doc-chapter-pill {{
        background: #c0392b;
        color: #ffffff;
        font-family: 'Oswald', sans-serif;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 3px 12px;
        border-radius: 2px;
        text-transform: uppercase;
        box-shadow: 0 2px 8px rgba(192, 57, 43, 0.4);
      }}

      .doc-header-title {{
        font-family: 'Noto Serif JP', serif;
        font-size: 36px;
        font-weight: 900;
        color: #14110e;
        letter-spacing: 1.5px;
        line-height: 1.1;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.9);
      }}

      .doc-header-sub {{
        margin-top: 6px;
        font-family: 'Courier Prime', 'Noto Serif JP', monospace;
        font-size: 17px;
        font-weight: 700;
        color: #5c4e3e;
        letter-spacing: 1.2px;
        display: flex;
        align-items: center;
        gap: 8px;
      }}

      .doc-header-sub::before {{
        content: "";
        display: inline-block;
        width: 14px;
        height: 3px;
        background: #c0392b;
      }}

      /* ================= 3-ZONE MODULAR HUD: ZONE 3 (TOP-RIGHT METADATA CLASSIFICATION) ================= */
      .doc-meta-badge {{
        position: absolute;
        top: 34px;
        right: 60px;
        z-index: 35;
        background: rgba(20, 18, 16, 0.94);
        border: 1px solid #3d3529;
        border-right: 4px solid var(--yellow-hl);
        padding: 6px 18px;
        color: #e5ded2;
        font-family: 'Courier Prime', monospace;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 2px;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.45);
        border-radius: 2px;
      }}

      /* ================= HIGH-TECH DUAL CONTAINERS (SCENE 2 & 3) ================= */
      .tech-split-container {{
        position: absolute;
        top: 155px;
        left: 60px;
        width: 1800px;
        height: 605px;
        display: flex;
        justify-content: space-between;
        z-index: 15;
      }}

      .tech-frame-left {{
        width: 875px;
        height: 595px;
        position: relative;
        border-radius: 4px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.65);
      }}

      .tech-frame-right {{
        width: 875px;
        height: 595px;
        position: relative;
        background: #0a0e14;
        border-radius: 4px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.65);
        overflow: hidden;
      }}

      .tech-caption-bar {{
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        background: rgba(14, 18, 24, 0.95);
        border-top: 1px solid rgba(255,255,255,0.12);
        color: #d0dbe5;
        font-family: var(--font-archival);
        font-size: 19px;
        font-weight: 700;
        letter-spacing: 1.5px;
        padding: 8px 18px;
        text-align: center;
        z-index: 26;
      }}

      /* Dedicated Top-level Live Video (Scene 2 & 3) */
      .tech-live-video {{
        position: absolute;
        top: 155px;
        left: 985px;
        width: 875px;
        height: 550px;
        object-fit: cover;
        z-index: 20;
        border-radius: 4px 4px 0 0;
      }}

      .cctv-hud {{
        position: absolute;
        top: 155px;
        left: 985px;
        width: 875px;
        height: 550px;
        pointer-events: none;
        z-index: 25;
        overflow: hidden;
        border-radius: 4px 4px 0 0;
      }}

      .cctv-rec-dot {{
        position: absolute;
        top: 14px;
        left: 18px;
        color: #ff3b30;
        font-family: 'Oswald', sans-serif;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 2px;
        text-shadow: 0 0 12px rgba(255, 59, 48, 0.95);
      }}

      .cctv-cam-id {{
        position: absolute;
        top: 14px;
        right: 18px;
        color: #38ef7d;
        font-family: 'Oswald', sans-serif;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(56, 239, 125, 0.8);
      }}

      .cctv-scanlines {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: repeating-linear-gradient(rgba(0,0,0,0) 0px, rgba(0,0,0,0) 2px, rgba(0,0,0,0.24) 3px, rgba(0,0,0,0.24) 4px);
        pointer-events: none;
      }}

      .cctv-crosshair {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90px;
        height: 90px;
        border: 1px dashed rgba(99, 154, 209, 0.45);
        border-radius: 50%;
        pointer-events: none;
      }}

      /* ================= ARCHIVAL MAT & POLAROID (SCENE 4, 5, 6) ================= */
      .folder-mat {{
        position: absolute;
        background: #e8e0cc;
        border: 2px dashed #b5a990;
        box-shadow: 0 25px 60px rgba(0,0,0,0.55), inset 0 0 25px rgba(120,95,50,0.18);
        border-radius: 4px;
        z-index: 10;
        pointer-events: none;
      }}

      .folder-tab {{
        position: absolute;
        top: -24px;
        left: 30px;
        background: #d4c8b0;
        color: #4a4030;
        font-family: var(--font-archival);
        font-size: 15px;
        font-weight: 700;
        padding: 4px 18px;
        border: 1px solid #b5a990;
        border-bottom: none;
        border-radius: 4px 4px 0 0;
        letter-spacing: 1.5px;
      }}

      .scrapbook-card {{
        position: absolute;
        background: #f7f3ea;
        padding: 14px 14px 34px 14px;
        box-shadow: 0 22px 50px rgba(0,0,0,0.58), inset 0 0 15px rgba(130,100,60,0.14);
        border: 1px solid #dcd4c0;
        border-radius: 3px;
        z-index: 15;
        display: flex;
        flex-direction: column;
        align-items: center;
        transform-origin: center center;
        will-change: transform, opacity;
      }}

      .scrapbook-card img {{
        display: block;
        object-fit: cover;
        border: 1px solid rgba(0,0,0,0.15);
      }}

      .photo-caption {{
        font-family: var(--font-archival);
        font-size: 21px;
        font-weight: 700;
        color: #2b251d;
        letter-spacing: 1.5px;
        margin-top: 12px;
        text-transform: uppercase;
      }}

      .tape {{
        position: absolute;
        width: 140px;
        height: 38px;
        background: rgba(220, 204, 168, 0.82);
        box-shadow: 0 2px 7px rgba(50,35,15,0.32);
        backdrop-filter: blur(1.5px);
        z-index: 22;
      }}

      .tape-tl {{ top: -16px; left: -30px; transform: rotate(-25deg); }}
      .tape-tr {{ top: -16px; right: -30px; transform: rotate(25deg); }}
      .tape-bl {{ bottom: -14px; left: -26px; transform: rotate(20deg); }}
      .tape-br {{ bottom: -14px; right: -26px; transform: rotate(-20deg); }}

      .archival-stamp {{
        position: absolute;
        border: 4px double var(--stamp-red);
        color: var(--stamp-red);
        font-family: 'Oswald', sans-serif;
        font-size: 25px;
        font-weight: 700;
        letter-spacing: 3px;
        padding: 6px 18px;
        text-transform: uppercase;
        border-radius: 4px;
        box-shadow: 0 4px 10px rgba(192,57,43,0.3);
        mix-blend-mode: multiply;
        z-index: 28;
        transform-origin: center center;
        opacity: 0.95;
        background: rgba(247, 243, 234, 0.55);
        backdrop-filter: blur(1px);
      }}

      .data-ribbon {{
        position: absolute;
        top: 785px;
        left: 50%;
        transform: translateX(-50%);
        width: 1780px;
        background: #1e1b17;
        border-left: 6px solid var(--yellow-hl);
        border-right: 6px solid var(--yellow-hl);
        color: #f0e6d2;
        font-family: 'Noto Serif JP', serif;
        font-size: 22px;
        font-weight: 700;
        letter-spacing: 1.5px;
        padding: 10px 24px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.65);
        z-index: 30;
        white-space: nowrap;
      }}

      /* Titan Confrontation Divider (Scene 6) */
      .versus-divider {{
        position: absolute;
        top: 172px;
        left: 50%;
        transform: translateX(-50%);
        width: 140px;
        height: 550px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        z-index: 25;
      }}

      .versus-badge {{
        background: #c0392b;
        color: #fff;
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 900;
        letter-spacing: 4px;
        padding: 8px 18px;
        border-radius: 4px;
        box-shadow: 0 0 25px rgba(255,0,0,0.7);
      }}

      .versus-text {{
        color: #f5d061;
        font-family: var(--font-headline);
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 2px;
        margin-top: 8px;
        text-align: center;
      }}

      /* ================= INTERACTIVE TIME-JUMP OVERLAY (VOX MOTIF) ================= */
      .time-jump-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 1080px;
        z-index: 75;
        pointer-events: none;
        overflow: hidden;
      }}

      .time-jump-backdrop {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle at 50% 50%, rgba(20, 18, 16, 0.90) 0%, rgba(10, 9, 8, 0.97) 100%);
      }}

      .time-jump-hud {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 1600px;
        display: flex;
        flex-direction: column;
        align-items: center;
        transform-origin: 15% 50%;
      }}

      .time-jump-header {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 50px;
      }}

      .time-jump-badge {{
        background: #c0392b;
        color: #fff;
        font-family: 'Oswald', sans-serif;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 4px;
        padding: 4px 18px;
        border-radius: 2px;
        box-shadow: 0 0 20px rgba(192, 57, 43, 0.6);
        margin-bottom: 12px;
      }}

      .time-jump-title {{
        font-family: 'Noto Serif JP', 'Oswald', serif;
        font-size: 46px;
        font-weight: 900;
        color: #f5f0e1;
        letter-spacing: 3px;
        text-shadow: 0 4px 18px rgba(0,0,0,0.8);
      }}

      .timeline-ruler {{
        position: relative;
        width: 1400px;
        height: 120px;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }}

      .ruler-line {{
        position: absolute;
        top: 50%;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #f0a500 0%, #a89f91 40%, #e74c3c 100%);
        box-shadow: 0 0 14px rgba(240, 165, 0, 0.5);
        transform: translateY(-50%);
      }}

      .timeline-node {{
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
        z-index: 10;
      }}

      .node-dot {{
        width: 22px;
        height: 22px;
        background: #2b251d;
        border: 4px solid #a89f91;
        border-radius: 50%;
        box-shadow: 0 2px 10px rgba(0,0,0,0.7);
      }}

      .node-label {{
        position: absolute;
        bottom: 34px;
        font-family: 'Oswald', sans-serif;
        font-size: 32px;
        font-weight: 700;
        color: #dcd4c0;
        letter-spacing: 2px;
        text-shadow: 0 2px 6px rgba(0,0,0,0.8);
      }}

      .node-sublabel {{
        position: absolute;
        top: 34px;
        font-family: 'Noto Serif JP', serif;
        font-size: 17px;
        font-weight: 700;
        color: #8c806f;
        white-space: nowrap;
        letter-spacing: 1px;
      }}

      .node-2024 .node-dot {{
        border-color: #e74c3c;
        background: #fff;
        box-shadow: 0 0 16px rgba(231, 76, 60, 0.8);
      }}

      .node-2024 .node-label {{
        color: #ff6b6b;
      }}

      .node-tag {{
        position: absolute;
        top: 64px;
        background: rgba(231, 76, 60, 0.2);
        border: 1px solid #e74c3c;
        color: #ff8585;
        font-family: 'Oswald', sans-serif;
        font-size: 13px;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 2px;
        white-space: nowrap;
      }}

      .node-1987 .node-dot {{
        width: 28px;
        height: 28px;
        border-color: #f0a500;
        background: #14110e;
      }}

      .node-target-ring {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 64px;
        height: 64px;
        border: 2px dashed #f0a500;
        border-radius: 50%;
        opacity: 0;
        pointer-events: none;
      }}

      .node-callout {{
        position: absolute;
        bottom: 82px;
        background: var(--yellow-hl);
        color: #14110e;
        font-family: 'Oswald', sans-serif;
        font-size: 15px;
        font-weight: 800;
        letter-spacing: 2px;
        padding: 4px 12px;
        border-radius: 3px;
        white-space: nowrap;
        box-shadow: 0 4px 14px rgba(240, 165, 0, 0.6);
        opacity: 0;
        transform: translateY(6px);
      }}

      /* Animated Mouse Cursor */
      .mouse-cursor-container {{
        position: absolute;
        top: 0;
        left: 0;
        z-index: 100;
        pointer-events: none;
        filter: drop-shadow(0 4px 12px rgba(0,0,0,0.7));
      }}

      .cursor-click-ripple {{
        position: absolute;
        top: 2px;
        left: 4px;
        width: 32px;
        height: 32px;
        border: 3px solid #f0a500;
        border-radius: 50%;
        transform: scale(0);
        opacity: 0;
        pointer-events: none;
      }}

      /* ================= SUBTITLES (HIGH READABILITY FOR MOBILE) ================= */
      .subtitle-card {{
        position: absolute;
        top: auto !important;
        bottom: 24px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 1780px !important;
        min-height: 76px !important;
        height: auto !important;
        background: rgba(14, 12, 10, 0.94);
        border-left: 8px solid var(--yellow-hl);
        border-radius: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 10px 32px;
        z-index: 100;
        box-shadow: 0 18px 40px rgba(0,0,0,0.85);
        box-sizing: border-box;
      }}

      .subtitle-text {{
        font-family: 'Noto Serif JP', serif;
        font-size: 31px;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.4;
        text-align: center;
        letter-spacing: 1.2px;
        word-break: break-all;
        overflow-wrap: anywhere;
        white-space: normal;
        max-width: 1700px;
        margin: 0 auto;
        display: block;
        text-shadow: 0 2px 8px rgba(0,0,0,0.8);
      }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-width="1920" data-height="1080" data-duration="{total_duration:.2f}">
      <div class="vignette-overlay"></div>

      <!-- ================= 0s - 4.8s: HIGH-IMPACT TAIWAN STRAIT CINEMATIC VIDEO HOOK ================= -->
      <video class="clip hook-video-layer" id="hook-video" data-start="0.00" data-duration="4.80" data-track-index="10" src="assets/taiwan_strait_hook.mp4" muted playsinline></video>
      <div class="clip hook-hud-container" id="hook-hud" data-start="0.00" data-duration="4.80" data-track-index="11" data-layout-allow-overlap data-layout-allow-overflow>
        <div class="cinematic-bar-top" data-layout-ignore></div>
        <div class="cinematic-bar-bottom" data-layout-ignore></div>
        <div class="radar-crosshair" data-layout-ignore></div>
        <div class="hook-alert-tag" data-layout-allow-overlap>⚠ DEFCON 1 // TAIWAN STRAIT CRISIS</div>
        <div class="hook-title-block" data-layout-allow-overlap>
          <div class="hook-title-main" data-layout-allow-overlap>台湾海峡の危機</div>
          <div class="hook-title-sub" data-layout-allow-overlap>「もし明日、この海峡で戦争が始まったら──」</div>
        </div>
      </div>
"""

# Add top-level cleanroom live videos for Scene 2 & Scene 3 (NO underlying photo, 100% clean fit!)
s2 = scene_timings[1] # Scene 2
s3 = scene_timings[2] # Scene 3

html += f"""
      <!-- ================= SCENE 2 LIVE WAFER FAB CCTV SURVEILLANCE FEED (15.2s) ================= -->
      <video class="clip tech-live-video" id="live-vid-s2" data-start="{s2['start']:.2f}" data-duration="{s2['duration']:.2f}" data-track-index="12" src="assets/cleanroom_wafer_clip.mp4" muted playsinline style="filter: grayscale(100%) contrast(1.35) brightness(0.85) sepia(18%);"></video>
      <div class="clip cctv-hud" id="cctv-hud-s2" data-start="{s2['start']:.2f}" data-duration="{s2['duration']:.2f}" data-track-index="14" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
        <div class="cctv-scanlines" data-layout-ignore></div>
        <div class="cctv-rec-dot" data-layout-allow-overlap>● REC 00:14:22:08</div>
        <div class="cctv-cam-id" data-layout-allow-overlap>CAM-04 // HSINCHU FAB 12B</div>
      </div>

      <!-- ================= SCENE 3 LIVE ASML LITHO TECHNICAL SCANNER FEED (16.0s) ================= -->
      <video class="clip tech-live-video" id="live-vid-s3" data-start="{s3['start']:.2f}" data-duration="{s3['duration']:.2f}" data-track-index="13" src="assets/cleanroom_litho_clip.mp4" muted playsinline style="filter: grayscale(80%) contrast(1.3) brightness(0.9) sepia(12%);"></video>
      <div class="clip cctv-hud" id="cctv-hud-s3" data-start="{s3['start']:.2f}" data-duration="{s3['duration']:.2f}" data-track-index="15" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
        <div class="cctv-scanlines" data-layout-ignore></div>
        <div class="cctv-crosshair" data-layout-ignore></div>
        <div class="cctv-rec-dot" style="color: #639ad1;" data-layout-allow-overlap>⊕ ASML TWINSCAN EUV</div>
        <div class="cctv-cam-id" style="color: #f5d061;" data-layout-allow-overlap>13.5nm LASER PRECISION</div>
      </div>
"""

# Generate Scenes HTML with 3-Zone Modular HUD (WW1 / NHK Standard)
for idx, item in enumerate(scene_timings, 1):
    sc = item["scene"]
    start = item["start"]
    dur = item["duration"]
    meta = scene_meta.get(idx, {})
    sfx_info = sfx_map.get(idx, {})
    
    chapter_tag = meta.get("chapter", f"ACT 1 // CHAPTER {idx}")
    main_title = meta.get("title", "TSMC HISTORICAL DOSSIER")
    sub_title = meta.get("subtitle", "")
    ref_code = meta.get("ref_code", f"REF-{idx:02d}")
    ref_title = meta.get("ref_title", "ARCHIVE REPORT")
    ribbon_text = meta.get("ribbon", "")
    stamp_text = meta.get("stamp", "ARCHIVE")
    
    html += f"""
      <!-- ================= SCENE {idx}: Act {sc['act']} [{start:.2f}s - {start+dur:.2f}s] ================= -->
      <div id="scene{idx}" class="clip scene" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="1">
        <div id="s{idx}-stage" class="scene-stage">
          <img class="bg-img" src="assets/clean_paper_bg.jpg" alt="Vintage Paper" />

          <!-- Zone 1: Top-Left Contextual & Temporal Anchor -->
          <div class="doc-header-anchor" id="s{idx}-header" data-layout-allow-overlap data-layout-allow-overflow>
            <div class="doc-header-row">
              <span class="doc-chapter-pill">{chapter_tag}</span>
              <span class="doc-header-title">{main_title}</span>
            </div>
            <div class="doc-header-sub">
              {sub_title}
            </div>
          </div>

          <!-- Zone 3: Top-Right Archival Classification Badge -->
          <div class="doc-meta-badge" id="s{idx}-meta-badge" data-layout-ignore>
            <span style="color: var(--yellow-hl);">● {ref_code}</span>
            <span>{ref_title}</span>
          </div>
"""

    if idx == 1:
        # Scene 1: Expansive Tactical Satellite Map (1640px x 605px)
        html += f"""
          <!-- Tactical Satellite Map of Hsinchu Park -->
          <div class="tech-frame-left" id="s1-map" style="top: 155px; left: 140px; width: 1640px; height: 605px; background: #111; overflow: hidden; border: 2px solid #5a4e3e; box-shadow: 0 25px 60px rgba(0,0,0,0.7);" data-hold data-layout-allow-overflow>
            <img src="assets/images/hsinchu_park_vintage.jpg" style="width: 100%; height: 100%; object-fit: cover; filter: contrast(1.2) brightness(0.85);" alt="Hsinchu Satellite" />
            <div class="radar-crosshair" style="border-color: rgba(240, 165, 0, 0.4);" data-layout-ignore></div>
            <div class="cctv-scanlines" data-layout-ignore></div>
            <div class="tech-caption-bar" data-layout-ignore>新竹サイエンスパーク · 台湾海峡沿岸 24°48'N 120°59'E // 警戒レベル：DEFCON 1</div>
          </div>

          <!-- Rubber Stamp Accent -->
          <div class="archival-stamp" id="s1-stamp" style="top: 175px; left: 1520px; transform: rotate(8deg);" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <!-- Contextual Data Ribbon (Zone 2 bottom) -->
          <div class="data-ribbon" id="s1-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""
    elif idx == 2:
        # Scene 2: High-Tech War Room Matrix & CCTV Monitor
        html += f"""
          <div class="tech-split-container" id="s2-container">
            <!-- Left: Crisis Matrix Dossier -->
            <div class="tech-frame-left" id="s2-card-left" style="border: 2px solid #4a3e2e;" data-hold data-layout-allow-overflow>
              <img src="{meta['left']}" style="width: 100%; height: 550px; object-fit: contain; background: #161412;" alt="Crisis Matrix" />
              <div class="tech-caption-bar" data-layout-ignore>有事被害試算 · 世界ハイテク産業への致命的打撃</div>
            </div>

            <!-- Right: High-Tech Video Frame (Live Wafer Fab feed) -->
            <div class="tech-frame-right" id="s2-card-right" style="border: 2px solid #283747;" data-hold data-layout-allow-overflow>
              <div class="tech-caption-bar" data-layout-ignore>新竹サイエンスパーク · 24H自動搬送ライン [CAM-04]</div>
            </div>
          </div>

          <!-- Rubber Stamp Accent -->
          <div class="archival-stamp" id="s2-stamp" style="top: 175px; left: 740px; transform: rotate(-8deg); border-color: #e74c3c; color: #e74c3c;" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <!-- Contextual Data Ribbon -->
          <div class="data-ribbon" id="s2-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""
    elif idx == 3:
        # Scene 3: High-Tech Blueprint & ASML Laser Optics
        html += f"""
          <div class="tech-split-container" id="s3-container">
            <!-- Left: 90% Monopoly Blueprint -->
            <div class="tech-frame-left" id="s3-card-left" style="border: 2px solid #1c3550;" data-hold data-layout-allow-overflow>
              <img src="{meta['left']}" style="width: 100%; height: 550px; object-fit: contain; background: #0b1622;" alt="90% Blueprint" />
              <div class="tech-caption-bar" data-layout-ignore>最先端 3nm / 2nm プロセス世界供給比率 (CHOKEPOINT)</div>
            </div>

            <!-- Right: EUV Laser Frame (Live Optical Scanning feed) -->
            <div class="tech-frame-right" id="s3-card-right" style="border: 2px solid #1f3d5c;" data-hold data-layout-allow-overflow>
              <div class="tech-caption-bar" data-layout-ignore>ASML極端紫外線(EUV)露光装置 · 1台350億円 (独占心臓部)</div>
            </div>
          </div>

          <!-- Rubber Stamp Accent -->
          <div class="archival-stamp" id="s3-stamp" style="top: 175px; left: 740px; transform: rotate(6deg);" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <!-- Contextual Data Ribbon -->
          <div class="data-ribbon" id="s3-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""
    elif idx == 4:
        # Scene 4: Government Archival Manila Dossier (Dual cards)
        html += f"""
          <div class="folder-mat" id="s4-mat" style="top: 155px; left: 60px; width: 1800px; height: 605px; transform: rotate(-0.4deg);" data-hold data-layout-allow-overflow>
            <div class="folder-tab" data-layout-ignore data-layout-allow-occlusion>FILE REF: METI-SEMICONDUCTOR-STRATEGY-2024</div>
          </div>

          <!-- Left Photo Card: Morris Chang 93yo -->
          <div class="scrapbook-card" id="s4-card-left" style="top: 172px; left: 100px; transform: rotate(-1.5deg);" data-hold data-layout-allow-overflow>
            <div class="tape tape-tl"></div>
            <div class="tape tape-br"></div>
            <img src="{meta['left']}" width="720" height="455" alt="Morris Chang 93yo" style="object-fit: cover; object-position: center center;" />
            <div class="photo-caption" data-layout-ignore>{meta['caption_left']}</div>
          </div>

          <!-- Right Photo Card: Kumamoto Fab -->
          <div class="scrapbook-card" id="s4-card-right" style="top: 178px; left: 990px; transform: rotate(1.5deg);" data-hold data-layout-allow-overflow>
            <div class="tape tape-tr"></div>
            <div class="tape tape-bl"></div>
            <img src="{meta['right']}" width="720" height="455" alt="Kumamoto Fab" style="object-fit: cover; object-position: center center;" />
            <div class="photo-caption" data-layout-ignore>{meta['caption_right']}</div>
          </div>

          <!-- Rubber Stamp Accent -->
          <div class="archival-stamp" id="s4-stamp" style="top: 175px; left: 1560px; transform: rotate(10deg);" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <!-- Contextual Data Ribbon -->
          <div class="data-ribbon" id="s4-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""
    elif idx == 5:
        # Scene 5: 1987 Film Noir Flashback (Hero Single Card Centered) + Interactive Time-Jump Overlay
        html += f"""
          <!-- Interactive Time-Jump Overlay (Vox Motif: 2024 -> 1987) -->
          <div class="time-jump-overlay" id="time-jump-overlay" style="opacity: 0;" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            <div class="time-jump-backdrop"></div>
            <div class="time-jump-hud" id="time-jump-hud">
              <div class="time-jump-header">
                <div class="time-jump-badge">REWIND // 37 YEARS</div>
                <div class="time-jump-title">TIME REGRESSION: 2024 → 1987</div>
              </div>
              <div class="timeline-ruler">
                <div class="ruler-line"></div>
                
                <!-- Year 1980 Tick -->
                <div class="timeline-node" style="position: absolute; left: 6%;">
                  <div class="node-dot" style="width: 14px; height: 14px; border-width: 2px;"></div>
                  <div class="node-label" style="font-size: 20px; bottom: 25px; opacity: 0.6;">1980</div>
                </div>

                <!-- Year 1987 Target Node -->
                <div class="timeline-node node-1987" id="node-1987" style="position: absolute; left: 22%;">
                  <div class="node-callout" id="callout-1987">TSMC FOUNDING</div>
                  <div class="node-target-ring" id="ring-1987"></div>
                  <div class="node-dot"></div>
                  <div class="node-label" style="color: #f0a500; font-size: 38px; font-weight: 900;">1987</div>
                  <div class="node-sublabel">新竹・モリス・チャン</div>
                </div>

                <!-- Intermediate ticks (1995, 2005, 2015) -->
                <div class="timeline-node" style="position: absolute; left: 42%;">
                  <div class="node-dot" style="width: 14px; height: 14px; border-width: 2px;"></div>
                  <div class="node-label" style="font-size: 20px; bottom: 25px; opacity: 0.6;">1995</div>
                </div>
                <div class="timeline-node" style="position: absolute; left: 60%;">
                  <div class="node-dot" style="width: 14px; height: 14px; border-width: 2px;"></div>
                  <div class="node-label" style="font-size: 20px; bottom: 25px; opacity: 0.6;">2005</div>
                </div>
                <div class="timeline-node" style="position: absolute; left: 78%;">
                  <div class="node-dot" style="width: 14px; height: 14px; border-width: 2px;"></div>
                  <div class="node-label" style="font-size: 20px; bottom: 25px; opacity: 0.6;">2015</div>
                </div>

                <!-- Year 2024 Origin Node -->
                <div class="timeline-node node-2024" id="node-2024" style="position: absolute; left: 92%;">
                  <div class="node-dot"></div>
                  <div class="node-label">2024</div>
                  <div class="node-sublabel">熊本JASM工場 開所</div>
                  <div class="node-tag">PRESENT DAY</div>
                </div>
              </div>
            </div>

            <!-- Virtual Interactive OS Mouse Cursor -->
            <div class="mouse-cursor-container" id="time-jump-cursor" style="opacity: 0;">
              <svg width="38" height="38" viewBox="0 0 24 24" fill="none">
                <path d="M4 2L18 11.5L11.5 13L9 19.5L4 2Z" fill="#f5f0e1" stroke="#14110e" stroke-width="1.8" stroke-linejoin="round"/>
              </svg>
              <div class="cursor-click-ripple" id="cursor-ripple"></div>
            </div>
          </div>

          <div class="folder-mat" id="s5-mat" style="top: 155px; left: 300px; width: 1320px; height: 605px; transform: rotate(-0.6deg); background: #e3dac5;" data-hold data-layout-allow-overflow>
            <div class="folder-tab" data-layout-ignore data-layout-allow-occlusion>HISTORICAL ARCHIVE // 1987 FOUNDING REPORT</div>
          </div>

          <div class="scrapbook-card" id="s5-card-center" style="top: 172px; left: 350px; width: 1220px; transform: rotate(0.6deg);" data-hold data-layout-allow-overflow>
            <div class="tape tape-tl"></div>
            <div class="tape tape-tr"></div>
            <div class="tape tape-bl"></div>
            <div class="tape tape-br"></div>
            <img src="{meta['left']}" width="1160" height="485" alt="Morris Chang 1987" style="object-fit: cover; object-position: center center;" />
            <div class="photo-caption" data-layout-ignore>{meta['caption_left']}</div>
          </div>

          <div class="archival-stamp" id="s5-stamp" style="top: 180px; left: 1400px; transform: rotate(-7deg);" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <div class="data-ribbon" id="s5-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""
    elif idx == 6:
        # Scene 6: Titan Duel Showdown (Intel vs TSMC Face-off)
        html += f"""
          <!-- Left Photo Card: Intel CEO Andy Grove -->
          <div class="scrapbook-card" id="s6-card-left" style="top: 172px; left: 100px; transform: rotate(-1.5deg);" data-hold data-layout-allow-overflow>
            <div class="tape tape-tl"></div>
            <div class="tape tape-bl"></div>
            <img src="{meta['left']}" width="720" height="455" alt="Intel Andy Grove" style="object-fit: cover; object-position: center center;" />
            <div class="photo-caption" data-layout-ignore>{meta['caption_left']}</div>
          </div>

          <!-- Versus Divider -->
          <div class="versus-divider" id="s6-vs" data-layout-ignore>
            <div class="versus-badge">VS</div>
            <div class="versus-text">IDM 対 ファウンドリ</div>
          </div>

          <!-- Right Photo Card: Morris Chang -->
          <div class="scrapbook-card" id="s6-card-right" style="top: 172px; left: 1060px; transform: rotate(1.5deg);" data-hold data-layout-allow-overflow>
            <div class="tape tape-tr"></div>
            <div class="tape tape-br"></div>
            <img src="{meta['right']}" width="720" height="455" alt="TSMC Morris Chang" style="object-fit: cover; object-position: center center;" />
            <div class="photo-caption" data-layout-ignore>{meta['caption_right']}</div>
          </div>

          <div class="archival-stamp" id="s6-stamp" style="top: 175px; left: 1580px; transform: rotate(10deg);" data-layout-ignore data-layout-allow-overlap data-layout-allow-occlusion>
            {stamp_text}
          </div>

          <div class="data-ribbon" id="s6-ribbon" data-layout-ignore data-layout-allow-overlap>
            {ribbon_text}
          </div>
"""

    html += f"""
        </div>
      </div>

      <!-- Subtitle for Scene {idx} (31px bold, high readability) -->
      <div class="subtitle-card clip" id="sub{idx}" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="2" data-layout-allow-overlap data-layout-allow-occlusion>
        <div class="subtitle-text" data-layout-allow-overlap>
          {sc['vo']}
        </div>
      </div>

      <!-- Voiceover Audio for Scene {idx} -->
      <audio class="clip" id="vo-{idx}" data-start="{start:.2f}" data-duration="{dur:.2f}" data-track-index="3" src="assets/audio/scene_{idx:02d}.mp3"></audio>
"""
    if sfx_info:
        html += f"""      <!-- SFX for Scene {idx} -->
      <audio class="clip" id="sfx-{idx}" data-start="{start+0.15:.2f}" data-duration="{sfx_info['dur']}" data-track-index="{idx+3}" src="{sfx_info['file']}"></audio>
"""
    if idx == 5:
        html += f"""      <!-- SFX for Interactive Mouse Click in Scene 5 -->
      <audio class="clip" id="sfx-mouse-click" data-start="{start+4.22:.2f}" data-duration="0.35" data-track-index="18" src="assets/sfx/mouse_click.wav"></audio>
"""

html += f"""
      <!-- Master Cinematic Tension & Drama BGM Score (Continuous across full 96.89s) -->
      <audio class="clip" id="bgm-cinematic-score" data-start="0.00" data-duration="{total_duration:.2f}" data-track-index="25" src="assets/audio/act1_cinematic_score.mp3"></audio>
    </div>

    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});

      // ================= 0s - 4.8s: Cinematic Taiwan Strait Hook Animations =================
      tl.fromTo("#hook-hud .hook-alert-tag", {{ scale: 0.8, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, ease: "power2.out" }}, 0.2);
      tl.fromTo("#hook-hud .hook-title-main", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power3.out" }}, 0.4);
      tl.fromTo("#hook-hud .hook-title-sub", {{ y: 20, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, 0.8);
      
      // Pull back transition into dossier
      tl.to("#hook-video, #hook-hud", {{ opacity: 0, scale: 1.08, duration: 0.65, ease: "power2.inOut" }}, 4.15);
"""

# Generate GSAP animations with Ken Burns & Magnates Media Dynamic Punches
for idx, item in enumerate(scene_timings, 1):
    start = item["start"]
    dur = item["duration"]
    drift_x = -12 if idx % 2 == 1 else 12
    drift_y = -5 if idx % 3 == 0 else 5
    sc1_offset = 4.3 if idx == 1 else 0.0
    
    html += f"""
      // ================= Scene {idx} Animations ({start:.2f}s - {start+dur:.2f}s) =================
      // Continuous Ken Burns Micro-Drift (Eliminating frozen static frames)
      tl.fromTo("#s{idx}-stage", 
        {{ scale: 1.0, x: 0, y: 0 }}, 
        {{ scale: 1.045, x: {drift_x}, y: {drift_y}, duration: {dur:.2f}, ease: "none" }}, 
        {start:.2f}
      );

      // Top-Left Header entrance & Top-Right Meta Badge
      tl.fromTo("#s{idx}-header", {{ x: -35, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, {start + sc1_offset + 0.15:.2f});
      tl.fromTo("#s{idx}-meta-badge", {{ x: 35, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.5, ease: "power2.out" }}, {start + sc1_offset + 0.25:.2f});
"""

    if idx == 1:
        html += f"""      tl.fromTo("#s1-map", {{ y: -40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.65, ease: "power2.out" }}, {start + sc1_offset + 0.2:.2f});
      tl.fromTo("#s1-stamp", {{ scale: 2.8, opacity: 0, rotate: -25 }}, {{ scale: 1, opacity: 0.95, rotate: 8, duration: 0.42, ease: "back.out(2.2)" }}, {start + sc1_offset + 0.75:.2f});
      tl.fromTo("#s1-ribbon", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + sc1_offset + 0.85:.2f});
"""
    elif idx in [2, 3]:
        html += f"""      tl.fromTo("#s{idx}-container", {{ y: -35, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, {start + 0.2:.2f});
      tl.fromTo("#live-vid-s{idx}, #cctv-hud-s{idx}", {{ y: -35, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.6, ease: "power2.out" }}, {start + 0.2:.2f});
      tl.fromTo("#s{idx}-stamp", {{ scale: 2.6, opacity: 0, rotate: -25 }}, {{ scale: 1, opacity: 0.95, rotate: 6, duration: 0.42, ease: "back.out(2.2)" }}, {start + 0.75:.2f});
      tl.fromTo("#s{idx}-stage", {{ x: -3, y: 2 }}, {{ x: 0, y: 0, duration: 0.18, ease: "power1.out" }}, {start + 0.78:.2f});
      tl.fromTo("#s{idx}-ribbon", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + 0.85:.2f});
"""
        if idx == 2:
            html += f"""      // Camera push into crisis metrics at key moment
      tl.to("#s2-stage", {{ scale: 1.09, x: 40, y: -10, duration: 1.0, ease: "power2.inOut" }}, {start + 6.5:.2f});
"""
        elif idx == 3:
            html += f"""      // Camera push into 90% monopoly chart
      tl.to("#s3-stage", {{ scale: 1.09, x: 40, y: -10, duration: 1.0, ease: "power2.inOut" }}, {start + 6.0:.2f});
"""
    elif idx == 4:
        html += f"""      tl.fromTo("#s4-mat", {{ y: -30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: "power2.out" }}, {start + 0.2:.2f});
      tl.fromTo("#s4-card-left", {{ y: -65, scale: 0.92, opacity: 0, rotate: 0 }}, {{ y: 0, scale: 1, opacity: 1, rotate: -1.5, duration: 0.7, ease: "back.out(1.4)" }}, {start + 0.3:.2f});
      tl.fromTo("#s4-card-right", {{ y: -65, scale: 0.92, opacity: 0, rotate: 0 }}, {{ y: 0, scale: 1, opacity: 1, rotate: 1.5, duration: 0.7, ease: "back.out(1.4)" }}, {start + 0.5:.2f});
      tl.fromTo("#scene4 .tape", {{ scale: 1.4, opacity: 0 }}, {{ scale: 1, opacity: 0.82, duration: 0.32, ease: "power2.out", stagger: 0.06 }}, {start + 0.7:.2f});
      tl.fromTo("#s4-stamp", {{ scale: 2.6, opacity: 0, rotate: -25 }}, {{ scale: 1, opacity: 0.92, rotate: 10, duration: 0.42, ease: "back.out(2.2)" }}, {start + 0.85:.2f});
      tl.fromTo("#s4-stage", {{ x: -3, y: 2 }}, {{ x: 0, y: 0, duration: 0.18, ease: "power1.out" }}, {start + 0.88:.2f});
      tl.fromTo("#s4-ribbon", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + 0.95:.2f});
      // Dramatic punch-in to 93yo Morris Chang
      tl.to("#s4-stage", {{ scale: 1.16, x: 130, y: -25, duration: 1.2, ease: "power3.inOut" }}, {start + 8.5:.2f});
"""
    elif idx == 5:
        html += f"""      // ================= Scene 5: Interactive Time-Jump Timeline -> 1987 =================
      // 1. Reveal timeline overlay & backdrop (Vox Motif)
      tl.fromTo("#time-jump-overlay", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.45, ease: "power2.out" }}, {start + 0.1:.2f});
      tl.fromTo("#time-jump-hud", {{ scale: 0.94, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.55, ease: "power2.out" }}, {start + 0.2:.2f});
      tl.fromTo("#node-2024", {{ scale: 0.8, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.5)" }}, {start + 0.35:.2f});

      // 2. Virtual Mouse Cursor wakes up at 2024
      tl.fromTo("#time-jump-cursor", 
        {{ x: 1548, y: 540, opacity: 0, scale: 0.7 }}, 
        {{ opacity: 1, scale: 1, duration: 0.35, ease: "power2.out" }}, 
        {start + 1.2:.2f}
      );

      // 3. Cursor smoothly glides along timeline ruler backwards to 1987
      tl.to("#time-jump-cursor", {{
        x: 568,
        y: 540,
        duration: 2.0,
        ease: "power2.inOut"
      }}, {start + 1.6:.2f});

      // 4. Hover target 1987 node: ring pulses, callout reveals
      tl.fromTo("#ring-1987", 
        {{ scale: 0.5, opacity: 0, rotate: 0 }}, 
        {{ scale: 1.15, opacity: 1, rotate: 90, duration: 0.5, ease: "power2.out" }}, 
        {start + 3.6:.2f}
      );
      tl.fromTo("#callout-1987", 
        {{ y: 15, opacity: 0, scale: 0.85 }}, 
        {{ y: 0, opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.8)" }}, 
        {start + 3.7:.2f}
      );

      // 5. Cursor Click down + ripple effect at 63.31s (matching audio sfx-mouse-click)
      tl.to("#time-jump-cursor", {{ scale: 0.82, duration: 0.12, ease: "power1.in" }}, {start + 4.19:.2f});
      tl.fromTo("#cursor-ripple", 
        {{ scale: 0.2, opacity: 1 }}, 
        {{ scale: 3.2, opacity: 0, duration: 0.42, ease: "power2.out" }}, 
        {start + 4.22:.2f}
      );
      tl.to("#time-jump-cursor", {{ scale: 1.0, duration: 0.15, ease: "back.out(2)" }}, {start + 4.31:.2f});

      // 6. Dramatic Camera Zoom-in directly into the 1987 node and dissolve to archival paper
      tl.to("#time-jump-hud", {{
        scale: 4.8,
        duration: 1.35,
        ease: "power3.in"
      }}, {start + 4.45:.2f});
      tl.to("#time-jump-cursor", {{ opacity: 0, duration: 0.25 }}, {start + 4.45:.2f});
      tl.to("#time-jump-overlay", {{
        opacity: 0,
        duration: 0.65,
        ease: "power2.inOut"
      }}, {start + 5.25:.2f});

      // 7. Historical 1987 Stage and Morris Chang dossier reveals under zoom
      tl.fromTo("#s5-mat", {{ y: -30, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.55, ease: "power2.out" }}, {start + 5.20:.2f});
      tl.fromTo("#s5-card-center", {{ y: -70, scale: 0.92, opacity: 0, rotate: 0 }}, {{ y: 0, scale: 1, opacity: 1, rotate: 0.6, duration: 0.72, ease: "back.out(1.4)" }}, {start + 5.35:.2f});
      tl.fromTo("#scene5 .tape", {{ scale: 1.4, opacity: 0 }}, {{ scale: 1, opacity: 0.82, duration: 0.32, ease: "power2.out", stagger: 0.06 }}, {start + 5.70:.2f});
      tl.fromTo("#s5-stamp", {{ scale: 2.8, opacity: 0, rotate: -35 }}, {{ scale: 1, opacity: 0.92, rotate: -7, duration: 0.42, ease: "back.out(2.2)" }}, {start + 5.85:.2f});
      tl.fromTo("#s5-stage", {{ x: -3, y: 2 }}, {{ x: 0, y: 0, duration: 0.18, ease: "power1.out" }}, {start + 5.89:.2f});
      tl.fromTo("#s5-ribbon", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + 5.95:.2f});
      // Deep camera push into 1987 Morris Chang
      tl.to("#s5-stage", {{ scale: 1.18, x: 0, y: -45, duration: 1.3, ease: "power3.inOut" }}, {start + 12.0:.2f});
"""
    elif idx == 6:
        html += f"""      tl.fromTo("#s6-card-left", {{ x: -80, opacity: 0, rotate: 0 }}, {{ x: 0, opacity: 1, rotate: -1.5, duration: 0.65, ease: "power2.out" }}, {start + 0.25:.2f});
      tl.fromTo("#s6-card-right", {{ x: 80, opacity: 0, rotate: 0 }}, {{ x: 0, opacity: 1, rotate: 1.5, duration: 0.65, ease: "power2.out" }}, {start + 0.35:.2f});
      tl.fromTo("#s6-vs", {{ scale: 2.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.45, ease: "back.out(2)" }}, {start + 0.6:.2f});
      tl.fromTo("#scene6 .tape", {{ scale: 1.4, opacity: 0 }}, {{ scale: 1, opacity: 0.82, duration: 0.32, ease: "power2.out", stagger: 0.06 }}, {start + 0.7:.2f});
      tl.fromTo("#s6-stamp", {{ scale: 2.6, opacity: 0, rotate: -25 }}, {{ scale: 1, opacity: 0.92, rotate: 10, duration: 0.42, ease: "back.out(2.2)" }}, {start + 0.85:.2f});
      tl.fromTo("#s6-stage", {{ x: -3, y: 2 }}, {{ x: 0, y: 0, duration: 0.18, ease: "power1.out" }}, {start + 0.88:.2f});
      tl.fromTo("#s6-ribbon", {{ y: 25, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.5, ease: "power3.out" }}, {start + 0.95:.2f});
      tl.to("#s6-stage", {{ scale: 1.10, x: -50, y: -10, duration: 1.0, ease: "power2.inOut" }}, {start + 5.5:.2f});
"""

html += """
      window.__timelines["main"] = tl;
      tl.seek(0);
    </script>
  </body>
</html>
"""

with open("demo-tsmc/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Regenerated demo-tsmc/index.html with WW1/NHK 3-Zone Modular HUD layout!")
