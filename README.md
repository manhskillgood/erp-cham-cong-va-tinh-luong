<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>

<h2 align="center">
     HỆ THỐNG ERP: CHẤM CÔNG & TÍNH LƯƠNG
</h2>

<div align="center">
    <p align="center">
        <img alt="AIoTLab Logo" width="170" src="https://github.com/user-attachments/assets/711a2cd8-7eb4-4dae-9d90-12c0a0a208a2" />
        <img alt="AIoTLab Logo" width="180" src="https://github.com/user-attachments/assets/dc2ef2b8-9a70-4cfa-9b4b-f6c2f25f1660" />
        <img alt="DaiNam University Logo" width="200" src="https://github.com/user-attachments/assets/77fe0fd1-2e55-4032-be3c-b1a705a1b574" />
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)
</div>


## 1. Giới thiệu hệ thống
Hệ thống **ERP: Chấm công & Tính lương** là một giải pháp quản lý nhân sự toàn diện, hỗ trợ doanh nghiệp tự động hóa các nghiệp vụ liên quan đến nhân sự, thời gian làm việc và tiền lương.

Hệ thống cung cấp các chức năng chính:
- Quản lý **nhân viên**, đơn vị công tác, chức vụ, bằng cấp.
- **Chấm công theo ca làm**, hỗ trợ đăng ký ca và đơn xin phép.
- Tự động tổng hợp **bảng chấm công** theo ngày, tháng.
- **Tính lương tự động** dựa trên công thực tế, lương cơ bản, phụ cấp và khấu trừ.
- Dashboard **AI hỗ trợ phân tích** chấm công và lương.
- Lưu trữ và truy vết **lịch sử lương, lịch sử chấm công** minh bạch.

Hệ thống được xây dựng dựa trên nền tảng **Odoo ERP**, đảm bảo tính mở rộng, linh hoạt và phù hợp với doanh nghiệp vừa và nhỏ.


## 2. Kiến trúc hệ thống
### 2.1 Mô hình tổng thể
Hệ thống được thiết kế theo mô hình **ERP Client – Server**, gồm các thành phần:
- **ERP Client**: Giao diện người dùng cho Nhân viên, HR và Quản trị viên.
- **ERP Server**: Xử lý nghiệp vụ, dữ liệu, workflow và AI.
- **Cơ sở dữ liệu**: Lưu trữ tập trung toàn bộ dữ liệu hệ thống.

Client và Server giao tiếp thông qua **API / RPC**.

### 2.2 Các phân hệ chính
- **HR Module**
  - Quản lý nhân viên
  - Quản lý đơn vị công tác
  - Quản lý chức vụ
  - Quản lý bằng cấp

- **Attendance Module**
  - Chấm công theo ca làm
  - Đăng ký ca làm
  - Quản lý đơn xin phép
  - Dashboard AI chấm công
  - Bảng chấm công

- **Payroll Module**
  - Cấu hình lương cơ bản
  - Tính lương tự động
  - Dashboard AI tính lương
  - Bảng lương và lịch sử lương


## 3. Công nghệ sử dụng

### 🖥️ Hệ điều hành
<p align="center">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"/>
</p>


### ⚙️ Công nghệ chính
<p align="center">
  <img src="https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/XML-FF6600?style=for-the-badge"/>
</p>


### 🗄️ Cơ sở dữ liệu
<p align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
</p>


## 4. Một số màn hình giao diện
<p align="center">
   <img src="ảnh/nhân sự.jpg" alt="Quản lý nhân sự" width="500"/>
</p>
<p align="center">
   <em>Hình 1: Giao diện quản lý nhân sự</em>
</p>

<p align="center">
   <img src="ảnh/db chấm công.jpg" alt="Thêm nhân viên" width="500"/>
</p>
<p align="center">
   <em>Hình 2: Giao diện thêm nhân viên</em>
</p>

<p align="center">
   <img src="ảnh/db chấm công.jpg" alt="Dashboard chấm công" width="500"/>
</p>
<p align="center">
   <em>Hình 2: Dashboard AI chấm công</em>
</p>

<p align="center">
   <img src="ảnh/db lương.jpg" alt="Dashboard tính lương" width="500"/>
</p>
<p align="center">
   <em>Hình 3: Dashboard AI tính lương</em>
</p>


## 5. Cài đặt & Triển khai
### Yêu cầu môi trường
- Ubuntu 20.04+  
- Python 3.8+  
- PostgreSQL  
- Odoo Community  

### Các bước triển khai
1. Cài đặt Odoo và các dependency cần thiết.
2. Khởi tạo cơ sở dữ liệu PostgreSQL.
3. Cấu hình Odoo Server (`odoo.conf`).
4. Cài đặt module **HR – Attendance – Payroll**.
5. Khởi động hệ thống và truy cập giao diện web.


## 6. Thành viên & Thông tin
- **Sinh viên thực hiện**: Lê Đức Mạnh  
- **Lớp**: CNTT 16-01  
- **Email**: leducmanh19102004@gmail.com  

© 2025 AIoTLab – Faculty of Information Technology, DaiNam University
