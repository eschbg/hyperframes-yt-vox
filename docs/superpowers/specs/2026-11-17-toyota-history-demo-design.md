# Thiết kế demo: Từ máy dệt đến Toyota

## Ý định

Tạo video demo ngang 16:9, dài đúng 30 giây, kể một mạch nguyên nhân–kết quả: gốc máy dệt của Sakichi Toyoda, Toyota thành lập năm 1937, triết lý sản xuất sau chiến tranh và Prius/hybrid. Mục tiêu là thể hiện phong cách documentary lịch sử đã quan sát: giấy nhăn, tư liệu cắt dán, bản đồ tối giản và chữ nhấn mầu vàng.

## Mục tiêu và giới hạn

- Đầu ra là `output/toyota-history-demo-30s.mp4`, 1920×1080, 30 giây, có hình, caption và nhạc/SFX không bản quyền.
- Mỗi cảnh chỉ truyền một ý; có mốc năm, hình chứng cứ hoặc bản đồ, và một kết luận ngắn.
- Palette: kem giấy, đen than, đỏ Toyota, vàng mù tạt. Dùng vàng chỉ cho từ khóa.
- Không tái tạo logo/tài liệu Toyota chính xác; không dùng tư liệu không rõ quyền sử dụng; không khẳng định số liệu không có nguồn kiểm chứng.

## Phương án đã cân nhắc

1. “Từ máy dệt đến Toyota” — được chọn: có mạch lịch sử rõ trong 30 giây.
2. Tác động của Toyota lên ngành xe — quá trừu tượng cho demo ngắn.
3. Một chiếc Corolla, một đế chế — hẹp hơn mục tiêu kể lịch sử công ty.

## Kịch bản định hướng

| Thời lượng | Ý chính | Hình ảnh |
| --- | --- | --- |
| 0–5s | Sakichi Toyoda và máy dệt | giấy nhăn, bản vẽ/máy dệt, mốc 1890s |
| 5–11s | Toyota thành lập 1937 | Nhật Bản tối giản, ảnh/nhãn xe đầu tiên |
| 11–19s | Hậu chiến và TPS | ảnh nhà máy cắt dán, luồng thẻ/linh kiện tối giản |
| 19–26s | Prius 1997 và hybrid | xe silhouette đỏ, biểu đồ năng lượng xanh-vàng |
| 26–30s | Kết | timeline thu gọn và câu chốt |

## Tiêu chí chấp nhận

- Thời lượng đo bằng `ffprobe` là 30.0 giây ± 0.1 giây.
- Cảnh 0–5, 5–11, 11–19, 19–26, 26–30 xuất hiện theo đúng thứ tự và caption đọc được.
- Render không có frame đen không chủ ý, không méo hình, không lỗi thiếu asset hoặc âm thanh vỡ.
- Style nhất quán với palette và quy tắc typography đã định.
