---
title: "Worklog Tuần 4"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

Mục tiêu trọng tâm của Tuần 4:
- Nghiên cứu hạ tầng mạng riêng ảo (VPC) nhằm xây dựng môi trường triển khai an toàn và biệt lập cho hệ thống.
- Triển khai cơ sở dữ liệu quan hệ Amazon RDS (động cơ MySQL) phục vụ cho dự án Pet Resort & Care.
- Cấu hình các nhóm bảo mật (Security Groups) nền tảng nhằm thiết lập lớp tường lửa bảo vệ dữ liệu.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu các khái niệm nền tảng về Amazon VPC, nguyên lý quy hoạch mạng thành Public Subnet (tiếp nhận traffic từ bên ngoài) và Private Subnet (ẩn giấu Database). | 11/05/2026 | 11/05/2026 | Tài liệu Amazon VPC |
| 2 | Tìm hiểu dịch vụ cơ sở dữ liệu Amazon RDS, tiến hành đánh giá ưu điểm của việc sử dụng RDS quản lý sẵn (Managed Service) so với tự vận hành MySQL trên EC2. | 12/05/2026 | 12/05/2026 | Tài liệu Amazon RDS |
| 3 | Tiến hành khởi tạo instance cơ sở dữ liệu Amazon RDS MySQL (áp dụng cấu hình Single-AZ thuộc gói Free Tier nhằm tối ưu hóa ngân sách thực tập). | 13/05/2026 | 13/05/2026 | AWS RDS Console |
| 4 | Thiết lập Security Group cho Database: Giới hạn quyền truy cập chỉ từ các dải IP nội bộ hoặc máy chủ được ủy quyền, ngăn chặn triệt để mọi kết nối trực tiếp từ Internet. | 14/05/2026 | 14/05/2026 | AWS Security Best Practices |
| 5 | Xác thực thông tin kết nối (Endpoint URL) của Database; chuẩn bị cấu trúc các bảng dữ liệu cốt lõi (User, Pet, Order) để sẵn sàng tích hợp với backend. | 15/05/2026 | 15/05/2026 | |

Kết quả đạt được trong Tuần 4:

• Hoàn thiện tư duy quy hoạch và thiết kế kiến trúc mạng an toàn trên môi trường Cloud dựa vào mô hình VPC và chiến lược phân chia Subnet chặt chẽ.

• Khởi chạy thành công hệ quản trị cơ sở dữ liệu MySQL trên nền tảng Amazon RDS (chế độ Single-AZ), đảm bảo đáp ứng yêu cầu kỹ thuật đồng thời tiết kiệm tối đa credit.

• Áp dụng thành công lớp tường lửa bằng Security Group, tạo màng chắn vững chắc bảo vệ Database instance khỏi các nguy cơ truy cập trái phép từ bên ngoài mạng lưới.