---
title: "Worklog Tuần 6"
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu trọng tâm
- Phân phối nội dung tĩnh toàn cầu với độ trễ thấp thông qua mạng lưới CDN Amazon CloudFront.
- Đóng quyền truy cập trực tiếp từ Internet vào S3 Frontend, chỉ cho phép đi qua CloudFront bằng Origin Access Control (OAC).
- Cấu hình lá chắn bảo mật AWS WAF để phát hiện và ngăn chặn các cuộc tấn công mạng nguy hiểm (SQL Injection, XSS, v.v.).

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tìm hiểu nguyên lý hoạt động của CDN CloudFront, khái niệm Edge Location, TTL và Origin. | 22/05/2026 | 22/05/2026 | [Amazon CloudFront Docs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) |
| 2 | Tạo CloudFront Distribution, trỏ Origin về S3 Bucket chứa Frontend ReactJS của dự án. | 23/05/2026 | 23/05/2026 | |
| 3 | Cấu hình Origin Access Control (OAC) và cập nhật lại S3 Bucket Policy để chỉ cho phép lưu lượng đến từ CloudFront. | 25/05/2026 | 25/05/2026 | |
| 4 | Cài đặt Error Pages trên CloudFront để xử lý các yêu cầu trang SPA (chuyển hướng lỗi 403/404 về `index.html` với mã 200). | 26/05/2026 | 26/05/2026 | |
| 5 | Nghiên cứu AWS WAF (Web Application Firewall) và tạo một Web ACL cơ bản. | 27/05/2026 | 27/05/2026 | [AWS WAF Docs](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |
| 6 | Đính kèm Web ACL chứa các bộ quy tắc chuẩn của AWS (AWS Managed Rules) vào CloudFront Distribution và xác minh hoạt động. | 28/05/2026 | 28/05/2026 | |

### Kết quả đạt được
- Tăng tốc độ tải trang giao diện đáng kể bằng việc lưu đệm (cache) tài nguyên ở các Edge Location toàn cầu qua CloudFront.
- Khóa hoàn toàn quyền truy cập trực tiếp S3 bucket Frontend từ bên ngoài, chỉ cho phép kết nối hợp lệ đi qua CloudFront.
- Áp dụng thành công lá chắn AWS WAF để bảo vệ lớp giao diện người dùng trước các rủi ro tấn công mạng phổ biến.