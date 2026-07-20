---
title: "Worklog Tuần 5"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu trọng tâm
- Khởi tạo không gian lưu trữ đối tượng ổn định, bảo mật với Amazon S3.
- Cấu hình Bucket S3 để sẵn sàng lưu trữ tài nguyên tĩnh (Static Assets) và hosting website tĩnh.
- Triển khai đẩy toàn bộ mã nguồn giao diện người dùng (ReactJS) và các tệp tin hình ảnh thú cưng lên các Bucket tương ứng.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tìm hiểu kiến trúc lưu trữ Amazon S3, các Storage Classes và cơ chế bảo mật (Bucket Policy, ACL). | 15/05/2026 | 15/05/2026 | [Amazon S3 Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 2 | Tạo Bucket `pet-resort-frontend` để lưu trữ mã nguồn tĩnh của ReactJS. | 16/05/2026 | 16/05/2026 | |
| 3 | Tạo Bucket `pet-resort-media` chuyên biệt dành cho hình ảnh thú cưng và cấu hình quyền truy cập. | 18/05/2026 | 18/05/2026 | |
| 4 | Cấu hình tính năng "Static website hosting" trên Bucket frontend và thiết lập chính sách Bucket Policy cho phép đọc công khai (Public Read) tạm thời phục vụ thử nghiệm. | 19/05/2026 | 19/05/2026 | |
| 5 | Xây dựng mã nguồn ReactJS (`npm run build`) dưới local và đẩy toàn bộ thư mục `dist`/`build` lên S3 Frontend Bucket. | 20/05/2026 | 20/05/2026 | |
| 6 | Kiểm tra liên kết truy cập tĩnh của S3, tải lên thử nghiệm các hình ảnh thú cưng và xác minh hiển thị. | 21/05/2026 | 21/05/2026 | |

### Kết quả đạt được
- Khởi tạo thành công 2 S3 Buckets chuyên biệt cho Frontend và Media.
- Triển khai thành công ứng dụng ReactJS lên S3 Static Hosting.
- Xác nhận tài nguyên tĩnh và hình ảnh được lưu trữ an toàn, truy cập trơn tru với đường dẫn S3 URL trực tiếp.