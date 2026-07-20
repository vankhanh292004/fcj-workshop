---
title: "Worklog Tuần 13"
weight: 13
chapter: false
pre: " <b> 1.13. </b> "
---

### Mục tiêu trọng tâm
- Phối hợp với nhóm tiến hành kiểm thử khả năng chịu tải (Load Test) của hệ thống.
- Phát hiện và vá các lỗi logic ứng dụng còn tồn đọng dưới môi trường tải cao.
- Hoàn thiện báo cáo thực tập, đóng gói tài liệu kỹ thuật và tham gia bảo vệ dự án cuối kỳ.

### Bảng nhật ký công việc

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
|------|----------|--------------|---------------|-------------------|
| 1 | Sử dụng các công cụ như Apache JMeter hoặc Locust để giả lập hàng trăm kết nối truy cập đồng thời vào hệ thống. | 10/07/2026 | 10/07/2026 | [Locust Docs](https://docs.locust.io/) |
| 2 | Giám sát các chỉ số phản hồi qua CloudWatch để theo dõi hiệu quả co giãn tự động của Auto Scaling Group. | 11/07/2026 | 11/07/2026 | |
| 3 | Khắc phục các điểm nghẽn cổ chai (bottlenecks) liên quan đến kết nối RDS MySQL bằng cách tinh chỉnh Connection Pool. | 13/07/2026 | 13/07/2026 | |
| 4 | Tổng hợp số liệu hiệu năng, rà soát lại các mục tiêu đề xuất ban đầu và viết báo cáo đánh giá dự án. | 14/07/2026 | 14/07/2026 | |
| 5 | Hoàn thiện trang web báo cáo cá nhân bằng Hugo, chạy build tĩnh (`hugo`) và đẩy lên GitHub Pages. | 15/07/2026 | 15/07/2026 | [GitHub Pages Deployment](https://gohugo.io/hosting-and-deployment/hosting-on-github/) |
| 6 | Tổng duyệt slide thuyết trình cùng nhóm và tham gia buổi bảo vệ báo cáo thực tập cuối kỳ. | 16/07/2026 | 20/07/2026 | |

### Kết quả đạt được
- Hệ thống chịu tải tốt với hơn 500 người dùng ảo đồng thời, tính năng Auto Scaling kích hoạt mượt mà theo đúng thiết kế.
- Hoàn tất khắc phục lỗi kết nối cơ sở dữ liệu và tối ưu hóa thời gian phản hồi API.
- Hoàn thành đầy đủ báo cáo thực tập cá nhân và tập thể, kết thúc kỳ thực tập thành công rực rỡ tại AWS Vietnam.
