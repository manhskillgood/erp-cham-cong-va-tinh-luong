
<h1 align="center">
THỰC TẬP CNTT7: THỰC TẬP DOANH NGHIỆP - QUẢN LÝ CHẤM CÔNG VÀ TÍNH LƯƠNG
</h1>
<div align="center">
  <img src="README/logoDaiNam.png" alt="DaiNam University Logo" width="250">
  <img src="README/fitdnu_logo.png" alt="KHOA CÔNG NGHỆ THỐNG TIN" width="250">
  <img src="README/aiotlab_logo.png" alt="AIOT Lab DNU Logo" width="250">
</div>
<br>
<div align="center">

[![FIT DNU](https://img.shields.io/badge/-FIT%20DNU-28a745?style=for-the-badge)](https://fitdnu.net/)
[![DAINAM UNIVERSITY](https://img.shields.io/badge/-DAINAM%20UNIVERSITY-dc3545?style=for-the-badge)](https://dainam.edu.vn/vi)

</div>

<div align="center">

[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-%23181717.svg?style=for-the-badge&logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

</div>

<hr>

<div align="center">

# 🏢 Giới thiệu hệ thống

</div>

### 📖 Hệ thống được xây dựng trên nền tảng **Odoo ERP** nhằm tối ưu hóa toàn diện quy trình quản trị nhân sự, chấm công và tự động hóa bảng lương cho tổ chức. Giải pháp kết hợp sức mạnh của phân tích dữ liệu và **Trí tuệ nhân tạo (AI)** để giải quyết bài toán minh bạch trong kỷ luật lao động và chính xác trong hạch toán chi phí.

### 🌟 Các tính năng cốt lõi:
* **Quản trị Chấm công Đa chiều:** Tự động ghi nhận ngày công, phân tích chi tiết số phút đi muộn/về sớm và quản lý trạng thái vắng mặt theo thời gian thực.
* **Phê duyệt Đơn từ Thông minh (AI Insight):** Sử dụng AI để thẩm định tính trung thực của các đơn xin nghỉ dựa trên việc đối chiếu lịch sử vi phạm và quy luật hành vi của nhân sự.
* **Dashboard Phân tích Hành vi:** Trực quan hóa các "lý do quốc dân" phổ biến và soi quy luật vi phạm theo thứ trong tuần để hỗ trợ quản lý ra quyết định chiến lược.
* **Tự động hóa Tính lương:** Kết xuất bảng lương chuẩn xác từ dữ liệu chấm công thực tế, giúp loại bỏ sai sót thủ công và đảm bảo quyền lợi cho người lao động.
* **Hệ thống Thông báo & Tương tác:** Tích hợp gửi thông báo kết quả phê duyệt và phiếu lương tự động qua Email, tối ưu hóa trải nghiệm nhân viên trong tổ chức.


<hr>

# 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 1.1. Clone project.
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
git checkout 

## 1.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 1.3. khởi tạo môi trường ảo.

`python3.10 -m venv ./venv`
Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu

```
source venv/bin/activate
pip3 install -r requirements.txt
```

# 2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.

`docker-compose up -d`

# 3. Setup tham số chạy cho hệ thống

## 3.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5432
xmlrpc_port = 8069
```
Có thể kế thừa từ **odoo.conf.template**

Ngoài ra có thể thêm mổ số parameters như:

```
-c _<đường dẫn đến tệp odoo.conf>_
-u _<tên addons>_ giúp cập nhật addons đó trước khi khởi chạy
-d _<tên database>_ giúp chỉ rõ tên database được sử dụng
--dev=all giúp bật chế độ nhà phát triển 
```

# 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

# 5. Khởi chạy Dashboard AI (Streamlit)
```
streamlit run dashboard_app.py chạy lệnh để khởi động Dashboard
```
<hr>

# 🚀 2. GIAO DIỆN CÁC CHỨC NĂNG
### Giao diện nhân sự
<img width="1902" height="931" alt="image" src="README/image.png" />

### Giao diện chấm công
<img width="1885" height="935" alt="image" src="README/img1.jpg" />

### Giao diện tính lương
<img width="1885" height="935" alt="image" src="README/img2.jpg" />

### Giao diện Dashboard AI
<img width="1885" height="935" alt="image" src="README/img3.jpg" />

<hr>

<h2 align="center">🤝</h2>
<p>Dự án được phát triển bởi:</p>
<center>
<table>
  <thead>
    <tr>
      <th>Giảng viên hướng dẫn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Thầy Lê Tuấn Anh</td>
    </tr>
  </tbody>
</table>
</center>

<center>
<p>Sinh viên thực hiện:</p>
<table>
  <thead>
    <tr>
      <th>Họ và Tên</th>
      <th>Mã sinh viên</th>
      <th>Vai trò</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ngô Tuấn Minh</td>
      <td>1571020175</td>
      <td>Phát triển dự án</td>
    </tr>
    <tr>
      <td>Triệu Vũ Hà My</td>
      <td>1571020181</td>
      <td>Phát triển dự án</td>
    </tr>
    <tr>
      <td>Nguyễn Trung Kiên</td>
      <td>1671020172</td>
      <td>Phát triển dự án</td>
    </tr>
  </tbody>
</table>
</center>

<p align="center">© 2026 NGÔ TUẤN MINH, CNTT16-06, TRƯỜNG ĐẠI HỌC ĐẠI NAM</p>

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
   <img src="ảnh/thêm nhân viên.jpg" alt="Thêm nhân viên" width="500"/>
</p>
<p align="center">
   <em>Hình 2: Giao diện thêm nhân viên</em>
</p>

<p align="center">
   <img src="ảnh/db chấm công.jpg" alt="Dashboard chấm công" width="500"/>
</p>
<p align="center">
   <em>Hình 3: Dashboard AI chấm công</em>
</p>

<p align="center">
   <img src="ảnh/db lương.jpg" alt="Dashboard tính lương" width="500"/>
</p>
<p align="center">
   <em>Hình 4: Dashboard AI tính lương</em>
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

