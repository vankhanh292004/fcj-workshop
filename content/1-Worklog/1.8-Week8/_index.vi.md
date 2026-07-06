---
title: "Worklog Tuần 8"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:
* Hoàn tất việc đóng gói mã nguồn Spring Boot của dự án Pet Resort & Care thành tệp thực thi độc lập (.jar) ngay trên máy cá nhân.
* Nghiên cứu và so sánh các giải pháp triển khai Backend: PaaS (AWS Elastic Beanstalk) vs IaaS (Amazon EC2).
* Sau khi được mentor tư vấn, chuyển hướng sang triển khai trực tiếp trên Amazon EC2 để tích lũy kinh nghiệm thực chiến sâu hơn.

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Tạm dừng việc code tính năng mới, bắt đầu tìm hiểu quy trình Build và Đóng gói một ứng dụng Spring Boot.<br>- Đọc tài liệu về Maven Lifecycle (Clean, Compile, Package). | 08/06/2026 | 08/06/2026 | Tài liệu Spring Boot Maven |
| 2 | - Thực hành chạy lệnh `mvn clean package` trên Terminal của VS Code / IntelliJ để đóng gói dự án Backend Pet Shop thành file `.jar`.<br>- Xử lý các lỗi lặt vặt liên quan đến Test Cases khi build file. | 09/06/2026 | 09/06/2026 | StackOverflow / Blog Java |
| 3 | - Tắt công cụ lập trình (IDE), mở Command Prompt của Windows và thử chạy file `.jar` vừa build bằng lệnh `java -jar petshop-backend.jar`.<br>- Kiểm tra lại các API trên Postman để chắc chắn file chạy độc lập tốt. | 10/06/2026 | 10/06/2026 | Java Documentation |
| 4 | - Tìm hiểu sơ bộ **AWS Elastic Beanstalk** (PaaS) — giải pháp tự động hóa giúp tải file `.jar` lên qua giao diện Web mà không cần gõ lệnh Linux.<br>- So sánh lợi ích/hạn chế giữa Beanstalk (dễ nhưng ít kiểm soát) và EC2 (khó hơn nhưng học được nhiều). | 11/06/2026 | 11/06/2026 | AWS Elastic Beanstalk Guide |
| 5 | - Sau khi tham vấn ý kiến mentor, nhóm quyết định triển khai trực tiếp trên **Amazon EC2** thay vì dùng Beanstalk. Lý do: Tự tay cấu hình máy chủ Linux, Security Group và Load Balancer mang lại giá trị học tập lớn hơn nhiều cho mục tiêu thực tập. | 12/06/2026 | 12/06/2026 | Tài liệu Amazon EC2 Linux |

### Kết quả đạt được tuần 8:

* **Hoàn thiện kỹ năng đóng gói ứng dụng Local (Application Packaging):**
  * Hiểu được sự khác biệt giữa việc chạy code trực tiếp trên công cụ lập trình (IDE) và chạy ứng dụng đã được biên dịch độc lập.
  * Sử dụng thành công Maven để đóng gói dự án Spring Boot thành một tệp thực thi `.jar` hoàn chỉnh.
  * Đảm bảo ứng dụng backend chạy ổn định trên môi trường Windows local thông qua lệnh `java -jar`, kết nối thành công với cơ sở dữ liệu.

* **Hình thành tư duy lựa chọn dịch vụ đám mây (Cloud Service Selection):**
  * Nắm được sự khác biệt giữa mô hình IaaS (Amazon EC2) và PaaS (AWS Elastic Beanstalk).
  * Đánh giá đúng: Beanstalk dễ dùng nhưng che giấu chi tiết hạ tầng; EC2 đòi hỏi nhiều công sức hơn nhưng tối đa hóa bài học thực chiến.

* **Xác định rõ lộ trình triển khai cho các tuần tiếp theo:**
  * Theo lời khuyên từ mentor, nhóm quyết định triển khai trực tiếp trên **Amazon EC2** cho dự án Pet Resort & Care. Dù con đường này đòi hỏi kỹ năng dòng lệnh Linux và cấu hình hạ tầng thủ công, đây là cơ hội học tập giá trị hơn nhiều, phù hợp với mục tiêu giáo dục của chương trình thực tập.