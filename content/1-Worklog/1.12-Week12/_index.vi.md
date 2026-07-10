---
title: "Worklog Tuần 12"
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Mục tiêu tuần 12:
* Hoàn thiện cấu hình giám sát (Monitoring) và kiểm thử sức chịu tải (Load Testing) cho hệ thống *Pet Resort & Care System* trên môi trường AWS.
* Thực hiện tối ưu chi phí (FinOps) bằng cách dọn dẹp tài nguyên rác.
* Tổng kết kiến thức toàn bộ 12 tuần thực tập, hoàn thiện tài liệu kỹ thuật và chuẩn bị slide/kịch bản cho buổi báo cáo nghiệm thu cuối kỳ.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| 2   | - Kiểm thử toàn diện (End-to-End Testing): Chạy smoke tests để kiểm tra luồng mua hàng, đặt lịch spa, thanh toán và kiểm tra kết nối từ Frontend (CloudFront) xuống Backend (ALB). | 06/07/2026   | 06/07/2026      | Kịch bản Test case của nhóm               |
| 3   | - Thiết lập Giám sát & Cảnh báo: Cấu hình Amazon CloudWatch (Dashboards) và tạo SNS Alarms gửi email cho Admin khi CPU của EC2 hoặc kết nối RDS vượt ngưỡng 80%.                            | 07/07/2026   | 07/07/2026      | AWS Documentation (CloudWatch, SNS)       |
| 4   | - Kiểm thử chịu tải (Load Testing): Giả lập lượng truy cập lớn đột ngột (Flash Sale) để kiểm tra cơ chế tự động mở rộng (Auto Scaling) của EC2 và khả năng Cache của Redis.               | 08/07/2026   | 08/07/2026      | Apache JMeter / Postman                   |
| 5   | - Tối ưu tài nguyên (FinOps): Dọn dẹp tài nguyên dư thừa (bucket thử nghiệm, snapshot cũ, Elastic IPs không dùng) để giữ chi phí dưới mức 130$/tháng.                                         | 09/07/2026   | 09/07/2026      | AWS Billing Console                       |
| 6   | - Hoàn thiện Deliverables: Viết file README hướng dẫn deploy, chốt tài liệu kiến trúc (Architecture Blueprint) và chuẩn bị Slide + kịch bản Demo cho buổi bảo vệ đồ án/nghiệm thu.          | 10/07/2026   | 10/07/2026      | Project Documentation                     |

### Kết quả đạt được tuần 12:

* **Hoàn thiện dự án (Ở mức đáp ứng cơ bản):** Hệ thống *Pet Resort & Care System* đã có thể vận hành ổn định và đáp ứng các luồng tính năng cốt lõi. Trong quá trình Load Test, cơ chế Auto Scaling đã hoạt động, tuy nhiên nhóm nhận thấy tốc độ scale-out đôi lúc vẫn còn độ trễ, cần phải tìm hiểu và tối ưu cấu hình kỹ hơn trong tương lai.
* **Giám sát & Tối ưu chi phí:** Thiết lập được luồng cảnh báo sự cố qua CloudWatch & SNS và dọn dẹp sạch sẽ tài nguyên rác. Dù vậy, hệ thống logging vẫn còn khá rời rạc, chưa tích hợp được các công cụ phân tích log tập trung chuyên sâu (như ELK stack).
* **Nhìn nhận thiếu sót & Bài học rút ra:** Nhìn lại hành trình 12 tuần, bản thân nhận thấy vẫn còn rất nhiều thiếu sót về tư duy tối ưu mã nguồn, chưa thiết lập được luồng CI/CD tự động hoàn toàn và các rủi ro bảo mật tiềm ẩn. Những kiến thức hiện tại mới chỉ là những viên gạch nền tảng ban đầu.
* **Tổng kết kỳ thực tập:** Chốt toàn bộ tài liệu kỹ thuật và sẵn sàng tâm lý cầu thị cho buổi bảo vệ đồ án. Đây sẽ là bước đệm quan trọng để bản thân tiếp tục đào sâu nghiên cứu các công nghệ nâng cao hơn như Containerization (Docker/EKS) và Microservices sau khi kết thúc thực tập.
##### Tuần 5 (18/05 – 24/05): Dịch vụ Compute AWS — EC2 vs Lambda
* Nghiên cứu chuyên sâu về **Mạng con (Subnets)** trong VPC: Phân loại Public, Private, VPN-only Subnet và quy tắc cấp phát dải IP (CIDR, 5 IP dự phòng của AWS).
* Tìm hiểu **NAT Gateway** kết hợp **Elastic IP** để cung cấp quyền truy cập Internet an toàn cho tài nguyên nằm trong Private Subnet.
* Đọc tài liệu tổng quan về **Amazon EC2**: Vòng đời của Instance (EC2 Lifecycle), các trạng thái hoạt động và cơ chế bảo mật **Key Pair**.
* Tìm hiểu khái niệm **Serverless** và cách thức hoạt động dựa trên sự kiện của dịch vụ **AWS Lambda**.
* Phân tích so sánh lý thuyết giữa **EC2** và **Lambda** về quản lý hạ tầng, cơ chế tự động co giãn (Scaling) và cách tính chi phí.
* Thảo luận nhóm và đánh giá: Ứng dụng Spring Boot (dự án Pet Resort) sẽ phù hợp với **EC2** (chạy trong Private Subnet qua NAT Gateway) hơn là Serverless Lambda.

