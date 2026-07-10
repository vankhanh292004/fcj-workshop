---
title: "Worklog Tuần 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu tuần 10:
* Tìm hiểu và thực hành cấu hình dịch vụ **Amazon CloudFront** để tăng tốc độ phân phối nội dung tĩnh cho dự án Pet Resort & Care.
* Phác thảo, hiệu chỉnh và hoàn thiện sơ đồ kiến trúc hệ thống (Architecture Diagram) dựa trên kiến thức S3 và CloudFront đã học.
* Rà soát luồng đi của dữ liệu trên sơ đồ, đảm bảo tính nhất quán với các dịch vụ AWS đã nghiên cứu ở các tuần trước.

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Nghiên cứu tổng quan dịch vụ **Amazon CloudFront**: Tìm hiểu khái niệm CDN (Content Delivery Network), Edge Location, Distribution và cách CloudFront tăng tốc phân phối nội dung tĩnh cho website.<br>- Đọc tài liệu AWS về các trường hợp sử dụng CloudFront cho website tĩnh (Accelerate Static Websites). | 22/06/2026 | 22/06/2026 | Tài liệu Amazon CloudFront |
| 2 | - Thực hành tạo **CloudFront Distribution** trên AWS Console: Trỏ nguồn dữ liệu gốc (Origin) về S3 Bucket `aws-first-cloud-journe...` đã tạo ở tuần trước.<br>- Distribution được tạo thành công với ID là **E2NI0FJ3HELT9Z**, trạng thái hoạt động là **Enabled** và đang trong quá trình triển khai (**Deploying**). | 23/06/2026 | 24/06/2026 | Bài thực hành FCJ - CloudFront |
| 3 | - Phân tích cấu trúc thư mục mã nguồn thực tế của dự án để phác thảo các phân lớp chức năng (Frontend ReactJS, Backend Spring Boot, Database MySQL).<br>- Vẽ bản nháp đầu tiên của sơ đồ kiến trúc trên Draw.io, tích hợp luồng CloudFront + S3 vào sơ đồ. | 25/06/2026 | 25/06/2026 | Sơ đồ khối hệ thống |
| 4 | - Lên văn phòng và truy cập cộng đồng AWS Study Group để đọc các bài đánh giá kiến trúc của các khóa trước.<br>- Tổng hợp các lỗi thiết kế hệ thống thường gặp thông qua các comment review của Admin, đối chiếu với cách tích hợp CloudFront trong sơ đồ của nhóm. | 26/06/2026 | 26/06/2026 | Cộng đồng AWS Study Group |
| 5 | - Chỉnh sửa và tối ưu hóa sơ đồ kiến trúc: Phân tách rõ ràng phân vùng mạng ảo VPC, vị trí đặt máy chủ trên nhiều Availability Zones, cơ sở dữ liệu RDS MySQL, và luồng CloudFront phân phối Frontend.<br>- Hoàn thiện bản vẽ kiến trúc tổng quan cấp độ nhóm và cập nhật tiến độ lên Hugo. | 27/06/2026 | 28/06/2026 | AWS Architecture Icon Set |

### Kết quả đạt được tuần 10:

#### Nắm vững cấu hình Amazon CloudFront cho Website tĩnh (CloudFront Distribution Setup)
* **Hiểu rõ vai trò của CloudFront trong kiến trúc hệ thống:**
  * Nắm được CloudFront là dịch vụ CDN toàn cầu của AWS, giúp phân phối nội dung tĩnh (HTML, CSS, JS, hình ảnh) từ các Edge Location gần người dùng nhất, giảm đáng kể độ trễ truy cập cho dự án Pet Resort & Care.
  * Hiểu được mục tiêu chính của bước này là tạo một **CloudFront Distribution** nhằm phân phối nội dung đang được lưu trữ trên S3 Bucket đã tạo ở tuần trước.
* **Thực hành thành công trên AWS Console:**
  * Trên bảng điều khiển CloudFront, một bản phân phối (Distribution) đã được tạo thành công với ID **E2NI0FJ3HELT9Z**.
  * Nguồn dữ liệu gốc (Origin) của bản phân phối này trỏ về tên `aws-first-cloud-journe...` (S3 Bucket đã khởi tạo).
  * Trạng thái hoạt động (Status) đã chuyển sang **Enabled**, và trạng thái cập nhật (Last modified) ghi nhận quá trình **Deploying** thành công.

#### Nghiên cứu và tối ưu hóa sơ đồ kiến trúc hệ thống (Architecture Blueprinting)
* **Chuẩn hóa luồng phân phối dữ liệu thực tế:**
  * Trực quan hóa thành công luồng đi của ứng dụng: Người dùng truy cập tên miền qua Route 53 -> Tải giao diện tĩnh từ phân vùng lưu trữ S3/CloudFront -> Gọi các RESTful API xuống tầng xử lý máy chủ.
  * Phân tách rõ ràng ranh giới bảo mật mạng (Network Isolation): Đặt các cổng tiếp nhận lưu lượng công cộng ở Public Subnet và cô lập hoàn toàn tầng xử lý mã nguồn backend cùng cơ sở dữ liệu RDS MySQL trong Private Subnet.
* **Đối chiếu và sửa đổi lỗi logic hệ thống:**
  * Loại bỏ các thành phần kiến trúc bị vẽ thừa hoặc quá phức tạp (như các dịch vụ Serverless tự động Lambda, DynamoDB của bài mẫu) không khớp với mã nguồn Spring Boot truyền thống của nhóm, tránh rủi ro bị Admin chất vấn khi bảo vệ tiến độ.

####  Tiếp thu kiến thức từ phản hồi cộng đồng (Community Review Insights)
* Nghiên cứu kỹ lưỡng các comment góp ý của Admin AWS Study Group trên các sơ đồ hạ tầng tương tự để rút kinh nghiệm cho dự án nhóm.
* Nắm rõ các lỗi chí mạng thường gặp khi vẽ sơ đồ: Mũi tên chỉ ngược luồng dữ liệu, đặt cơ sở dữ liệu quan hệ ở Public Subnet, hoặc cấu hình sai quy tắc điều hướng của tường lửa Security Groups.
* Đảm bảo sự liên kết chặt chẽ giữa lý thuyết hạ tầng đám mây (S3, CloudFront) và cấu trúc code local hiện tại của dự án.