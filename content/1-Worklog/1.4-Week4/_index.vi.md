---
title: "Worklog Tuần 4"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu trọng tâm
- Thiết lập các "cửa ngõ" giao thông mạng để kết nối VPC ra bên ngoài (Internet Gateway & NAT Gateway).
- Cấu hình Route Table điều hướng gói tin cho từng loại Subnet (Public và Private).
- Tạo và định nghĩa các chốt chặn bảo mật (Security Groups) ở cấp độ Instance để kiểm soát luồng dữ liệu truy cập ra vào.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tạo Internet Gateway (IGW) và đính kèm (attach) vào VPC dự án để mở luồng Internet cho Public Subnets. | 08/05/2026 | 08/05/2026 | [VPC Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) |
| 2 | Cấu hình Route Table cho Public Subnet định tuyến lưu lượng `0.0.0.0/0` qua Internet Gateway. | 09/05/2026 | 09/05/2026 | |
| 3 | Tạo Elastic IP và khởi tạo NAT Gateway đặt tại Public Subnet để cho phép Private Subnet kết nối Internet một chiều. | 11/05/2026 | 11/05/2026 | [NAT Gateway Docs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 4 | Cấu hình Route Table cho các Private Subnets để chuyển hướng lưu lượng đi ra ngoài Internet qua NAT Gateway. | 12/05/2026 | 12/05/2026 | |
| 5 | Thiết kế các chốt chặn bảo mật Security Group riêng cho ALB, EC2 Web Server và RDS Database Instance. | 13/05/2026 | 13/05/2026 | [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) |
| 6 | Cấu hình luật Inbound/Outbound rules cho các Security Group (chỉ cho phép EC2 nhận traffic từ ALB, RDS nhận traffic từ EC2). | 14/05/2026 | 14/05/2026 | |

### Kết quả đạt được
- Hoàn thành hạ tầng định tuyến mạng VPC: Mạng Public kết nối Internet hai chiều, mạng Private chỉ kết nối Internet một chiều qua NAT Gateway (phục vụ cập nhật thư viện và tải gói phần mềm).
- Thiết lập tường lửa Security Group hoạt động chéo chặt chẽ, ngăn chặn triệt để các kết nối trực tiếp trái phép từ môi trường ngoài vào tầng Backend/Database.