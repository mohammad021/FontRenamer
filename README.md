# FontRenamer
`fontrenamer.py` is a Python script designed to rename font files (e.g., .ttf, .woff, .woff2, .otf) based on the font name and style.


### **فارسی**

## فهرست مطالب

1. [معرفی پروژه](#font-renamer-اسکریپت-پایتون-برای-تغییر-نام-فایلهای-فونت)
2. [ویژگی‌ها](#ویژگیها)
3. [پیش‌نیازها](#پیشنیازها)
4. [نصب و راه‌اندازی](#نصب-و-راهاندازی)
5. [نحوه استفاده](#نحوه-استفاده)
    - [تغییر نام فایل‌های فونت](#نحوه-استفاده)
6. [جزئیات اسکریپت](#جزئیات-اسکریپت)
7. [لایسنس](#لایسنس)

### **English**

## Table of Contents

1. [Project Introduction](#font-renamer-a-python-script-for-renaming-font-files)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
    - [Renaming Font Files](#usage)
6. [Script Details](#script-details)
7. [License](#license)

---


### **Font Renamer: اسکریپت پایتون برای تغییر نام فایل‌های فونت**

`fontrenamer.py` یک اسکریپت پایتون است که برای تغییر نام فایل‌های فونت (مانند .ttf, .woff, .woff2, .otf) بر اساس نام و سبک فونت طراحی شده است. این اسکریپت به توسعه‌دهندگان وب و طراحان کمک می‌کند تا فونت‌های خود را به صورت سازماندهی شده و قابل شناسایی نگه دارند.

#### ویژگی‌ها
- **نصب خودکار کتابخانه‌های مورد نیاز:** اسکریپت کتابخانه‌های پایتون مورد نیاز (`fonttools` و `brotli`) را اگر نصب نشده باشند، به صورت خودکار نصب می‌کند.
- **استخراج اطلاعات فونت:** نام و سبک فونت را از فایل فونت استخراج می‌کند.
- **تغییر نام فایل‌های فونت:** فایل‌های فونت را براساس نام و سبک فونت به فرمت جدید تغییر نام می‌دهد.

#### پیش‌نیازها
1. **پایتون نسخه 3.6 یا بالاتر**
   - می‌توانید پایتون را از [Python.org](https://www.python.org) دانلود و نصب کنید.

#### نصب و راه‌اندازی
1. **کلون کردن مخزن:**
   ```bash
   git clone https://github.com/mohammad021/FontRenamer.git
   cd FontRenamer
   ```

2. **اجرای اسکریپت:**
   ```bash
   python fontrenamer.py
   ```

#### نحوه استفاده
1. **تغییر نام فایل‌های فونت:**
   برای تغییر نام فایل‌های فونت در دایرکتوری جاری، اسکریپت را اجرا کنید:
   ```bash
   python fontrenamer.py
   ```

#### جزئیات اسکریپت
1. **install_package:**
   - یک پکیج را با استفاده از pip نصب می‌کند.

2. **get_font_info:**
   - نام و سبک فونت را از فایل فونت استخراج می‌کند.

3. **تغییر نام فایل‌های فونت:**
   - فایل‌های فونت را براساس نام و سبک استخراج شده تغییر نام می‌دهد.

#### لایسنس
این پروژه تحت لایسنس MIT منتشر می‌شود.

---


### **Font Renamer: A Python Script for Renaming Font Files**

`fontrenamer.py` is a Python script designed to rename font files (e.g., .ttf, .woff, .woff2, .otf) based on the font name and style. This script helps web developers and designers keep their fonts organized and easily identifiable.

#### Features
- **Automatic Installation of Required Libraries:** The script installs the necessary Python libraries (`fonttools` and `brotli`) if they are not already installed.
- **Extract Font Information:** Extracts the name and style of the font from the font file.
- **Rename Font Files:** Renames font files based on the extracted name and style.

#### Prerequisites
1. **Python 3.6 or higher**
   - You can download and install Python from [Python.org](https://www.python.org).

#### Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohammad021/FontRenamer.git
   cd FontRenamer
   ```

2. **Run the Script:**
   ```bash
   python fontrenamer.py
   ```

#### Usage
1. **Renaming Font Files:**
   To rename the font files in the current directory, run the script:
   ```bash
   python fontrenamer.py
   ```

#### Script Details
1. **install_package:**
   - Installs a package using pip.

2. **get_font_info:**
   - Extracts the name and style of the font from the font file.

3. **Renaming Font Files:**
   - Renames font files based on the extracted name and style.

#### License
This project is released under the MIT License.

---
