---
title: "Worklog Tuần 2"
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu trọng tâm
- Xây dựng hệ thống quản lý định danh và quyền truy cập (AWS IAM).
- Tạo các tài khoản người dùng (User) cho từng thành viên trong nhóm dự án.
- Thiết lập và cấp phát các chính sách phân quyền (Policy & Group) theo nguyên tắc đặc quyền tối thiểu (Least Privilege).

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Nghiên cứu tài liệu AWS IAM, khái niệm User, Group, Policy và Role. | 24/04/2026 | 24/04/2026 | [AWS IAM Docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) |
| 2 | Kích hoạt Multi-Factor Authentication (MFA) cho tài khoản Root để bảo vệ hạ tầng cấp cao nhất. | 25/04/2026 | 25/04/2026 | |
| 3 | Tạo các nhóm IAM đại diện cho các vai trò (Developer, Admin, DevOps) trong nhóm dự án. | 27/04/2026 | 27/04/2026 | |
| 4 | Soạn thảo các chính sách JSON IAM tùy chỉnh để cấp quyền truy cập hạn chế cho các dịch vụ S3, EC2 và RDS. | 28/04/2026 | 28/04/2026 | |
| 5 | Khởi tạo tài khoản IAM User riêng biệt cho từng thành viên và gán vào nhóm tương ứng. | 29/04/2026 | 29/04/2026 | |
| 6 | Tiến hành kiểm thử đăng nhập, xác thực MFA cho các thành viên và bàn giao thông tin tài khoản an toàn. | 30/04/2026 | 30/04/2026 | |

### Kết quả đạt được
- Bảo mật tài khoản Root bằng lớp bảo vệ MFA.
- Toàn bộ thành viên có tài khoản IAM User riêng biệt, chấm dứt việc dùng chung tài khoản hoặc dùng Root.
- Thiết lập thành công các nhóm phân quyền (Groups) và chính sách (Policies) chặt chẽ, tuân thủ tiêu chuẩn bảo mật AWS.