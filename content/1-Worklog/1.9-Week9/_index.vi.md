---
title: "Worklog Tuần 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:
* Tìm hiểu dịch vụ lưu trữ đối tượng **Amazon S3** và thực hành khởi tạo S3 Bucket phục vụ cho việc lưu trữ ảnh thú cưng, hóa đơn của dự án Pet Resort & Care.
* Tối ưu hóa cấu hình bảo mật mã nguồn Backend và hiệu suất truy vấn cơ sở dữ liệu trên môi trường phát triển cục bộ (Local).
* Nghiên cứu các quy tắc đặt tên, quản lý quyền sở hữu và chính sách truy cập trên Amazon S3.

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Rà soát các lớp dịch vụ `ProductServiceImpl`, `BookingServiceImpl` phía Backend.<br>- Kiểm tra và tối ưu hóa các câu truy vấn JPA/Hibernate liên quan đến bảng đơn hàng và lịch hẹn để tránh lỗi N+1 Query. | 15/06/2026 | 15/06/2026 | Spring Data JPA Guide |
| 2 | - Nghiên cứu tổng quan dịch vụ **Amazon S3** (Simple Storage Service): Tìm hiểu khái niệm Bucket, Object, Key và các trường hợp sử dụng phổ biến (lưu trữ tĩnh, sao lưu dữ liệu, phân phối nội dung).<br>- Đọc tài liệu AWS về quy tắc đặt tên S3 Bucket (phải là duy nhất toàn cầu – globally unique). | 16/06/2026 | 16/06/2026 | Tài liệu Amazon S3 |
| 3 | - Thực hành tạo S3 Bucket trên AWS Console: Nhập tên `aws-first-cloud-journey`, thiết lập Vùng khả dụng là **Châu Á Thái Bình Dương - Singapore (ap-southeast-1)**.<br>- Cấu hình Object Ownership ở trạng thái **ACLs disabled** theo khuyến nghị của AWS. Xử lý lỗi trùng tên bucket bằng cách thêm hậu tố số để đảm bảo tính duy nhất. | 17/06/2026 | 18/06/2026 | Bài thực hành FCJ - S3 |
| 4 | - Tiến hành bảo mật tệp `application.yml` bằng cách tách các thông tin nhạy cảm (URL kết nối DB, Username, Password, Secret Key của JWT Provider) ra khỏi mã nguồn thuần túy.<br>- Chuyển đổi cấu hình sang dạng sử dụng các biến môi trường hệ thống (Environment Variables). | 19/06/2026 | 19/06/2026 | AWS Security Best Practices |
| 5 | - Sử dụng công cụ Postman để kiểm thử các kịch bản lỗi cục bộ (Error Scenarios): Giả lập gửi Token JWT hết hạn, truyền dữ liệu không hợp lệ vào API đặt lịch.<br>- Hoàn thiện bộ lọc xử lý lỗi tập trung `GlobalExceptionHandler`, cập nhật tiến độ lên trang Hugo. | 20/06/2026 | 21/06/2026 | Guide to API Error Handling |

### Kết quả đạt được tuần 9:

* **Nắm vững kiến thức nền tảng về Amazon S3 (S3 Bucket Initialization & Naming Rules):**
  * Hiểu rõ Amazon S3 là dịch vụ lưu trữ đối tượng với khả năng mở rộng gần như không giới hạn, phù hợp để lưu trữ ảnh thú cưng, hóa đơn và các tài liệu tĩnh cho dự án Pet Resort & Care.
  * Thực hành thành công quy trình tạo S3 Bucket trên AWS Console: Nhập tên `aws-first-cloud-journey`, thiết lập vùng **ap-southeast-1 (Singapore)**, và cấu hình **Object Ownership** ở trạng thái **ACLs disabled** đúng theo khuyến nghị bảo mật của AWS.
  * Ghi nhận bài học quan trọng: Tên S3 Bucket bắt buộc phải là **duy nhất trên toàn cầu (globally unique)**. Khi đặt tên trùng với bucket đã tồn tại, hệ thống sẽ báo lỗi màu đỏ *"Bucket with the same name already exists"* và yêu cầu thêm số vào sau tên để tránh trùng lặp.

* **Tối ưu hóa cấu hình và hiệu suất ứng dụng cục bộ (Local Performance Tuning):**
  * Tối ưu hóa thành công cơ chế nạp dữ liệu liên kết (FetchType) trong các thực thể JPA (như phân hệ `Order` và `Booking`), giúp giảm đáng kể số lượng truy vấn thừa xuống cơ sở dữ liệu local.
  * Triển khai giải pháp che giấu thông tin nhạy cảm: Loại bỏ hoàn toàn việc viết cứng (Hardcode) tài khoản cơ sở dữ liệu và mã khóa bí mật JWT trong file cấu hình, chuyển sang nạp động thông qua biến môi trường hệ thống.

* **Hoàn thiện khả năng xử lý lỗi và kiểm thử mã nguồn (Robust Error Handling Verified):**
  * Nâng cấp phân hệ bắt ngoại lệ `GlobalExceptionHandler`: Đảm bảo tất cả lỗi hệ thống (lỗi sai định dạng dữ liệu, lỗi phân quyền truy cập, lỗi `ResourceNotFoundException`) đều trả về cấu trúc JSON phản hồi đồng nhất dạng `ApiResponse`.
  * Xác minh tính ổn định của ứng dụng thông qua chuỗi kiểm thử Postman với các tham số edge-case, đảm bảo backend không bị sập nguồn (Crash) đột ngột khi nhận dữ liệu xấu.

* **Chuẩn bị sẵn sàng tài liệu hạ tầng:**
  * Tài liệu hóa toàn bộ danh mục các biến môi trường cần thiết cùng thông tin cấu hình S3 để chuẩn bị cho việc tích hợp đồng bộ lên hệ thống AWS trong các giai đoạn tiếp theo.