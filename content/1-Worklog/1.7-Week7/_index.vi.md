---
title: "Worklog Tuần 7"
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
* Tích hợp giao diện Frontend ReactJS với các RESTful API của Spring Boot Backend.
* Triển khai hoàn chỉnh luồng xác thực người dùng và phân quyền hệ thống bằng mã báo hiệu JWT.
* Kiểm thử tích hợp (Integration Testing) các tính năng cốt lõi của hệ thống Pet Shop (Giỏ hàng, Đặt lịch Spa, Tạo đơn hàng).

### Nhiệm vụ thực hiện trong tuần:
| Ngày | Nhiệm vụ chi tiết | Ngày bắt đầu | Ngày kết thúc | Tài liệu tham khảo |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Kết nối các trang hiển thị của React Frontend với API của Spring Boot thông qua lớp trung gian `services/api.js`.<br>- Cấu hình Axios base URL trỏ chính xác về địa chỉ IP/Endpoint của máy chủ Backend. | 01/06/2026 | 01/06/2026 | Tài liệu Axios & Spring Boot API |
| 2 | - Xây dựng luồng Đăng nhập/Đăng ký hoàn chỉnh tại giao diện `LoginPage` và `RegisterPage`.<br>- Tích hợp cơ chế xử lý chuỗi mã báo hiệu xác thực JWT (`JwtResponse`, `JwtTokenProvider`) từ `AuthController` phía Backend vào kho lưu trữ `authStore.js` của Frontend để quản lý phiên làm việc và bảo vệ các tuyến đường kiểm soát (`ProtectedRoute`, `AdminRoute`). | 02/06/2026 | 02/06/2026 | Spring Security & React Context |
| 3 | - Kết nối trang danh mục hàng hóa (`ProductsPage`, `ProductCard`) với dữ liệu động từ `ProductController`.<br>- Triển khai logic xử lý cho trang giỏ hàng `CartPage` thông qua `cartStore.js`, kết nối đồng bộ trạng thái đến `CartController` phía Backend. | 03/06/2026 | 03/06/2026 | React State Management |
| 4 | - Xây dựng luồng xử lý đơn đặt hàng (`CheckoutPage`) và luồng đặt lịch hẹn chăm sóc thú cưng (`BookingPage`).<br>- Thiết lập cổng kết nối dữ liệu từ giao diện xuống các bộ điều khiển chức năng hệ thống backend bao gồm `OrderController` và `BookingController`. | 04/06/2026 | 04/06/2026 | Spring Boot Controller Mapping |
| 5 | - Thực hiện kiểm thử toàn diện (End-to-End Testing) luồng trải nghiệm khách hàng: Đăng ký -> Đăng nhập -> Thêm giỏ hàng -> Đặt lịch dịch vụ cắt tỉa (`SpaServiceController`) -> Thanh toán hóa đơn.<br>- Tối ưu hóa tệp `CorsConfig` ở phía Spring Boot để xử lý triệt để các lỗi chặn chia sẻ tài nguyên chéo nguồn (CORS) giữa hai môi trường. | 05/06/2026 | 05/05/2026 | Integration Testing Guide |

### Kết quả đạt được tuần 7:

* **Tích hợp thành công kiến trúc đa tầng (Frontend - Backend Integration):**
  * Thiết lập kết nối thông suốt giữa ứng dụng giao diện ReactJS và các dịch vụ RESTful API của Spring Boot thông qua lớp xử lý tập trung `services/api.js`.
  * Cấu hình xử lý và bắt lỗi hệ thống đồng bộ để hiển thị thông báo phản hồi (Feedback) chuẩn xác cho người dùng khi có lỗi gọi API thất bại.

* **Hoàn thành phân hệ xác thực và bảo mật hệ thống (Authentication & Authorization):**
  * Khách hàng có thể đăng ký tài khoản mới, hệ thống tự động mã hóa mật khẩu mật định và lưu trữ an toàn vào cơ sở dữ liệu.
  * Cơ chế Đăng nhập/Đăng xuất hoạt động ổn định, mã báo hiệu JWT được lưu trữ và đính kèm tự động vào Header của mỗi request nhờ cấu hình bộ lọc `JwtAuthenticationFilter` phía backend.
  * Phân quyền truy cập các phân hệ quản trị nghiêm ngặt: Các trang kiểm soát dữ liệu của Admin (`AdminBookingsPage`, `AdminProductsPage`, `DashboardPage`) được bảo vệ tuyệt đối bằng `AdminRoute` ở frontend, ngăn chặn hoàn toàn việc người dùng phổ thông truy cập trái phép.

* **Hiện thực hóa các tính năng nghiệp vụ cốt lõi của ứng dụng Pet Shop:**
  * **Hiển thị sản phẩm/dịch vụ:** Dữ liệu hàng hóa và dịch vụ spa được tải động từ `ProductController` và `SpaServiceController`.
  * **Giỏ hàng (`cartStore.js`):** Thêm, xóa, cập nhật số lượng vật phẩm và tự động tính toán tổng giá trị đơn hàng.
  * **Đơn hàng & Đặt lịch:** Hoàn thiện luồng lưu trữ thông tin giao dịch vào bảng đơn hàng (`OrderController`) và lịch đặt chỗ chăm sóc thú cưng (`BookingController`).

* **Hoàn thành kiểm thử luồng vận hành (End-to-End User Journey Verified):**
  * Kiểm thử thành công kịch bản: Khách hàng mới đăng ký -> Đăng nhập vào hệ thống -> Duyệt danh sách dịch vụ Spa -> Thêm sản phẩm thức ăn hạt vào giỏ -> Thực hiện đặt lịch hẹn và tạo hóa đơn thành công.

* **Cải thiện trải nghiệm và tối ưu hóa hệ thống:**
  * Sửa lỗi xung đột tài nguyên chéo nguồn bằng cách tinh chỉnh chính xác các cấu hình định tuyến trong tệp `CorsConfig` của Spring Boot.
  * Thêm trạng thái tải dữ liệu (Loading states) trên giao diện để tối ưu hóa trải nghiệm tương tác trực quan cho người dùng.