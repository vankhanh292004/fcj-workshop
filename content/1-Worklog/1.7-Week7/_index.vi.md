---
title: "Worklog Tuần 7"
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu trọng tâm
- Khởi tạo máy chủ ảo Amazon EC2 nằm trong vùng mạng riêng (Private Subnet).
- Cấu hình hạ tầng tính toán chạy hệ điều hành Linux (Amazon Linux/Ubuntu).
- Thiết lập môi trường chạy ứng dụng Java và chuẩn bị các điều kiện cần thiết để triển khai Backend Spring Boot.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu các dòng Instance của EC2, lựa chọn kích cỡ máy chủ tối ưu (`t3.medium`/`t3.micro`) phù hợp với Spring Boot. | 29/05/2026 | 29/05/2026 | [Amazon EC2 Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 2 | Khởi tạo EC2 Instances chạy hệ điều hành Amazon Linux 2 tại các Private Subnets của VPC. | 30/05/2026 | 30/05/2026 | |
| 3 | Tạo và quản lý an toàn cặp khóa Key Pair (.pem) để kết nối SSH bảo mật vào máy chủ ảo. | 01/06/2026 | 01/06/2026 | |
| 4 | Cấu hình Bastion Host (hoặc EC2 Instance Connect Endpoint) để làm cầu nối SSH từ ngoài Internet vào các máy chủ trong Private Subnet. | 02/06/2026 | 02/06/2026 | |
| 5 | Kết nối SSH thành công vào EC2 và thực hiện cài đặt môi trường Java (OpenJDK 17) cùng các gói công cụ cơ bản. | 03/06/2026 | 03/06/2026 | |
| 6 | Đóng gói ứng dụng Spring Boot và chuyển tệp tin `.jar` lên máy chủ EC2 để kiểm tra khởi chạy môi trường thành công. | 04/06/2026 | 04/06/2026 | |

### Kết quả đạt được
- Tạo thành công các máy chủ ảo EC2 được cô lập an toàn trong Private Subnets.
- Cài đặt đầy đủ runtime Java 17 và cấu hình hệ điều hành sẵn sàng để chạy Spring Boot.
- Thiết lập cơ chế kết nối SSH gián tiếp an toàn thông qua Bastion Host, duy trì bảo mật cho phân vùng mạng lõi.