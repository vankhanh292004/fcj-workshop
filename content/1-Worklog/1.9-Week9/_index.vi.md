---
title: "Worklog Tuần 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:
* Tối ưu hóa cấu hình bảo mật mã nguồn và hiệu suất truy vấn cơ sở dữ liệu local cho dự án Pet Resort & Care.
* Nghiên cứu lý thuyết về các công cụ giám sát (Monitoring) và ghi nhật ký hệ thống (Logging) trên AWS.
* Thực hiện kiểm thử các kịch bản ngoại lệ (Edge Cases) dưới môi trường local để chuẩn bị cho việc triển khai diện rộng.

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Rà soát các lớp dịch vụ `ProductServiceImpl`, `BookingServiceImpl` phía Backend.<br>- Kiểm tra và tối ưu hóa các câu truy vấn JPA/Hibernate liên quan đến bảng đơn hàng và lịch hẹn để tránh lỗi N+1 Query. | 15/06/2026 | 15/06/2026 | Spring Data JPA Guide |
| 2 | - Tìm hiểu lý thuyết dịch vụ giám sát **Amazon CloudWatch**.<br>- Nghiên cứu các khái niệm cơ bản: CloudWatch Metrics (CPU Utilization, Network In/Out), Log Groups và cơ chế hoạt động của CloudWatch Alarms. | 16/06/2026 | 16/06/2026 | Tài liệu Amazon CloudWatch |
| 3 | - Tiến hành bảo mật tệp `application.yml` bằng cách tách các thông tin nhạy cảm (URL kết nối DB, Username, Password, Secret Key của JWT Provider) ra khỏi mã nguồn thuần túy.<br>- Chuyển đổi cấu hình sang dạng sử dụng các biến môi trường hệ thống (Environment Variables). | 17/06/2026 | 17/06/2026 | AWS Security Best Practices |
| 4 | - Tìm hiểu cách xây dựng **Amazon CloudWatch Dashboard** để giám sát máy chủ EC2 và Application Load Balancer.<br>- Học cách tạo Dashboard tùy chỉnh kết hợp các chỉ số CPU, Memory, Network và trạng thái Health Check của ALB phục vụ công tác quản trị sau này. | 18/06/2026 | 18/06/2026 | AWS CloudWatch Dashboard Docs |
| 5 | - Sử dụng công cụ Postman để thực hiện kiểm thử diện rộng các kịch bản lỗi cục bộ (Error Scenarios): Giả lập gửi Token JWT hết hạn, truyền dữ liệu không hợp lệ vào API đặt lịch.<br>- Hoàn thiện bộ lọc xử lý lỗi tập trung `GlobalExceptionHandler` và cập nhật Hugo. | 19/06/2026 | 19/06/2026 | Guide to API Error Handling |

### Kết quả đạt được tuần 9:

* **Tối ưu hóa cấu hình và hiệu suất ứng dụng cục bộ (Local Performance Tuning):**
  * Tối ưu hóa thành công cơ chế nạp dữ liệu liên kết (FetchType) trong các thực thể JPA (như phân hệ `Order` và `Booking`), giúp giảm số lượng truy vấn thừa xuống cơ sở dữ liệu local.
  * Triển khai giải pháp che giấu thông tin nhạy cảm: Loại bỏ hoàn toàn việc viết cứng (Hardcode) tài khoản cơ sở dữ liệu và mã khóa bí mật JWT trong file cấu hình, chuyển cấu trúc sang nạp động thông qua biến môi trường để đảm bảo không rò rỉ dữ liệu khi push code lên GitHub.

* **Tiếp thu nền tảng kiến thức về giám sát hệ thống (Monitoring & Observability Foundations):**
  * Hiểu được cách thức **Amazon CloudWatch** thu thập các chỉ số tài nguyên từ máy chủ theo thời gian thực để người quản trị đưa ra quyết định nâng cấp hoặc hạ cấp cấu hình dòng máy EC2.
  * Nắm được bản chất của Log Groups và cách hệ thống quản lý tập trung nhật ký hoạt động (Application Logs), hỗ trợ đắc lực cho việc định vị nguyên nhân gây ra lỗi (Debugging) sau khi đưa ứng dụng lên đám mây.

* **Hoàn thiện khả năng xử lý lỗi và kiểm thử mã nguồn (Robust Error Handling Verified):**
  * Nâng cấp phân hệ bắt ngoại lệ `GlobalExceptionHandler`: Đảm bảo tất cả các lỗi từ hệ thống (lỗi sai định dạng dữ liệu, lỗi phân quyền truy cập, lỗi không tìm thấy tài nguyên `ResourceNotFoundException`) đều trả về cấu trúc JSON phản hồi đồng nhất dạng `ApiResponse`.
  * Xác minh tính ổn định của ứng dụng thông qua chuỗi kiểm thử Postman với các tham số edge-case, đảm bảo backend không bị sập nguồn (Crash) đột ngột khi gặp dữ liệu xấu.

* **Chuẩn bị sẵn sàng tài liệu hạ tầng:**
  * Tài liệu hóa toàn bộ danh mục các biến môi trường cần thiết để chuẩn bị cho việc cấu hình đồng bộ lên hệ thống Web Console của AWS trong các giai đoạn tiếp theo.