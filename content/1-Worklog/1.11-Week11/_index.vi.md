---
title: "Worklog Tuần 11"
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu trọng tâm
- Rà soát bản vẽ mạng lưới Topology tổng thể của dự án Pet Resort.
- Triển khai giải pháp VPC Endpoint (S3 Gateway Endpoint) để tối ưu hóa đường truyền dữ liệu nội bộ.
- Cắt giảm chi phí NAT Gateway bằng cách cho phép các máy chủ trong vùng Private truy xuất S3 trực tiếp mà không cần đi qua Internet.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tổng hợp và đối chiếu bản vẽ thiết kế mạng lõi hiện tại với tài nguyên thực tế đã chạy trên AWS. | 26/06/2026 | 26/06/2026 | |
| 2 | Phân tích báo cáo chi phí AWS Billing, phát hiện chi phí NAT Gateway tăng cao do truyền tải hình ảnh thú cưng từ S3 về EC2. | 27/06/2026 | 27/06/2026 | |
| 3 | Nghiên cứu giải pháp VPC Endpoints (Gateway Endpoints và Interface Endpoints). | 29/06/2026 | 29/06/2026 | [VPC Endpoints Docs](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) |
| 4 | Tạo S3 Gateway Endpoint trong VPC và liên kết trực tiếp vào Route Table của các Private Subnets. | 30/06/2026 | 30/06/2026 | [S3 Gateway Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) |
| 5 | Điều chỉnh cấu hình Security Groups và S3 Bucket Policy để chấp nhận kết nối nội bộ thông qua Endpoint mới. | 01/07/2026 | 01/07/2026 | |
| 6 | Thực hiện tải tệp lớn từ S3 về EC2 trong Private Subnet và kiểm tra bảng định tuyến để đảm bảo gói tin không đi qua NAT Gateway. | 02/07/2026 | 02/07/2026 | |

### Kết quả đạt được
- Tối ưu hóa thành công đường truyền kết nối nội bộ giữa Amazon EC2 và Amazon S3.
- Tiết kiệm đáng kể chi phí băng thông NAT Gateway bằng cách giữ gói tin lưu chuyển hoàn toàn trong mạng nội bộ của AWS (không đi ra ngoài Internet công cộng).
- Hoàn thiện và chuẩn hóa sơ đồ mạng Topology phục vụ cho khâu đóng gói báo cáo cuối kỳ.