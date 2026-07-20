---
title: "Worklog Tuần 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu trọng tâm
- Thiết lập hệ thống giám sát sức khỏe hạ tầng thời gian thực bằng Amazon CloudWatch.
- Thu thập và phân tích các chỉ số CPU, RAM, Network của EC2 và các kết nối cơ sở dữ liệu trên RDS.
- Xây dựng cơ chế gửi thông báo cảnh báo tự động thông qua Amazon Simple Notification Service (SNS) khi hệ thống gặp sự cố.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tìm hiểu hệ thống giám sát Amazon CloudWatch (Metrics, Alarms, Logs) và dịch vụ thông báo Amazon SNS. | 19/06/2026 | 19/06/2026 | [Amazon CloudWatch Docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) |
| 2 | Cấu hình CloudWatch Agent trên máy chủ EC2 để bắt đầu gửi các log hệ thống và log Spring Boot về CloudWatch Log Groups. | 20/06/2026 | 20/06/2026 | |
| 3 | Tạo Amazon SNS Topic tên `system-alerts` và thực hiện đăng ký (subscribe) nhận tin nhắn qua email cá nhân. | 22/06/2026 | 22/06/2026 | [Amazon SNS Docs](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) |
| 4 | Cấu hình các CloudWatch Alarms giám sát chỉ số CPU Utilization (cảnh báo khi > 80% liên tục trong 5 phút) cho các EC2 Instance. | 23/06/2026 | 23/06/2026 | |
| 5 | Tạo cảnh báo CloudWatch Alarm theo dõi trạng thái kết nối Database Connections trên RDS và lỗi HTTP 5XX từ ALB. | 24/06/2026 | 24/06/2026 | |
| 6 | Thực hiện kiểm tra thử nghiệm cơ chế bắn cảnh báo (giả lập tăng CPU ảo) và kiểm tra email thông báo nhận được từ SNS. | 25/06/2026 | 25/06/2026 | |

### Kết quả đạt được
- Tích hợp thành công bộ giám sát tập trung CloudWatch thu thập đầy đủ log và chỉ số hiệu năng hệ thống.
- Cấu hình các ngưỡng cảnh báo linh hoạt giúp phát hiện sớm các nguy cơ quá tải máy chủ hoặc ngắt kết nối cơ sở dữ liệu.
- Thiết lập kênh thông báo tự động qua email thông qua Amazon SNS, đảm bảo khả năng phản ứng nhanh trước các lỗi vận hành.