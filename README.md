# HyperFrames YouTube Documentary — Vox × MagnatesMedia Style

Dự án dựng video documentary chuyên nghiệp phong cách kết hợp **Vox** (infographic, bản đồ, giải thích trực quan) và **MagnatesMedia** (kể chuyện kịch tính, xung đột, chiều sâu lịch sử) sử dụng công nghệ **HyperFrames** (Code-driven video production with HTML/CSS/GSAP).

---

## 📁 Cấu trúc Dự án

```
.
├── demo-tsmc-v2/           # Dự án chính: TSMC — The Semiconductor Empire (Act 1 Master)
│   ├── index.html          # Composition 1920x1080 24fps HTML/CSS/GSAP
│   └── assets/             # Âm thanh (VO, SFX, BGM), video, hình ảnh tư liệu
├── demo-tsmc/              # Bản dựng TSMC v1
├── demo-nvidia/            # Bản demo phong cách NVIDIA
├── demo-ww2/               # Bản demo tư liệu lịch sử WW2
├── toyota-demo/            # Bản demo Toyota
├── assets_tsmc/            # Thư viện tư liệu TSMC (bản đồ vệ tinh, phòng sạch EUV, ảnh lịch sử)
└── scripts/                # Bộ công cụ Python: sinh audio, phân tích đối thủ, xử lý màu
```

---

## 🚀 Hướng dẫn Sử dụng

### 1. Xem trước trong HyperFrames Studio (Live Preview)

Khởi chạy studio preview trên trình duyệt:

```bash
npx hyperframes preview demo-tsmc-v2
```

Hoặc xem trực tiếp trên port tuỳ chọn:

```bash
npx hyperframes preview demo-tsmc-v2 --port 3003
```

Mở trình duyệt tại: `http://localhost:3003/#project/demo-tsmc-v2`

### 2. Kiểm tra chất lượng (Linting)

```bash
npx hyperframes lint demo-tsmc-v2
```

### 3. Chụp ảnh kiểm tra từng mốc thời gian (Snapshots)

```bash
npx hyperframes snapshot demo-tsmc-v2 --at 1.0,3.8,6.0,7.5,8.3,9.5 --output ./snapshots
```

### 4. Xuất video MP4 (Render)

```bash
npx hyperframes render demo-tsmc-v2 --output ./output/tsmc_act1_master.mp4
```

---

## 🎨 Đặc trưng Visual DNA

- **Hệ màu:** Warm Vintage Gold Parchment (`#F3E8D2` highlight, `#C89E48` amber gold, `#1C1712` deep ink).
- **Typography:** `Oswald` (tiêu đề mạnh mẽ), `Noto Serif JP` & `Noto Sans JP` (nội dung tiếng Nhật), `JetBrains Mono` / `Courier Prime` (thông số hồ sơ kỹ thuật).
- **Storytelling:** Kết hợp zoom 3D từ vũ trụ, hạ cánh xuống eo biển Đài Loan, khóa mục tiêu Tân Trúc, cảnh đệm phòng sạch siêu tinh khiết EUV Gigafab 12 và chuyển tiếp sang bộ thẻ hồ sơ tác động chuỗi cung ứng toàn cầu.
