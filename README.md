# Nihonium

Phong trào ứng dụng nhắn tin và mạng xã hội mã nguồn mở dành cho người Việt 🇻🇳.

> Mức độ hiện tại: dự án đang ở giai đoạn khởi tạo / prototype UI. Chưa hoàn thiện chức năng chat, backend, API hay tích hợp mạng xã hội đầy đủ.

## Tình trạng hiện tại

- Đã có khung giao diện cơ bản bằng PySide6.
- Có thư mục `qfluentwidgets_pro/` chứa bản local của thư viện UI Fluent Widgets.
- Có thư mục `ui/` với các file khởi tạo: `mainwindow.py`, `sidebar.py`.
- `main.py` hiện chưa có logic chạy app thực tế.
- Chưa có API server, cơ sở dữ liệu, xác thực người dùng, hoặc chat real-time.

## Mục tiêu dự án

- Xây dựng ứng dụng nhắn tin đa nền tảng.
- Hỗ trợ người dùng Việt Nam với giao diện dễ dùng.
- Mở rộng khả năng tương tác như tin nhắn, file, hình ảnh, nhóm, quản lý hồ sơ.
- Phát triển theo mô hình mã nguồn mở, có thể mở rộng cộng đồng.

## Cấu trúc thư mục

```text
Nihonium/
├── README.md
├── main.py                  # điểm vào ứng dụng (hiện đang trong giai đoạn khởi tạo)
├── qfluentwidgets_pro/      # thư viện UI Fluent Widgets local/custom
│   ├── __init__.py
│   ├── common/
│   ├── components/
│   ├── window/
│   └── ...
├── ui/
│   ├── mainwindow.py
│   ├── sidebar.py
│   └── pages/
└── ...
```

## Yêu cầu môi trường

- Python 3.10+
- PySide6
- Thư viện UI Fluent Widgets (`qfluentwidgets_pro` đã được thêm vào repo)

Cài đặt cơ bản:

```bash
python -m venv .venv
source .venv/bin/activate  # trên macOS/Linux
python -m pip install --upgrade pip
python -m pip install PySide6
```

## Chạy ứng dụng

Hiện tại, dự án chưa có entrypoint hoàn chỉnh. Khi logic chạy app được triển khai, cách khởi chạy sẽ là:

```bash
python main.py
```

## Lộ trình phát triển

- [x] Khởi tạo repo và cấu trúc dự án.
- [x] Thiết lập nền tảng UI PySide6 / Fluent.
- [ ] Xây dựng giao diện chính và layout điều hướng.
- [ ] Xử lý hiển thị tin nhắn, chuyển trang, sidebar, profile, settings.
- [ ] Thiết kế API / backend cho nhắn tin.
- [ ] Tích hợp gửi nhận tin nhắn, file, hình ảnh, thư mục.
- [ ] Kết nối UI với API.
- [ ] Thêm bảo mật, xác thực, lưu trữ dữ liệu và tối ưu hiệu suất.

## Ghi chú

Dự án này hiện đang ở giai đoạn đầu và chưa nên được xem là sản phẩm hoàn chỉnh. README này phản ánh đúng trạng thái hiện tại của repository, thay vì mô tả một ứng dụng đã phát triển xong.
