---
title: "Worklog Tuần 12"
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Mục tiêu trọng tâm
- Lắp ráp, tích hợp cấu hình và thông luồng kết nối giữa 3 tầng dịch vụ: ReactJS Frontend, Spring Boot Backend và RDS Database.
- Triển khai chạy thử nghiệm hệ thống trực tiếp trên môi trường Internet thông qua đường dẫn ALB và CloudFront.
- Đảm bảo cơ chế bảo mật CORS, mã hóa giao dịch và kết nối thông suốt.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Cấu hình tham số kết nối database (JDBC URL, username, password) trong file `application.properties` của Spring Boot để trỏ về RDS MySQL Endpoint. | 03/07/2026 | 03/07/2026 | |
| 2 | Khởi động lại dịch vụ backend trên các EC2 instances trong Private Subnet và kiểm tra log kết nối cơ sở dữ liệu thành công. | 04/07/2026 | 04/07/2026 | |
| 3 | Biên dịch lại mã nguồn ReactJS Frontend, điều chỉnh cấu hình API Endpoint trỏ về tên miền/URL của Application Load Balancer. | 06/07/2026 | 06/07/2026 | |
| 4 | Cấu hình cho phép CORS (Cross-Origin Resource Sharing) trong ứng dụng Spring Boot để chấp nhận các yêu cầu gửi đến từ domain CloudFront. | 07/07/2026 | 07/07/2026 | |
| 5 | Đẩy bản dựng ReactJS mới nhất lên S3, xóa bộ nhớ đệm (Invalidation) trên CloudFront Distribution. | 08/07/2026 | 08/07/2026 | [CloudFront Invalidation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) |
| 6 | Truy cập website trực tiếp bằng link CloudFront, thực hiện tạo tài khoản, đặt lịch spa và mua sản phẩm để xác minh hệ thống hoạt động thông suốt từ đầu đến cuối (E2E). | 09/07/2026 | 09/07/2026 | |

### Kết quả đạt được
- Tích hợp thành công cấu trúc 3 tầng (Frontend - Backend - Database) hoạt động ăn khớp với nhau.
- Đưa website chính thức hoạt động trên môi trường Internet toàn cầu thông qua CloudFront CDN và ALB.
- Xác nhận các tính năng chính của Pet Resort (đăng ký, đặt lịch, giỏ hàng) hoạt động ổn định và chính xác.