---
title: "Worklog Tuần 2"
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

Mục tiêu tuần 2:
- Tìm hiểu tổng quan về nền tảng AWS, triết lý vận hành và kiến trúc hạ tầng toàn cầu (Global Infrastructure).
- Nắm vững quy trình khởi tạo tài khoản AWS an toàn và các phương pháp xác thực bảo mật đa yếu tố.
- Cấu hình phân quyền quản trị cơ bản và nghiên cứu các phương pháp quản lý, tối ưu hóa chi phí đám mây.

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Tìm hiểu sự khác biệt của AWS (tầm nhìn, văn hóa, triết lý giá) và cấu trúc hạ tầng cơ sở toàn cầu (Data Center, Availability Zone). | 24/04/2026 | 24/04/2026 | [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure) |
| 2 | Khởi tạo tài khoản AWS đầu tiên. Nghiên cứu khái niệm về root user và hiểu rõ việc root user có toàn quyền với tài khoản, không thể bị giới hạn. | 25/04/2026 | 25/04/2026 | Tài liệu thực hành AWS |
| 3 | Thực hành gia tăng bảo mật bằng cách thiết lập MFA (Multi-factor Authentication) cho tài khoản. Cài đặt thiết bị MFA ảo trên smartphone sử dụng Microsoft Authenticator, Google Authenticator, hoặc Okta Verify. Tìm hiểu thêm về khóa bảo mật U2F cứng. | 26/04/2026 | 26/04/2026 | Tài liệu thực hành AWS |
| 4 | Xây dựng cơ chế phân quyền an toàn: Tạo Admin Group và Admin User để quản lý quyền truy cập vào các tài nguyên thay vì sử dụng trực tiếp user root. | 27/04/2026 | 27/04/2026 | Tài liệu thực hành AWS |
| 5 | Làm quen với Management Console và cấu hình AWS Command Line Interface (CLI) để tương tác với các dịch vụ bằng dòng lệnh. | 28/04/2026 | 28/04/2026 | <https://aws.amazon.com/console/> |
| 6 | Thực hành tạo các loại cảnh báo ngân sách với AWS Budgets (Cost, Usage, Reservation, Saving plans budget) và tổng hợp báo cáo worklog. | 30/04/2026 | 30/04/2026 | Tài liệu thực hành AWS |

Thành tích tuần 2:

• Nắm được triết lý vận hành của AWS và kiến trúc cách ly lỗi (fault isolation) thông qua các Availability Zone (AZ).

• Hoàn tất việc tạo tài khoản AWS đầu tiên và nắm rõ tính chất quyền hạn tối đa của root user. 

• Cấu hình thành công lớp bảo mật MFA bằng ứng dụng trên smartphone và hiểu được cơ chế hoạt động của khóa bảo mật U2F.

• Thiết lập thành công Admin Group và Admin User để phân quyền an toàn, áp dụng nguyên tắc đặc quyền tối thiểu trong quản trị hệ thống.

• Nắm bắt được các phương pháp tiết kiệm chi phí đám mây và biết cách thiết lập các loại ngân sách bảo vệ tài khoản bằng công cụ AWS Budgets.