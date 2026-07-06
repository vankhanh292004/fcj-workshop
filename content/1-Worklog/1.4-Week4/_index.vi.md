---
title: "Worklog Tuần 4"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

Mục tiêu tuần 4:
- Tìm hiểu về hạ tầng mạng ảo cô lập (VPC) để làm môi trường triển khai hệ thống an toàn.
- Khởi tạo cơ sở dữ liệu quan hệ Amazon RDS MySQL cho dự án Pet Resort & Care.
- Thiết lập các nhóm bảo mật (Security Groups) ban đầu để bảo vệ dữ liệu.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tìm hiểu khái niệm cơ bản về Amazon VPC, cách phân chia Public Subnet (đón khách) và Private Subnet (giấu Database). | 11/05/2026 | 11/05/2026 | Tài liệu Amazon VPC |
| 2 | Nghiên cứu về dịch vụ cơ sở dữ liệu quan hệ Amazon RDS, so sánh ưu điểm giữa tự cài MySQL trên EC2 và dùng RDS quản lý sẵn. | 12/05/2026 | 12/05/2026 | Tài liệu Amazon RDS |
| 3 | Thực hành khởi tạo một cơ sở dữ liệu Amazon RDS MySQL (lựa chọn cấu hình Single-AZ Free Tier để tối ưu chi phí thực tập). | 13/05/2026 | 13/05/2026 | AWS RDS Console |
| 4 | Cấu hình Security Group cho Database: Chỉ cho phép các dải IP nội bộ hoặc máy chủ được chỉ định truy cập, chặn hoàn toàn Internet bên ngoài. | 14/05/2026 | 14/05/2026 | AWS Security Best Practices |
| 5 | Kiểm tra thông tin kết nối (Endpoint URL) của Database; chuẩn bị cấu hình các bảng dữ liệu mẫu (User, Pet, Order) cho backend. | 15/05/2026 | 15/05/2026 | |

Thành tích tuần 4:

• Nắm vững tư duy thiết kế mạng an toàn trên Cloud thông qua mô hình VPC và phân tách Subnet bảo mật.

• Khởi tạo thành công máy chủ Database MySQL trên nền tảng Amazon RDS ở chế độ Single-AZ để tiết kiệm ngân sách credit.

• Thiết lập thành công lớp tường lửa Security Group cơ bản để bảo vệ Database khỏi các truy cập trái phép từ Internet.