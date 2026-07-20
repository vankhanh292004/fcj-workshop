---
title: "Worklog Tuần 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu trọng tâm
- Dịch chuyển cơ sở dữ liệu quan hệ MySQL lên dịch vụ quản lý Amazon RDS hỗ trợ kiến trúc Multi-AZ.
- Khởi tạo bộ nhớ đệm phân tán Amazon ElastiCache (Redis) nhằm nâng cao tốc độ tải và xử lý mượt mà tính năng giỏ hàng (Cart).
- Cấu hình phân quyền truy cập mạng lưới bảo mật an toàn cho cơ sở dữ liệu và cache.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu kiến trúc Amazon RDS Multi-AZ và các phương án tối ưu bộ nhớ đệm Redis trên AWS. | 12/06/2026 | 12/06/2026 | [Amazon RDS Docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) |
| 2 | Tạo Subnet Group chứa các Private Subnets dành riêng cho cơ sở dữ liệu RDS. | 13/06/2026 | 13/06/2026 | |
| 3 | Khởi tạo RDS MySQL Database Instance với tùy chọn Multi-AZ để tự động sao lưu dự phòng giữa các Availability Zones. | 15/06/2026 | 15/06/2026 | |
| 4 | Thiết lập phân vùng lưu trữ cache bằng cách khởi tạo cụm Amazon ElastiCache (Redis) trong vùng Private Subnets. | 16/06/2026 | 16/06/2026 | [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) |
| 5 | Điều chỉnh cấu hình Security Groups cho phép kết nối từ EC2 Backend đến cổng `3306` (RDS MySQL) và cổng `6379` (ElastiCache Redis). | 17/06/2026 | 17/06/2026 | |
| 6 | Đẩy dữ liệu cấu trúc mẫu (schema) của dự án lên RDS và kết nối thành công từ client quản lý database. | 18/06/2026 | 18/06/2026 | |

### Kết quả đạt được
- Triển khai thành công cơ sở dữ liệu Amazon RDS Multi-AZ có tính sẵn sàng cao và cơ chế tự động chuyển đổi dự phòng (failover).
- Cấu hình thành công cụm ElastiCache Redis phục vụ lưu trữ thông tin giỏ hàng tạm thời với tốc độ truy xuất cực nhanh.
- Thiết lập tường lửa mạng chặt chẽ, cô lập hoàn toàn tầng cơ sở dữ liệu và bộ nhớ đệm khỏi mạng công cộng.