---
title: "Worklog Tuần 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu tuần 10:
* Tập trung phân tích, phác thảo và hiệu chỉnh sơ đồ kiến trúc hệ thống (Architecture Diagram) cho dự án Pet Resort & Care.
* Nghiên cứu và tham khảo các bài viết, nhận xét (Comments) của các Admin trên cộng đồng AWS Study Group để tối ưu hóa thiết kế.
* Rà soát toàn bộ luồng đi của dữ liệu trên sơ đồ, đảm bảo tính nhất quán với định hướng hạ tầng đơn giản đã nghiên cứu ở Tuần 8 và Tuần 9.

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Phân tích cấu trúc thư mục mã nguồn thực tế của dự án để phác thảo các phân lớp chức năng (Frontend ReactJS, Backend Spring Boot, Database MySQL).<br>- Vẽ bản nháp đầu tiên của sơ đồ trên Draw.io. | 22/06/2026 | 22/06/2026 | Sơ đồ khối hệ thống |
| 2 | - Lên văn phòng và truy cập cộng đồng AWS Study Group để đọc các bài đánh giá kiến trúc của các khóa trước.<br>- Tổng hợp các lỗi thiết kế hệ thống thường gặp thông qua các comment review của Admin. | 23/06/2026 | 23/06/2026 | Cộng đồng AWS Study Group |
| 3 | - Đối chiếu sơ đồ kiến trúc của nhóm với phần mã nguồn thực tế; rà soát xem luồng kết nối có bị quá sức hoặc xuất hiện các dịch vụ không có trong code hay không.<br>- Kiểm tra tính logic của các mũi tên chỉ luồng API. | 24/06/2026 | 24/06/2026 | |
| 4 | - Thực hiện chỉnh sửa, tối ưu hóa sơ đồ: Phân tách rõ ràng phân vùng mạng ảo VPC, vị trí đặt máy chủ trên nhiều Vùng sẵn sàng (Availability Zones) và cơ sở dữ liệu RDS MySQL nhằm bám sát định hướng kiến trúc High Availability. | 25/06/2026 | 25/06/2026 | AWS Architecture Icon Set |
| 5 | - Hoàn thiện bản vẽ kiến trúc tổng quan (Architecture Blueprint) cấp độ nhóm.<br>- Viết tài liệu mô tả ngắn gọn luồng tương tác giữa các thành viên, rà soát lại toàn bộ hệ thống và cập nhật tiến độ tuần lên Hugo. | 26/06/2026 | 26/06/2026 | |

### Kết quả đạt được tuần 10:

#### A. Nghiên cứu và tối ưu hóa sơ đồ kiến trúc hệ thống (Architecture Blueprinting)
* **Chuẩn hóa luồng phân phối dữ liệu thực tế:**
  * Trực quan hóa thành công luồng đi của ứng dụng: Người dùng truy cập tên miền qua Route 53 -> Tải giao diện tĩnh từ phân vùng lưu trữ S3/CloudFront -> Gọi các RESTful API xuống tầng xử lý máy chủ.
  * Phân tách rõ ràng ranh giới bảo mật mạng (Network Isolation): Đặt các cổng tiếp nhận lưu lượng công cộng ở Public Subnet và cô lập hoàn toàn tầng xử lý mã nguồn backend cùng cơ sở dữ liệu RDS MySQL trong Private Subnet.
* **Đối chiếu và sửa đổi lỗi logic hệ thống:**
  * Loại bỏ các thành phần kiến trúc bị vẽ thừa hoặc quá phức tạp (như các dịch vụ Serverless tự động Lambda, DynamoDB của bài mẫu) không khớp với mã nguồn Spring Boot truyền thống của nhóm, tránh rủi ro bị Admin chất vấn khi bảo vệ tiến độ.

#### B. Tiếp thu kiến thức từ phản hồi cộng đồng (Community Review Insights)
* **Học hỏi từ các bài đánh giá thực chiến:**
  * Nghiên cứu kỹ lưỡng các comment góp ý của Admin AWS Study Group trên các sơ đồ hạ tầng tương tự để rút kinh nghiệm cho dự án nhóm.
  * Nắm rõ các lỗi chí mạng thường gặp khi vẽ sơ đồ: Mũi tên chỉ ngược luồng dữ liệu, đặt cơ sở dữ liệu quan hệ ở Public Subnet, hoặc cấu hình sai quy tắc điều hướng của tường lửa Security Groups.

#### C. Định hình phương án triển khai thực tế (Deployment Alignment)
* Đảm bảo sự liên kết chặt chẽ giữa lý thuyết hạ tầng đám mây và cấu trúc code local hiện tại của dự án. 
* Giữ vững tiêu chí thiết kế hệ thống tối giản, thực tế, tập trung vào việc lưu trữ ảnh thú cưng/hóa đơn qua S3 và chạy ứng dụng Spring Boot ổn định, giúp nhóm tự tin làm chủ cấu trúc hệ thống mà không bị quá tải về mặt kiến thức.