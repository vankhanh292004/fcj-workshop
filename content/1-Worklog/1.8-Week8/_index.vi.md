---
title: "Worklog Tuần 8"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu trọng tâm
- Xây dựng cơ chế cân bằng tải thông minh bằng Application Load Balancer (ALB) đặt tại Public Subnets.
- Cấu hình Target Group hướng lưu lượng truy cập HTTP/HTTPS vào các EC2 Instances chạy Spring Boot.
- Thiết lập quy tắc co giãn tự động (Auto Scaling Group) để đảm bảo hệ thống tự động bổ sung máy chủ khi lưu lượng tải tăng đột biến.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu cơ chế hoạt động của Elastic Load Balancing (ELB) và Auto Scaling. | 05/06/2026 | 05/06/2026 | [AWS ALB Docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) |
| 2 | Tạo Application Load Balancer (ALB) nằm trên các Public Subnets ở 2 AZ khác nhau. | 06/06/2026 | 06/06/2026 | |
| 3 | Cấu hình Target Group cho ứng dụng Spring Boot chạy cổng `8080` kèm theo cơ chế Health Check (đường dẫn `/api/health`). | 08/06/2026 | 08/06/2026 | |
| 4 | Tạo Amazon Machine Image (AMI) từ EC2 đã cài đặt sẵn môi trường Spring Boot ở tuần trước để làm bản mẫu. | 09/06/2026 | 09/06/2026 | [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) |
| 5 | Tạo Launch Template và cấu hình Auto Scaling Group (ASG) sử dụng bản mẫu AMI vừa tạo, thiết lập số lượng instance tối thiểu (1) và tối đa (3). | 10/06/2026 | 10/06/2026 | [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) |
| 6 | Cấu hình Target Tracking Policy (khi CPU vượt quá 70% sẽ tự động scale-up máy chủ mới) và kiểm tra liên kết ALB đầu vào. | 11/06/2026 | 11/06/2026 | |

### Kết quả đạt được
- Triển khai thành công Application Load Balancer điều hướng lưu lượng truy cập trơn tru qua Target Group.
- Tạo bản mẫu AMI chuẩn hóa cấu hình môi trường Backend Spring Boot.
- Thiết lập thành công Auto Scaling Group đi kèm chính sách tự động co giãn, đảm bảo khả năng sẵn sàng cao và tối ưu hóa tài nguyên cho hệ thống.