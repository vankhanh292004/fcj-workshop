---
title: "Worklog Tuần 5"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

Mục tiêu tuần 5:
- Tiếp cận và tìm hiểu tổng quan nhóm dịch vụ tính toán (Compute Services) trên nền tảng AWS.
- Nghiên cứu lý thuyết cơ bản về máy chủ ảo (Amazon EC2) và kiến trúc phi máy chủ (AWS Lambda).
- Đánh giá sơ bộ đặc điểm của từng dịch vụ để định hướng giải pháp triển khai phần xử lý backend sau này.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Đọc tài liệu tổng quan về Amazon EC2: Tìm hiểu về vòng đời của một Instance (EC2 Lifecycle), các trạng thái hoạt động và cơ chế bảo mật khóa Key Pair. | 18/05/2026 | 18/05/2026 | Tài liệu Amazon EC2 |
| 2 | Tìm hiểu khái niệm cơ bản về Serverless (kiến trúc phi máy chủ) và cách thức hoạt động dựa trên sự kiện của dịch vụ AWS Lambda. | 19/05/2026 | 19/05/2026 | Tài liệu AWS Lambda |
| 3 | Thực hiện bài toán phân tích so sánh lý thuyết giữa EC2 và Lambda về mặt quản lý hạ tầng, cơ chế tự động co giãn (Scaling) và cách tính chi phí. | 20/05/2026 | 20/05/2026 | AWS Compute Blog |
| 4 | Thảo luận tổng quan với nhóm về mô hình kiến trúc web: Đánh giá xem một ứng dụng Spring Boot (như dự án Pet Resort) sẽ phù hợp với EC2 truyền thống hay Serverless Lambda hơn. | 21/05/2026 | 21/05/2026 | |
| 5 | Hệ thống hóa lại toàn bộ kiến thức lý thuyết đã tìm hiểu trong tuần và cập nhật tiến độ báo cáo vào hệ thống Hugo local. | 22/05/2026 | 22/05/2026 | |

Thành tích tuần 5:

• Nắm vững các khái niệm nền tảng về hạ tầng tính toán trên mây, phân biệt được sự khác nhau giữa mô hình cấp phát máy chủ ảo (EC2) và chạy hàm Serverless (Lambda).

• Hiểu rõ các kịch bản sử dụng (Use Cases) phù hợp cho từng dịch vụ để áp dụng vào các bài toán thực tế sau này.

• Tích lũy thêm tư duy phân tích hệ thống tổng quan, chuẩn bị tốt cho giai đoạn đóng gói bản Proposal kiến trúc chính thức.