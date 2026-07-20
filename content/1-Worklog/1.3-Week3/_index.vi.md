---
title: "Worklog Tuần 3"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu trọng tâm
- Bắt tay thiết kế bản đồ mạng lõi trên AWS bằng dịch vụ Amazon VPC.
- Phân chia CIDR Block và cấu hình dải Subnet hợp lý cho hệ thống Pet Care.
- Thiết lập ranh giới rõ ràng giữa vùng mạng nội bộ (Private Subnet) chứa Database/Backend và mạng công cộng (Public Subnet) chứa Load Balancer/NAT.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu kiến trúc VPC, cách phân bổ CIDR Block và quy hoạch IP cho hệ thống. | 01/05/2026 | 01/05/2026 | [Amazon VPC Docs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 2 | Phác thảo sơ đồ thiết kế VPC gồm 2 Availability Zones (AZs) để đảm bảo tính sẵn sàng cao. | 02/05/2026 | 02/05/2026 | |
| 3 | Tạo VPC chính cho dự án với CIDR `10.0.0.0/16` trên bảng điều khiển AWS. | 04/05/2026 | 04/05/2026 | |
| 4 | Cấu hình 2 Public Subnet (một cho mỗi AZ) để tiếp nhận lưu lượng truy cập từ ngoài Internet. | 05/05/2026 | 05/05/2026 | |
| 5 | Cấu hình 4 Private Subnet (2 cho Backend App và 2 cho RDS Database) nhằm cô lập hoàn toàn tài nguyên nhạy cảm. | 06/05/2026 | 06/05/2026 | |
| 6 | Kiểm tra lại bảng phân bổ địa chỉ IP của VPC và hoàn thành thiết kế sơ đồ mạng lõi. | 07/05/2026 | 07/05/2026 | |

### Kết quả đạt được
- Tạo thành công Amazon VPC ổn định làm nền tảng mạng lõi cho toàn bộ dự án.
- Thiết lập phân vùng rõ ràng với 2 Public Subnets và 4 Private Subnets trải rộng trên 2 Availability Zones.
- Đảm bảo các tài nguyên hệ thống được cô lập đúng cách tại tầng mạng.