---
title: "Worklog Tuần 11"
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

* Tìm hiểu và thực hành **tự động hóa hạ tầng (Infrastructure as Code)** với dịch vụ **AWS CloudFormation** để triển khai tài nguyên AWS theo mẫu cấu hình.
* Tiếp nhận đánh giá (feedback) từ Admin/Mentor để chỉnh sửa và chốt sơ đồ kiến trúc AWS cuối cùng.
* Tiến hành triển khai (Deploy) toàn bộ dự án Pet Resort & Care System lên môi trường Cloud thực tế dựa trên kiến trúc đã chốt.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Tiếp nhận feedback từ admin: Chỉnh sửa lại luồng CloudFront phân phối nội dung Frontend và Media để tránh lỗi flow; vẽ lại các line kết nối cho trực quan.<br>- Chốt bản vẽ kiến trúc AWS cuối cùng. | 29/06/2026   | 29/06/2026      | Feedback từ Admin AWS Study Group         |
| 3   | - Nghiên cứu dịch vụ **AWS CloudFormation**: Tìm hiểu khái niệm Stack, Template (YAML/JSON) và quy trình tự động hóa tạo tài nguyên (IaC).<br>- Thực hành tạo Stack trên CloudFormation Console: Cấu hình các tham số **AvailabilityZone** (`us-east-1a`), **LatestAmiId** (Amazon Linux 2 AMI), Email nhận thông báo và tên S3 Bucket. | 30/06/2026   | 01/07/2026      | Bài thực hành FCJ - CloudFormation        |
| 4   | - Tải lên S3 Bucket `aws-backup-lab13-fcj` hai file quan trọng: `backup-lab.yaml` (mẫu cấu hình hạ tầng) và `lambda_function.zip` (mã nguồn xử lý) vào thư mục `Backup Plan/`.<br>- Triển khai stack `backup-plan-lab13` trên CloudFormation, theo dõi quá trình tạo tài nguyên (CREATE_IN_PROGRESS). | 01/07/2026   | 02/07/2026      | AWS Documentation (CloudFormation, S3)    |
| 5   | - Triển khai lớp Tính toán (Compute Tier): Đưa mã nguồn Backend Spring Boot lên EC2.<br>- Cấu hình Auto Scaling Group và điều phối traffic bằng Application Load Balancer (ALB).<br>- Xác minh các sự kiện CloudFormation: LambdaRole, SNSTopic, Instance, Route đều đạt trạng thái **CREATE_COMPLETE**. | 02/07/2026   | 03/07/2026      | AWS Documentation (EC2, ALB, Auto Scaling)|
| 7   | - Triển khai lớp Biên (Edge): Upload mã nguồn tĩnh ReactJS lên S3 Frontend, tạo S3 Media.<br>- Cấu hình CloudFront phân luồng request và gắn tường lửa AWS WAF để bảo vệ hệ thống.        | 04/07/2026   | 04/07/2026      | AWS Documentation (CloudFront, S3, WAF)   |

### Kết quả đạt được tuần 11:

#### Nắm vững tự động hóa hạ tầng với AWS CloudFormation (Infrastructure as Code)
* **Hiểu rõ quy trình triển khai hạ tầng tự động:**
  * Khi cấu hình tạo Stack trong CloudFormation, hệ thống yêu cầu bắt buộc phải nhập tên Stack (*Stack name is required*).
  * Quá trình triển khai yêu cầu các tham số (Parameters) cụ thể bao gồm vùng **AvailabilityZone** (đang cấu hình `us-east-1a`) và mã **LatestAmiId** (đường dẫn tới Amazon Linux 2 AMI).
  * Các tham số bổ sung cần điền: **NotificationEmail** (Email nhận thông báo), **S3BucketName** (Tên S3 Bucket) và **S3KeyLambdaZip** (đường dẫn file Zip chứa code Lambda).
* **Thực hành trên S3 và CloudFormation Console:**
  * Trong giao diện S3, bucket `aws-backup-lab13-fcj` đã được tạo và chứa thư mục `Backup Plan/` với hai file quan trọng: `backup-lab.yaml` (mẫu cấu hình hạ tầng) và `lambda_function.zip` (mã nguồn xử lý tự động).
  * Giao diện CloudFormation cho thấy stack `backup-plan-lab13` đã được khởi tạo thành công vào ngày 27 tháng 10 năm 2024, trạng thái ban đầu là **CREATE_IN_PROGRESS**.
  * Mục Sự kiện (Events) của stack hiển thị lịch sử tạo tài nguyên: các thành phần **LambdaRole**, **SNSTopic**, **Instance**, và **Route** đều đạt trạng thái **CREATE_COMPLETE**.

##### Hoàn thiện Kiến trúc Hệ thống (Architecture Finalization)
* Sửa thành công lỗi logic trong thiết kế luồng dữ liệu (Data Flow) theo góp ý của Admin: Tách biệt rõ ràng vai trò của CloudFront kết hợp S3 cho Frontend tĩnh, và luồng gọi tài nguyên Media trực tiếp.
* Chốt được sơ đồ kiến trúc dự án, chuẩn bị sẵn sàng cho quá trình báo cáo và nghiệm thu dự án cuối kỳ.

####  Triển khai thực tế lên Đám mây (Cloud Deployment)
* Đưa thành công toàn bộ hệ thống *Pet Resort & Care System* từ môi trường Local lên hạ tầng AWS thực tế.
* Hệ thống đã có thể truy cập mượt mà qua Internet bằng tên miền, các luồng gọi API từ Frontend xuống Backend và luồng truy xuất hình ảnh/media hoạt động trơn tru qua hệ thống CDN toàn cầu.
* Áp dụng thành công các nguyên tắc bảo mật (Zero Trust): Hoàn toàn không mở cổng SSH (Port 22), ẩn Database vào Private Subnet và sử dụng Secrets Manager để bảo mật thông tin đăng nhập.

####  Minh chứng triển khai (Deployment Evidence)

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