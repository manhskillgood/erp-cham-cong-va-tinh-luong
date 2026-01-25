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

---

## 1. Giới thiệu hệ thống
Hệ thống **ERP: Chấm công & Tính lương** là nền tảng quản lý nhân sự dành cho doanh nghiệp, hỗ trợ tự động hóa các nghiệp vụ:
- Quản lý **nhân viên**, đơn vị công tác, chức vụ, bằng cấp.
- **Chấm công thông minh** theo ca làm, đơn xin phép.
- Tự động tổng hợp **bảng chấm công** theo ngày/tháng.
- **Tính lương tự động** dựa trên công thực tế, lương cơ bản, phụ cấp và khấu trừ.
- Cung cấp **Dashboard AI** hỗ trợ phân tích chấm công và tính lương.
- Quản lý lịch sử lương, truy vết dữ liệu minh bạch.

Hệ thống được xây dựng theo mô hình **ERP Client–Server**, đảm bảo khả năng mở rộng, tích hợp và phù hợp với doanh nghiệp vừa và nhỏ.

---

## 2. Kiến trúc hệ thống
### Mô hình tổng thể
- **ERP Client**: Giao diện người dùng cho nhân viên, HR và quản trị viên.
- **ERP Server**: Xử lý nghiệp vụ, dữ liệu, AI và tích hợp hệ thống.
- **Cơ sở dữ liệu**: Lưu trữ tập trung thông tin nhân sự, chấm công, lương.

### Phân hệ chính
- **HR Module**
  - Thêm/sửa/xóa nhân viên
  - Quản lý đơn vị công tác, chức vụ, bằng cấp
- **Attendance Module**
  - Chấm công theo ca
  - Đăng ký ca làm
  - Đơn xin phép
  - Dashboard AI chấm công
- **Payroll Module**
  - Cấu hình lương cơ bản
  - Tính lương tự động
  - Dashboard AI tính lương
  - Bảng lương & lịch sử lương

Hệ thống sử dụng **API / RPC** để kết nối Client – Server và **ORM** để thao tác dữ liệu với cơ sở dữ liệu.

---

## 3. Ngôn ngữ & Công nghệ sử dụng
[![Java](https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=java&logoColor=white)](https://www.java.com/)
[![Java Swing](https://img.shields.io/badge/Java%20Swing-007396?style=for-the-badge&logo=java&logoColor=white)](https://docs.oracle.com/javase/tutorial/uiswing/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![REST API](https://img.shields.io/badge/REST%20API-005571?style=for-the-badge)](https://restfulapi.net/)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-FF6F00?style=for-the-badge)](#)

---

## 4. Một số màn hình giao diện
<p align="center">
   <img src="images/login.png" alt="Đăng nhập hệ thống" width="500"/>
</p>
<p align="center">
   <em>Hình 1: Giao diện đăng nhập hệ thống ERP</em>
</p>

<p align="center">
   <img src="images/attendance_dashboard.p_
