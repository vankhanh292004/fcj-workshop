---
title: "Worklog Tuần 11"
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

* Tiếp nhận đánh giá (feedback) từ Admin/Mentor để chỉnh sửa, tối ưu hóa và chốt sơ đồ kiến trúc AWS cuối cùng.
* Tiến hành triển khai (Deploy) toàn bộ dự án Pet Resort & Care System (cả Frontend và Backend) lên môi trường Cloud thực tế dựa trên kiến trúc đã chốt.
* Đảm bảo hệ thống hoạt động ổn định trên kiến trúc 3-Tier, đáp ứng tính sẵn sàng cao (Multi-AZ) và bảo mật khép kín.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Tiếp nhận feedback từ admin: Chỉnh sửa lại luồng CloudFront phân phối nội dung Frontend và Media để tránh lỗi flow; vẽ lại các line kết nối cho trực quan.<br>- Chốt bản vẽ kiến trúc AWS cuối cùng. | 29/06/2026   | 29/06/2026      | Feedback từ Admin AWS Study Group         |
| 3   | - Triển khai lớp Mạng & Bảo mật: Khởi tạo VPC, Public/Private Subnet (Multi-AZ), NAT Gateway.<br>- Thiết lập Security Groups, IAM Roles, KMS và Secrets Manager.                            | 30/06/2026   | 30/06/2026      | AWS Documentation (VPC, IAM, KMS)         |
| 4   | - Triển khai lớp Dữ liệu (Data Tier): Cài đặt Amazon RDS MySQL (Multi-AZ, Sync Replication) và Amazon ElastiCache (Redis) theo mô hình Cache-Aside.                                         | 01/07/2026   | 01/07/2026      | AWS Documentation (RDS, ElastiCache)      |
| 5   | - Triển khai lớp Tính toán (Compute Tier): Đưa mã nguồn Backend Spring Boot lên EC2.<br>- Cấu hình Auto Scaling Group và điều phối traffic bằng Application Load Balancer (ALB).            | 02/07/2026   | 03/07/2026      | AWS Documentation (EC2, ALB, Auto Scaling)|
| 7   | - Triển khai lớp Biên (Edge): Upload mã nguồn tĩnh ReactJS lên S3 Frontend, tạo S3 Media.<br>- Cấu hình CloudFront phân luồng request và gắn tường lửa AWS WAF để bảo vệ hệ thống.        | 04/07/2026   | 04/07/2026      | AWS Documentation (CloudFront, S3, WAF)   |

### Kết quả đạt được tuần 11:

#### A. Hoàn thiện Kiến trúc Hệ thống (Architecture Finalization)
* Sửa thành công lỗi logic trong thiết kế luồng dữ liệu (Data Flow) theo góp ý của Admin: Tách biệt rõ ràng vai trò của CloudFront kết hợp S3 cho Frontend tĩnh, và luồng gọi tài nguyên Media trực tiếp.
* Chốt được sơ đồ kiến trúc dự án, chuẩn bị sẵn sàng cho quá trình báo cáo và nghiệm thu dự án cuối kỳ.

#### B. Triển khai thực tế lên Đám mây (Cloud Deployment)
* Đưa thành công toàn bộ hệ thống *Pet Resort & Care System* từ môi trường Local lên hạ tầng AWS thực tế.
* Hệ thống đã có thể truy cập mượt mà qua Internet bằng tên miền, các luồng gọi API từ Frontend xuống Backend và luồng truy xuất hình ảnh/media hoạt động trơn tru qua hệ thống CDN toàn cầu.
* Áp dụng thành công các nguyên tắc bảo mật (Zero Trust): Hoàn toàn không mở cổng SSH (Port 22), ẩn Database vào Private Subnet và sử dụng Secrets Manager để bảo mật thông tin đăng nhập.

#### C. Minh chứng triển khai (Deployment Evidence)

* **Sơ đồ tài nguyên VPC (VPC Resource Map):** Trực quan hóa cấu trúc các subnet, route table và gateway phục vụ cho thiết lập sẵn sàng cao Multi-AZ.
  ![VPC Resource Map](/images/1-Worklog/vpc_resource_map.png)

* **Nhóm bảo mật (Security Groups):** Các quy tắc tường lửa được cấu hình chi tiết cho ALB, Backend, Database và Cache.
  ![Security Groups](/images/1-Worklog/security_groups.png)

* **Ước tính chi phí RDS Database:** Chi tiết bảng tính toán chi phí hàng tháng trong quá trình thiết lập RDS MySQL.
  ![RDS Database Estimated Costs](/images/1-Worklog/rds_estimated_costs.png)

* **Khởi tạo RDS MySQL Instance:** Tiến trình khởi chạy cơ sở dữ liệu `petshop-database-1` trên môi trường AWS Console.
  ![RDS Instance Launching](/images/1-Worklog/rds_creating.png)

* **Kết nối & Chi tiết RDS Database:** Thông số kỹ thuật của cơ sở dữ liệu, hiển thị Endpoint nội bộ và phân vùng hoạt động.
  ![RDS Connectivity Details](/images/1-Worklog/rds_connectivity.png)