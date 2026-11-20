---
name: vox-channel-standards
description: Use when designing visual identity, creating brand assets, reviewing thumbnails, or verifying historical authenticity for a Vox × MagnatesMedia style documentary YouTube channel.
---

# Vox × MagnatesMedia Channel Brand Standards

## Overview

This skill establishes the universal **Visual DNA, Historical Authenticity Rules, and Quality Gates** for the channel. Every video in the series must adhere to these identity standards to maintain recognizability, viewer retention, and documentary authority.

---

## 1. Visual DNA & Color Palette

### ⚠️ Rủi ro 1: Bị biến thành "Tài liệu Thế chiến / Cổ trang"
- **Hiện tượng:** Nếu nền giấy quá sẫm màu, quá nhiều vết ố cà phê và rách cháy xém, khán giả sẽ tưởng đây là video về Thế chiến II, Đức Quốc Xã hoặc thời Trung cổ.
- **Quy chuẩn bắt buộc:**
  - Giữ nền giấy ở tông **vàng kem hiện đại** (Manila Folder / Archival Office Paper):
    - Light: `#fbf7ee`
    - Mid / Canvas: `#f3e8d2`
    - Dark accent: `#181512`
  - Đan cài các yếu tố **Tech & Business hiện đại**:
    - Lưới tọa độ vi mạch / blueprint grid overlay (`.tech-grid-overlay`).
    - Biểu đồ tài chính phẳng sạch sẽ, thước đo gauge 90%, thanh đo số liệu điện tử.

---

## 2. Historical & Visual Authenticity

### ⚠️ Rủi ro 2: Khán giả soi tính chính xác của tư liệu (Visual Authenticity)
Khán giả của ngách công nghệ, tài chính và lịch sử doanh nghiệp là nhóm người có học thức cao và cực kỳ tinh ý.
- **Quy tắc vàng 1: Đúng nhân vật — Đúng năm tháng:**
  - Ảnh Morris Chang 55 tuổi thành lập TSMC (1987) phải là ảnh trung niên thời Texas Instruments, tuyệt đối không lấy ảnh cụ già 93 tuổi gán vào năm 1987.
  - Ảnh Andy Grove (Intel) trong cuộc thanh tra 1988 phải đúng thời kỳ CEO Intel, không dùng ảnh những năm 1960.
  - Ảnh Jensen Huang năm 1995 phải là ảnh thanh niên thời đầu thành lập NVIDIA.
- **Quy tắc vàng 2: Phân biệt tư liệu thật và tái hiện (Reconstruction):**
  - Không tự tạo văn bản, hợp đồng giả mạo rồi khẳng định là tài liệu thật.
  - Các tài liệu đồ họa phục dựng phải có nhãn rõ ràng: `RECONSTRUCTION` / `CASE ARCHIVE` / `DOSSIER`.

---

## 3. The 4 Brand Signature Components

Every episode on the channel must include these four signature components:

### 1. Fixed Top Bar (Khung định vị điều tra)
- **Vị trí:** Cố định góc trên màn hình (`top: 36px; left: 60px; right: 60px`).
- **Nội dung:**
  - Trái: `<span class="vox-pill-badge">ACT X</span> CASE FILE #0X: [TÊN CÔNG TY] // [CHỦ ĐỀ PHÂN CẢNH]`
  - Phải: `[NĂM] // [ĐỊA ĐIỂM / TỔ CHỨC]`
- **Mục đích:** Khẳng định với khán giả đây là một series hồ sơ điều tra chuyên sâu.

### 2. Action Stamps (Con dấu mộc đập xuống tại bước ngoặt)
- Mỗi bước ngoặt kịch tính phải có một con dấu mộc đập mạnh xuống kèm âm thanh `impact_boom.wav` hoặc `paper_slap.wav`:
  - `RESIGNED` (Từ chức / Bị phế truất)
  - `REJECTED` (Bị đối tác từ chối)
  - `BANKRUPT / COLLAPSE` (Bên bờ vực phá sản)
  - `ALL-IN` (Canh bạc tất tay)
  - `INTEL CERTIFIED` (Đạt chứng chỉ chất lượng)
  - `100% EXCLUSIVE` (Độc quyền toàn cầu)
  - `SILICON SHIELD` (Lá chắn địa chính trị)

### 3. 1-vs-1 Confrontation / Morph Split (Màn đấu trí đối kháng)
- Khi phân tích đấu trí kinh doanh (Intel vs TSMC, Apple vs Samsung, IDM vs Foundry):
  - Sử dụng bố cục chia đôi màn hình (Split screen: Bên trái khách hàng/đối thủ, bên phải TSMC).
  - Hoặc sơ đồ Morph: Khối IDM vỡ đôi thành Fabless + Pure-play Foundry.

### 4. Yellow Highlighter (`.vox-highlight-box`)
- Vệt bút dạ quang vàng chỉ quét vào các con số chấn động hoặc tôn chỉ cốt lõi:
  - `$10B CapEx`, `90% Global Share`, `200 Defects`, `1.2 Trillion Yen`.
  - Tuyên ngôn: `「顧客と絶対に競合しない」` (Không bao giờ cạnh tranh với khách hàng).
- **Tuyệt đối không:** Quét bừa bãi toàn bộ đoạn văn bản, chỉ quét đúng cụm từ khóa then chốt.

---

## 4. Episode Production Quality Gates

Mỗi video trước khi xuất bản lên kênh phải vượt qua bảng kiểm soát 5 điểm:

- [ ] **1. Bảng màu:** Manila kem hiện đại (`#f3e8d2`), không bị ngả sang màu nâu cháy của Thế chiến.
- [ ] **2. Nhân vật & Mốc năm:** Nhân vật lịch sử đúng độ tuổi tương ứng với sự kiện đang kể.
- [ ] **3. Âm thanh cân bằng:** Giọng đọc to rõ (Peak `-2.5 dB`), BGM nền lùi hẳn phía sau (Peak `-18.2 dB`, Mean `-34 dB`), SFX không chói tai.
- [ ] **4. Pacing 18–20 phút:** Có đủ khoảng nghỉ (Hold time 8.5–12.5s) cho từng đồ họa và con dấu.
- [ ] **5. Con dấu hành động:** Có ít nhất 4–6 con dấu mộc đập xuống tại các bước ngoặt kịch tính.