##### Tuần 6 (25/05 – 29/05): Ôn tập kiến thức, CloudFront & phác thảo kiến trúc
* Lên văn phòng tham gia các buổi tự học, hệ thống hóa lại các thiết lập bảo mật tài khoản; kiểm tra cấu hình MFA và chính sách phân quyền IAM.
* Ôn tập chuyên sâu về **Amazon S3**: Cơ chế quản lý vòng đời đối tượng (Lifecycle Policies) và bảo mật Bucket.
* Thảo luận nhóm về mô hình VPC; rà soát lại lý thuyết phân chia Subnet và cách thức hoạt động của **Security Groups**.
* Tìm hiểu giải pháp phân phối Frontend tĩnh: So sánh giữa **S3 Static Hosting** thông thường và tích hợp **AWS Amplify**.
* Xác định định hướng: Sử dụng **Amazon S3 + CDN (CloudFront)** cho Frontend ReactJS để tối ưu chi phí.

##### Tuần 7 (01/06 – 05/06): Tích hợp Frontend-Backend, JWT & kiểm thử E2E
* Kết nối các trang hiển thị của **React Frontend** với API của **Spring Boot** thông qua lớp trung gian `services/api.js`; cấu hình **Axios base URL** trỏ về Backend.
* Xây dựng luồng **Đăng nhập/Đăng ký** hoàn chỉnh (`LoginPage`, `RegisterPage`); tích hợp cơ chế xử lý chuỗi mã báo hiệu xác thực **JWT** (`JwtResponse`, `JwtTokenProvider`) từ `AuthController` phía Backend vào `authStore.js` của Frontend.
* Kết nối trang danh mục hàng hóa (`ProductsPage`, `ProductCard`) với dữ liệu động từ `ProductController`; triển khai logic cho giỏ hàng `CartPage` thông qua `cartStore.js`.
* Xây dựng luồng đơn đặt hàng (`CheckoutPage`) và đặt lịch hẹn chăm sóc thú cưng (`BookingPage`); kết nối đến `OrderController` và `BookingController`.
* Kiểm thử toàn diện **(End-to-End Testing)** luồng trải nghiệm khách hàng: **Đăng ký → Đăng nhập → Thêm giỏ hàng → Đặt lịch Spa → Thanh toán hóa đơn**.
* Tối ưu hóa tệp `CorsConfig` để xử lý triệt để lỗi **CORS** giữa Frontend và Backend.

##### Tuần 8 (08/06 – 12/06): Đóng gói Spring Boot (.jar) & đánh giá Beanstalk vs EC2
* Tạm dừng code tính năng mới, bắt đầu tìm hiểu quy trình **Build và Đóng gói** ứng dụng Spring Boot; đọc tài liệu về **Maven Lifecycle** (Clean, Compile, Package).
* Thực hành chạy lệnh `mvn clean package` để đóng gói dự án Backend thành file `.jar`; xử lý các lỗi liên quan đến Test Cases khi build.
* Tắt IDE, mở **Command Prompt** và chạy file `.jar` bằng lệnh `java -jar petshop-backend.jar`; kiểm tra lại các API trên Postman để chắc chắn file chạy độc lập tốt.
* Tìm hiểu sơ bộ **AWS Elastic Beanstalk** (PaaS): Giải pháp tự động hóa giúp tải file `.jar` lên qua giao diện Web mà không cần gõ lệnh Linux.
* So sánh lợi ích/hạn chế giữa **Beanstalk** (dễ nhưng ít kiểm soát) và **EC2** (khó hơn nhưng học được nhiều).
* Sau khi tham vấn ý kiến **Mentor**, nhóm quyết định triển khai trực tiếp trên **Amazon EC2** thay vì dùng Beanstalk — tự tay cấu hình máy chủ Linux, Security Group và Load Balancer mang lại giá trị học tập lớn hơn.

---

