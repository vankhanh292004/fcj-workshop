---
title: "Worklog Tuần 5"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

Mục tiêu tuần 5:
- Hoàn thiện kiến thức về hạ tầng mạng đám mây với các khái niệm về Mạng con (Subnets) và NAT Gateway để thiết lập môi trường bảo mật.
- Tiếp cận và tìm hiểu tổng quan nhóm dịch vụ tính toán (Compute Services) trên nền tảng AWS.
- Nghiên cứu lý thuyết cơ bản về máy chủ ảo (Amazon EC2), kiến trúc phi máy chủ (AWS Lambda) và cách triển khai chúng trong không gian mạng ảo.
- Đánh giá sơ bộ đặc điểm của từng dịch vụ để định hướng giải pháp triển khai phần xử lý backend sau này.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu chuyên sâu về Mạng con (Subnets) trong VPC: Phân loại Public, Private, VPN-only subnet và quy tắc cấp phát dải IP (CIDR, 5 IP dự phòng của AWS). | 18/05/2026 | 18/05/2026 | Tài liệu AWS VPC |
| 2 | Tìm hiểu khái niệm và cách cấu hình NAT Gateway kết hợp với Elastic IP (IP tĩnh) để cung cấp quyền truy cập Internet an toàn cho các tài nguyên (như máy chủ ảo) nằm trong Private subnet. | 19/05/2026 | 19/05/2026 | Tài liệu AWS NAT Gateway |
| 3 | Đọc tài liệu tổng quan về Amazon EC2: Tìm hiểu về vòng đời của một Instance (EC2 Lifecycle), các trạng thái hoạt động và cơ chế bảo mật khóa Key Pair. | 20/05/2026 | 20/05/2026 | Tài liệu Amazon EC2 |
| 4 | Tìm hiểu khái niệm cơ bản về Serverless (kiến trúc phi máy chủ) và cách thức hoạt động dựa trên sự kiện của dịch vụ AWS Lambda. | 21/05/2026 | 21/05/2026 | Tài liệu AWS Lambda |
| 5 | Thực hiện bài toán phân tích so sánh lý thuyết giữa EC2 và Lambda về mặt quản lý hạ tầng, cơ chế tự động co giãn (Scaling) và cách tính chi phí. | 22/05/2026 | 22/05/2026 | AWS Compute Blog |
| 6 | Thảo luận tổng quan với nhóm về mô hình kiến trúc web: Đánh giá xem ứng dụng Spring Boot (như dự án Pet Resort) sẽ phù hợp với EC2 (chạy trong Private Subnet qua NAT Gateway) hay Serverless Lambda hơn. | 23/05/2026 | 23/05/2026 | |
| 7 | Hệ thống hóa lại toàn bộ kiến thức lý thuyết đã tìm hiểu trong tuần và cập nhật tiến độ báo cáo vào hệ thống Hugo local. | 24/05/2026 | 24/05/2026 | |

Thành tích tuần 5:

• Nắm vững kiến trúc mạng nội bộ VPC, hiểu rõ cách phân chia các phân đoạn mạng (Subnet) và vai trò thiết yếu của NAT Gateway trong việc giúp máy chủ ảo truy cập Internet mà không bị lộ diện ra ngoài.

• Hiểu rõ các khái niệm nền tảng về hạ tầng tính toán trên mây, phân biệt được sự khác nhau giữa mô hình cấp phát máy chủ ảo truyền thống (EC2) và chạy hàm Serverless (Lambda).

• Xác định được các kịch bản sử dụng (Use Cases) phù hợp cho từng dịch vụ để áp dụng vào việc thiết kế kiến trúc Backend an toàn và tối ưu chi phí cho dự án thực tế.

• Tích lũy thêm tư duy phân tích hệ thống tổng quan, chuẩn bị tốt cho giai đoạn đóng gói bản Proposal kiến trúc chính thức.