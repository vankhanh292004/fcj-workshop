---
title: "Worklog Tuần 8"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:
* Hoàn tất việc đóng gói mã nguồn Spring Boot của dự án Pet Resort & Care thành tệp thực thi độc lập (.jar) ngay trên máy cá nhân.
* Nghiên cứu và so sánh các giải pháp triển khai Backend: PaaS (AWS Elastic Beanstalk) vs IaaS (Amazon EC2).
* Thực hành các lệnh Linux cơ bản (`pscp`, `chmod`, `ping`) và tìm hiểu về lưu trữ EC2 Instance Store.
* Cấu hình hạ tầng mạng AWS (VPC Route Tables, Transit Gateway) để chuẩn bị môi trường triển khai thực tế theo hướng dẫn của mentor.

### Nhiệm vụ thực hiện trong tuần:

| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| 1 | - Thực hành dòng lệnh Linux: Sử dụng công cụ `pscp` trên Windows để copy file khóa bảo mật (`.pem`/`.ppk`) lên thư mục `/home/ec2-user/` của máy chủ EC2.<br>- Thiết lập bảo mật SSH bằng lệnh `chmod 400` cho file khóa và dùng `ping amazon.com` để kiểm tra kết nối mạng. | 08/06/2026 | 08/06/2026 | Linux Command Line Guide |
| 2 | - Thiết lập hạ tầng mạng trên AWS VPC Console.<br>- Cấu hình **VPC Route Tables** cho các mạng độc lập (First, Second, Third, Fourth VPC) và định tuyến lưu lượng (`0.0.0.0/0`) tập trung về **Transit Gateway**. | 09/06/2026 | 09/06/2026 | AWS VPC & Transit Gateway |
| 3 | - Tạm dừng việc code tính năng mới, bắt đầu tìm hiểu quy trình Build và Đóng gói một ứng dụng Spring Boot.<br>- Đọc tài liệu về Maven Lifecycle (Clean, Compile, Package). | 10/06/2026 | 10/06/2026 | Spring Boot Maven Documentation |
| 4 | - Thực hành chạy lệnh `mvn clean package` trên Terminal của VS Code / IntelliJ để đóng gói dự án Backend Pet Shop thành file `.jar`.<br>- Xử lý các lỗi lặt vặt liên quan đến Test Cases trong quá trình build. | 11/06/2026 | 11/06/2026 | StackOverflow / Java Blogs |
| 5 | - Đóng công cụ lập trình (IDE), mở Command Prompt của Windows và thử chạy file `.jar` vừa build bằng lệnh `java -jar petshop-backend.jar`.<br>- Kiểm tra lại các API trên Postman để đảm bảo file độc lập chạy trơn tru. | 12/06/2026 | 12/06/2026 | Java Documentation |
| 6 | - Tìm hiểu sơ bộ **AWS Elastic Beanstalk** (PaaS) — giải pháp tự động hóa giúp tải file `.jar` lên qua giao diện Web.<br>- So sánh ưu nhược điểm giữa Beanstalk và **Amazon EC2** (IaaS). | 13/06/2026 | 13/06/2026 | AWS Elastic Beanstalk Guide |
| 7 | - Sau khi tham vấn ý kiến mentor, quyết định triển khai trực tiếp trên **Amazon EC2** để tối đa hóa giá trị học tập thực tế.<br>- Nghiên cứu đặc tính lưu trữ của **EC2 Instance Store**: ổ NVMe tốc độ cao nhưng mất dữ liệu khi stop máy (không phù hợp cho database chính). | 14/06/2026 | 14/06/2026 | Amazon EC2 & Storage Docs |

### Kết quả đạt được tuần 8:

* **Hoàn thiện kỹ năng đóng gói ứng dụng Local (Application Packaging):** Sử dụng thành công Maven để build dự án thành file `.jar` và chạy độc lập qua dòng lệnh.
* **Hình thành tư duy lựa chọn dịch vụ đám mây (Cloud Service Selection Mindset):** Phân biệt được IaaS và PaaS, hiểu rõ tính chất "bay hơi" (ephemeral) của dữ liệu Instance Store để có chiến lược lưu trữ an toàn cho cơ sở dữ liệu.
* **Làm chủ cấu hình mạng & Linux Server:** Thực hiện thành công việc truyền file từ xa (`pscp`), thiết lập quyền bảo mật (`chmod 400`), và thiết lập định tuyến trung tâm giữa các VPC thông qua Transit Gateway.
* **Xác định rõ lộ trình triển khai:** Theo lời khuyên từ mentor, nhóm đã chuẩn bị sẵn sàng hạ tầng mạng và server EC2 cơ bản, tạo tiền đề để đưa dự án lên môi trường cloud vào tuần sau.