#### GIAI ĐOẠN 3: TRIỂN KHAI CLOUD & TỰ ĐỘNG HÓA (Tuần 9 – 12)

##### Tuần 9 (15/06 – 21/06): Khởi tạo S3 Bucket, bảo mật mã nguồn & xử lý lỗi
* Nghiên cứu tổng quan dịch vụ **Amazon S3** (Simple Storage Service): Khái niệm Bucket, Object, Key và các trường hợp sử dụng phổ biến.
* Thực hành tạo S3 Bucket trên AWS Console: Nhập tên `aws-first-cloud-journey`, thiết lập vùng **ap-southeast-1 (Singapore)**, cấu hình **Object Ownership** ở trạng thái **ACLs disabled** theo khuyến nghị AWS.
* Ghi nhận bài học quan trọng: Tên S3 Bucket bắt buộc phải là **duy nhất trên toàn cầu (globally unique)**. Khi đặt tên trùng, hệ thống báo lỗi *"Bucket with the same name already exists"* — cần thêm hậu tố số để tránh trùng lặp.
* Rà soát và tối ưu hóa các lớp dịch vụ `ProductServiceImpl`, `BookingServiceImpl`; khắc phục lỗi **N+1 Query** trong JPA/Hibernate.
* Bảo mật tệp `application.yml`: Tách thông tin nhạy cảm (DB URL, Username, Password, JWT Secret Key) ra khỏi mã nguồn, chuyển sang sử dụng **biến môi trường hệ thống (Environment Variables)**.
* Hoàn thiện bộ lọc xử lý lỗi tập trung `GlobalExceptionHandler` và kiểm thử Postman với các kịch bản edge-case.

##### Tuần 10 (22/06 – 28/06): Cấu hình CloudFront, hoàn thiện kiến trúc & review cộng đồng
* Nghiên cứu dịch vụ **Amazon CloudFront**: Khái niệm CDN (Content Delivery Network), Edge Location, Distribution và cách tăng tốc phân phối nội dung tĩnh.
* Thực hành tạo **CloudFront Distribution**: Trỏ Origin về S3 Bucket `aws-first-cloud-journe...` đã tạo ở tuần trước. Distribution được tạo thành công với ID **E2NI0FJ3HELT9Z**, trạng thái **Enabled** và đang **Deploying**.
* Phân tích cấu trúc mã nguồn thực tế để phác thảo các phân lớp chức năng; vẽ bản nháp sơ đồ kiến trúc trên **Draw.io** với luồng CloudFront + S3.
* Truy cập cộng đồng **AWS Study Group** để đọc các bài đánh giá kiến trúc của các khóa trước; tổng hợp các lỗi thiết kế thường gặp từ comment review của Admin.
* Trực quan hóa luồng ứng dụng: **Route 53 → S3/CloudFront → RESTful API → Backend → RDS MySQL**.
* Loại bỏ các thành phần kiến trúc thừa (Lambda, DynamoDB từ bài mẫu) không khớp với mã nguồn Spring Boot của nhóm.

##### Tuần 11 (29/06 – 04/07): CloudFormation (IaC), chốt kiến trúc & triển khai lên cloud
* Tiếp nhận feedback từ Admin: Chỉnh sửa luồng CloudFront phân phối Frontend và Media; chốt bản vẽ kiến trúc AWS cuối cùng.
* Nghiên cứu dịch vụ **AWS CloudFormation**: Khái niệm Stack, Template (YAML/JSON) và quy trình tự động hóa tạo tài nguyên **(Infrastructure as Code)**.
* Thực hành tạo Stack trên CloudFormation Console: Cấu hình tham số **AvailabilityZone** (`us-east-1a`), **LatestAmiId** (Amazon Linux 2 AMI), **NotificationEmail**, **S3BucketName**, **S3KeyLambdaZip**.
* Tải lên S3 Bucket `aws-backup-lab13-fcj` hai file: `backup-lab.yaml` (mẫu cấu hình hạ tầng) và `lambda_function.zip` (mã nguồn xử lý) vào thư mục `Backup Plan/`.
* Stack `backup-plan-lab13` được khởi tạo ngày 27/10/2024; các thành phần **LambdaRole**, **SNSTopic**, **Instance**, **Route** đều đạt trạng thái **CREATE_COMPLETE**.
* **Triển khai toàn bộ hệ thống lên AWS thực tế:**
  * Lớp Mạng & Bảo mật: VPC, Public/Private Subnet (Multi-AZ), NAT Gateway, Security Groups, IAM Roles, KMS, Secrets Manager.
  * Lớp Dữ liệu: Amazon RDS MySQL (Multi-AZ, Sync Replication), ElastiCache Redis (Cache-Aside).
  * Lớp Tính toán: EC2 + Auto Scaling Group + Application Load Balancer (ALB).
  * Lớp Biên: S3 Frontend + S3 Media + CloudFront + AWS WAF.
