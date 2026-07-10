---
title: "Worklog Tuần 3"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

Mục tiêu tuần 3:
- Tìm hiểu và thực hành chuyên sâu về dịch vụ quản lý chi phí AWS Budgets để thiết lập các cơ chế giám sát tài khoản.
- Kích hoạt cảnh báo ngân sách tự động để kiểm soát chi phí thực tập.
- Khởi tạo môi trường lưu trữ hình ảnh thử nghiệm phục vụ cho các tài nguyên (ảnh thú cưng, hóa đơn dịch vụ) của dự án Pet Resort thông qua Amazon S3.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu tổng quan về AWS Budgets và tìm hiểu 4 loại ngân sách chính: Cost Budget, Usage Budget, RI Budget, và Savings Plans Budget. | 01/05/2026 | 01/05/2026 | AWS Study Group |
| 2 | Thực hành tạo Cost Budget thông qua AWS Management Console (dịch vụ Billing) để nhận cảnh báo khi tổng chi phí vượt ngưỡng. | 02/05/2026 | 02/05/2026 | AWS Management Console |
| 3 | Thực hành tạo Usage Budget để kiểm soát mức sử dụng theo từng dịch vụ, ví dụ thiết lập cảnh báo cho ngưỡng giờ sử dụng tài nguyên mỗi tháng. | 03/05/2026 | 03/05/2026 | AWS Management Console |
| 4 | Cấu hình và kích hoạt hệ thống cảnh báo ngân sách tự động (AWS Budgets / Billing Alarms) để kiểm soát dung lượng Credit thực tập. | 04/05/2026 | 04/05/2026 | Tài liệu AWS Billing |
| 5 | Nghiên cứu tài liệu về Reservation Instance (RI) Budget, Savings Plans Budget và xem xét các hướng dẫn minh họa. | 05/05/2026 | 05/05/2026 | AWS Study Group |
| 6 | Thực hành tạo S3 Bucket đầu tiên trên AWS Console với tên định danh độc nhất phục vụ lưu trữ tài nguyên: `petshop-media-storage`. | 06/05/2026 | 06/05/2026 | Giao diện điều khiển AWS |
| 7 | Đánh giá lại toàn bộ các bài lab cấu hình ngân sách và tổng hợp báo cáo worklog tuần. | 07/05/2026 | 07/05/2026 | AWS Study Group |

Thành tích tuần 3:

• Nắm vững tư duy quản lý chi phí, hiểu rõ sự khác biệt giữa Cost Budget và Usage Budget để kiểm soát tài nguyên trên đám mây.

• Hoàn thành việc giả lập cấu hình ngân sách với các tham số thực tế và kích hoạt thành công công cụ kiểm soát tự động để ngăn chặn rủi ro phát sinh chi phí ngoài ý muốn (vượt Credit thực tập).

• Khởi tạo thành công không gian lưu trữ biệt lập `petshop-media-storage` trên Amazon S3, bước đầu xây dựng hạ tầng lưu trữ tài nguyên tĩnh cho dự án Pet Resort.