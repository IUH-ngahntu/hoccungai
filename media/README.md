# Danh mục media

Tất cả media do tác giả tự tạo (Python/Pillow, ffmpeg, espeak-ng). Dung lượng đo thực tế (1 KB = 1000 byte).

| Tệp | Mô tả | Nguồn | Giấy phép | Văn bản thay thế / phụ đề | Dung lượng (KB) |
|---|---|---|---|---|---|
| `img/logo.svg` | Logo (M1) | Tự thiết kế | Nhóm sở hữu | alt="Học Cùng AI – về trang chủ" | 0.4 |
| `img/icons.svg` | Icon sprite (M6) | Tự vẽ SVG | Nhóm sở hữu | aria-hidden (icon trang trí) | 0.7 |
| `img/favicon.png` | Favicon (M7) | Tạo từ logo | Nhóm sở hữu | không cần | 0.4 |
| `img/hero-1280.webp` | Hero 1280×480 (M2) | Tự thiết kế (Pillow) | Nhóm sở hữu | Hình hai sinh viên cạnh laptop và biểu tượng AI | 12.9 |
| `img/hero-768.webp` | Hero 768×320 (M2) | Tự thiết kế | Nhóm sở hữu | như trên | 8.5 |
| `img/hero-360.webp` | Hero 360×220 (M2) | Tự thiết kế | Nhóm sở hữu | như trên | 5.1 |
| `img/hero-1280.jpg` | Hero JPEG dự phòng | Tự thiết kế | Nhóm sở hữu | như trên | 29.5 |
| `img/chu-de-1.webp` | Thumb chủ đề 1 (M4) | Tự thiết kế | Nhóm sở hữu | Biểu tượng AI trên nền xanh | 2.5 |
| `img/chu-de-2.webp` | Thumb chủ đề 2 (M4) | Tự thiết kế | Nhóm sở hữu | Dấu tích trên nền cam | 2.8 |
| `img/chu-de-3.webp` | Thumb chủ đề 3 (M4) | Tự thiết kế | Nhóm sở hữu | Dấu hỏi trên nền xanh lá | 2.1 |
| `img/ve-chung-toi.webp` | Ảnh “Về chúng tôi” (M5) | Tự thiết kế | Nhóm sở hữu | Sơ đồ ba bước | 6.2 |
| `img/banner-bai-2-960.webp` | Banner bài 2 – 960 (M8) | Tự thiết kế | Nhóm sở hữu | Biển hiệu bài 2 | 7.8 |
| `img/banner-bai-2-768.webp` | Banner bài 2 – 768 (M8) | Tự thiết kế | Nhóm sở hữu | như trên | 5.8 |
| `img/banner-bai-2-360.webp` | Banner bài 2 – 360 (M8) | Tự thiết kế | Nhóm sở hữu | như trên | 2.6 |
| `img/infographic-bai-2.webp` | Infographic (M10) | Tự thiết kế | Nhóm sở hữu | Ba cột + figcaption đầy đủ | 27.8 |
| `img/infographic-bai-2.pdf` | Infographic PDF | Tự thiết kế | Nhóm sở hữu | bản tải về | 54.3 |
| `img/lien-quan-1-240.webp` | Bài liên quan 1 – 240 (M11) | Tự thiết kế | Nhóm sở hữu | Biển hiệu Bài 1 | 1.6 |
| `img/lien-quan-1-480.webp` | Bài liên quan 1 – 480 (M11) | Tự thiết kế | Nhóm sở hữu | như trên | 3.6 |
| `img/lien-quan-3-240.webp` | Bài liên quan 3 – 240 (M11) | Tự thiết kế | Nhóm sở hữu | Biển hiệu Bài 3 | 1.7 |
| `img/lien-quan-3-480.webp` | Bài liên quan 3 – 480 (M11) | Tự thiết kế | Nhóm sở hữu | như trên | 3.9 |
| `video/intro.mp4` | Video giới thiệu 18 s MP4 (M3) | Tự dựng (ffmpeg) | Nhóm sở hữu | Phụ đề intro.vi.vtt + bản chữ | 310.3 |
| `video/intro.webm` | Video giới thiệu WebM | Tự dựng | Nhóm sở hữu | như trên | 361.9 |
| `video/intro-poster.webp` | Poster video giới thiệu (M3p) | Trích từ video | Nhóm sở hữu | không cần (poster) | 3.4 |
| `video/intro.vi.vtt` | Phụ đề video giới thiệu | Tự viết | Nhóm sở hữu | — | 0.4 |
| `video/bai-2.mp4` | Video bài 2 – 60 s MP4 (M9) | Tự dựng | Nhóm sở hữu | Phụ đề bai-2.vi.vtt + bản chữ | 789.9 |
| `video/bai-2.webm` | Video bài 2 WebM | Tự dựng | Nhóm sở hữu | như trên | 723.3 |
| `video/bai-2-poster.webp` | Poster video bài 2 | Trích từ video | Nhóm sở hữu | không cần (poster) | 7.4 |
| `video/bai-2.vi.vtt` | Phụ đề bài 2 | Tự viết | Nhóm sở hữu | — | 1.1 |
| `audio/bai-2.mp3` | Âm thanh bài 2 MP3 | espeak-ng (giọng tổng hợp) | Dùng nội bộ; thay bằng giọng thu thật | Bản chữ trên trang | 360.6 |
| `audio/bai-2.ogg` | Âm thanh bài 2 OGG | espeak-ng | như trên | như trên | 169.3 |

Tổng dung lượng thư mục media: 2908 KB.

## Quy trình cập nhật media
1. Đặt tệp gốc vào nơi lưu trữ riêng (không commit tệp gốc nặng).
2. Nén: ảnh WebP chất lượng 70; video H.264 Baseline + AAC (MP4) và VP9 + Opus (WebM).
3. Thêm alt/phụ đề, cập nhật bảng này và `media/media.json`.
4. Chạy `tools/check-site.py` rồi mới commit.