* Áp dụng thành công nguyên tắc bảo mật **Zero Trust**: Không mở SSH (Port 22), ẩn Database vào Private Subnet, sử dụng Secrets Manager.

##### Tuần 12 (06/07 – 10/07): Load Testing, Monitoring, FinOps & Tổng kết dự án
* Kiểm thử toàn diện (E2E), kiểm thử sức chịu tải (Load Testing), cấu hình CloudWatch Dashboards + SNS Alarms.
* Tối ưu tài nguyên (FinOps), dọn dẹp tài nguyên rác; hoàn thiện tài liệu kỹ thuật và chuẩn bị bảo vệ đồ án.

---

#### Bảng tổng hợp nhanh 12 tuần:

| Tuần | Thời gian | Trọng tâm chính | Kỹ năng/Dịch vụ AWS |
|------|-----------|------------------|----------------------|
| 1 | 17/04 – 23/04 | Làm quen AWS & cài đặt môi trường | AWS Free Tier, IAM, Hugo, EC2 basics |
| 2 | 24/04 – 30/04 | Bảo mật tài khoản & quản lý chi phí | MFA, Root User, Admin Group, AWS CLI, Budgets |
| 3 | 01/05 – 07/05 | Amazon S3 & AWS Budgets chi tiết | S3 (`petshop-media-storage`), 4 loại Budget |
| 4 | 11/05 – 15/05 | VPC, RDS MySQL & Security Groups | VPC, Public/Private Subnet, RDS MySQL, SG |
| 5 | 18/05 – 24/05 | Compute Services: EC2 vs Lambda | Subnet, NAT Gateway, EC2 Lifecycle, Lambda |
| 6 | 25/05 – 29/05 | Ôn tập & phác thảo kiến trúc | IAM/S3/VPC/EC2 review, S3 Static Hosting, CDN |
| 7 | 01/06 – 05/06 | Tích hợp Frontend-Backend & JWT | ReactJS + Spring Boot, JWT Auth, E2E Testing |
| 8 | 08/06 – 12/06 | Đóng gói .jar & lựa chọn dịch vụ | Maven, `.jar`, Beanstalk vs EC2, chọn EC2 |
| 9 | 15/06 – 21/06 | S3 Bucket & bảo mật mã nguồn | S3 `aws-first-cloud-journey`, ACLs, env vars |
| 10 | 22/06 – 28/06 | CloudFront & hoàn thiện kiến trúc | CloudFront Distribution, Draw.io, community review |
| 11 | 29/06 – 04/07 | CloudFormation (IaC) & deploy Cloud | CloudFormation Stack, VPC Multi-AZ, full deploy |
| 12 | 06/07 – 10/07 | Load Test, Monitoring & Tổng kết | CloudWatch, SNS, FinOps, project defense |

---

#### Các dịch vụ AWS đã sử dụng trong suốt dự án:

| Nhóm dịch vụ | Dịch vụ cụ thể | Vai trò trong dự án |
|--------------|-----------------|---------------------|
| **Tính toán (Compute)** | Amazon EC2, Auto Scaling Group | Chạy Spring Boot Backend, tự động co giãn theo tải |
| **Lưu trữ (Storage)** | Amazon S3 | Lưu trữ Frontend tĩnh (ReactJS), ảnh thú cưng, hóa đơn, template CloudFormation |
| **Cơ sở dữ liệu (Database)** | Amazon RDS MySQL, ElastiCache (Redis) | Lưu trữ dữ liệu quan hệ (Multi-AZ), caching hiệu suất cao |
| **Mạng & CDN** | Amazon VPC, CloudFront, Route 53, ALB, NAT Gateway | Phân vùng mạng bảo mật, phân phối nội dung toàn cầu, cân bằng tải |
| **Bảo mật (Security)** | IAM, Security Groups, KMS, Secrets Manager, AWS WAF, MFA | Phân quyền, tường lửa, mã hóa dữ liệu, bảo vệ ứng dụng web |
| **Giám sát (Monitoring)** | Amazon CloudWatch, SNS | Dashboard giám sát CPU/Memory/Network, cảnh báo sự cố qua email |
| **Tự động hóa (IaC)** | AWS CloudFormation | Triển khai hạ tầng tự động bằng template YAML (`backup-lab.yaml`) |
| **Quản lý chi phí** | AWS Budgets, Billing Console | Kiểm soát ngân sách (Cost/Usage/RI/Savings Plans), cảnh báo vượt mức |