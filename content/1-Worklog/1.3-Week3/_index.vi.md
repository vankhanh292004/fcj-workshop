---
title: "Worklog Tuần 3"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

Mục tiêu tuần 3:
- Tìm hiểu cơ chế quản lý lưu trữ đối tượng và tài nguyên tĩnh trên đám mây.
- Khởi tạo môi trường lưu trữ hình ảnh thử nghiệm phục vụ cho các tài nguyên (ảnh thú cưng, hóa đơn dịch vụ) của dự án Pet Resort.
- Thiết lập các cơ chế giám sát tài khoản và cảnh báo chi phí ban đầu.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Cấu hình và kích hoạt hệ thống cảnh báo ngân sách tự động (AWS Budgets / Billing Alarms) để kiểm soát dung lượng Credit thực tập. | 04/05/2026 | 04/05/2026 | Tài liệu AWS Billing |
| 2 | Nghiên cứu lý thuyết nền tảng về dịch vụ Amazon S3 (Simple Storage Service), các khái niệm về Bucket, Object và Storage Classes. | 05/05/2026 | 05/05/2026 | Tài liệu Amazon S3 |
| 3 | Thực hành tạo S3 Bucket đầu tiên trên AWS Console với tên định danh độc nhất phục vụ lưu trữ tài nguyên: `petshop-media-storage`. | 06/05/2026 | 06/05/2026 | Giao diện điều khiển AWS |
| 4 | Thao tác tải lên (Upload) dữ liệu hình ảnh mẫu thông qua giao diện S3 Console; tìm hiểu cấu hình Object Ownership và quyền truy cập cơ bản. | 07/05/2026 | 07/05/2026 | Tài liệu Quản lý đối tượng S3 |
| 5 | Tìm hiểu nguyên tắc bảo mật IAM nâng cao; thực hành tạo IAM User riêng biệt có phân quyền giới hạn thay vì thao tác trực tiếp bằng Root Account. | 08/05/2026 | 08/05/2026 | AWS IAM Best Practices |

Thành tích tuần 3:

• Kích hoạt thành công công cụ kiểm soát ngân sách tự động để ngăn chặn rủi ro phát sinh chi phí ngoài ý muốn trên tài khoản đám mây.

• Khởi tạo thành công không gian lưu trữ biệt lập `petshop-media-storage` trên Amazon S3, làm quen với luồng upload và quản lý file tĩnh.

• Nắm vững các bước phân quyền cơ bản và thiết lập chính sách bảo mật IAM an toàn theo tiêu chuẩn khuyến nghị của AWS.