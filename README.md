### วิธีการติดตั้งโปรแกรม
----------
#### Download & install Application
Download:

----------
#### Install Opencv-Python on Raspberry pi 4 
----------
1. Update & Upgrade แพ็คเกจของราสเบอร์รีพาย
 ```bash
  sudo apt-get update && sudo apt-get upgrade
 ```
2.	ติดตั้งเครื่องมือในการใช้งานโอเพนซีวีคือ CMake สำหรับเป็นตัวช่วยในการกำหนดค่ากระบวนการสร้างโอเพนซีวี
 ```bash
  sudo apt-get install build-essential cmake pkg-config
 ```
3. ติดตั้งไลบรารีของรูปภาพ วิดีโอ และคำสั่งการใช้งานพื้นฐานที่เกี่ยวข้องสำหรับใช้งานโอเพนซีวี
```bash
  sudo apt-get install cmake gfortran
  sudo apt-get install libjpeg-dev libtiff-dev libgif-dev
  sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
  sudo apt-get install libgtk2.0-dev libcanberra-gtk*
  sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
  sudo apt-get install libtbb2 libtbb-dev libdc1394–22-dev libv4l-dev
  sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev
  sudo apt-get install libjasper-dev liblapack-dev libhdf5-dev
  sudo apt-get install gcc-arm* protobuf-compiler
 ```
4. ทำการดาวน์โหลดโอเพนซีวีสำหรับราสเบร์รีพาย
- ดาวน์โหลดโอเพนซีวี
 ```bash
  cd ~
  wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
  wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
 ```
- ทำการแตกซิปไฟล์ที่ดาวน์โหลดมา
 ```bash
  unzip opencv.zip
  unzip opencv_contrib.zip
 ```
- ทำการเปลี่ยนชื่อไฟล์ของโอเพนซีวีเพื่อนำไปใช้งานในโครงงาน
 ```bash
  mv opencv-4.0.0 opencv
  mv opencv_contrib-4.0.0 opencv_contrib
 ```
5. ทำการติดตั้งนัมพาย
 ```bash
  pip install numpy
 ```
----------
#### Install Webcam on Raspberry pi 4 
----------
```bash
  sudo apt-get install fswebcam
 ```
#### คำอธิบายการใช้งาน
```bash
  เมื่อทำการติดตั้ง OpenCV และ Webcam บน Raspberry pi เรียบร้อยแล้ว ผู้ใช้สามารถเรียกใช้งาน การทำงานของกล้องเว็บแคมในการตรวจจับใบหน้าเพื่อสร้างระบบเตือนภัยอัตโนมัติและการทำงานของกล้องเว็บแคมในการตรวจจับมือเพื่อสร้างระบบควบคุมเครื่องใช้ไฟฟ้าอัตโนมัติ
 ```
 1. การใช้งานแอปพลิเคชันในการควบคุมการเปิดและปิดไฟ

- ทำการรันเซิร์ฟเวร์ของราสเบอร์รีพายก่อนพื่อให้แอปพลิเคชันสามารถควบคุมการทำงานการเปิดและปิดของหลอดไฟได้
[![server.jpg](https://i.postimg.cc/Bn12p7xm/server.jpg)](https://postimg.cc/gxmwkDth)

ไฟล์เซิร์ฟเวร์สามารถดาวน์โหลดได้ที่: [server.py]()

- แอปพลิเคชันสำหรับควบคุมการเปิดและปิดไฟจะประกอบด้วยหน้าสำหรับควบคุมการทำงานและหน้าสำหรับแก้ไขชื่อของหลอดไฟแต่ละหลอด โดยในส่วนของหน้าแอปพลิเคชันสำหรับควบคุมการทำงานของหลอดไฟแต่ละหลอดจะแสดงรายละเอียดดังภาพ
[![App-control.jpg](https://i.postimg.cc/KvbYwqS9/App-control.jpg)](https://postimg.cc/5jP1Fmtv)

- ผู้ใช้สามารถควบคุมการเปิดและปิดไฟซึ่งในหน้าหลักของแอปพลิเคชันสามารถให้ผู้ใช้เลือกควบคุมเปิดและปิดไฟแต่ละหลอดได้ ซึ่งในหน้าหลักของแอปพลิเคชันนี้ จะประกอบไปด้วยหลอดไฟ 4 หลอด หลอดไฟแต่ละหลอดจะอยู่ในแต่ละห้อง โดยที่ผู้ใช้เลือกปุ่ม “ON / OFF” ตามความต้องการของผู้ใช้ในการควบคุมการเปิดและปิดไฟ ถ้าผู้ใช้ต้องการเปิดไฟหลอดที่ 1 ผู้ใช้สามารถกดปุ่ม “ON หรือ OFF” เพื่อเปิดหรือปิดไฟ และถ้าผู้ใช้เปิดไฟ แอปพลิเคชันจะแสดงสถานะการเปิดไฟขึ้นโดยที่หลอดไฟจะเปลี่ยนเป็นสีเหลืองดังรูป และข้อความที่อยู่ด้านหน้ารูปของหลอดไฟจะบอกสถานะว่า หลอดไฟเปิดหรือปิดอยู่ ถ้ารูปหลอดไฟเปลี่ยนเป็นสีเหลืองแสดงว่าหลอดไฟเปิดอยู่ ถ้ารูปหลอดไฟไม่ใช่สีแหลืองแสดงว่าหลอดไฟปิดอยู่ ดังภาพ
[![app3.jpg](https://i.postimg.cc/SNxBnCWS/app3.jpg)](https://postimg.cc/14bCTgC2)

2.	การใช้งานแอปพลิเคชันในการเปลี่ยนชื่อของหลอดไฟ

- ผู้ใช้สามารถกดที่เมนู “Edit name Lamp” และหน้าแอปพลิเคชันจะเข้ามาสู่การแก้ไขชื่อของหลอดไฟแต่ละหลอด เมื่อผู้ใช้แก้ไขชื่อเรียบร้อยแล้ว ระบบจะทำการบันทึกข้อความที่ผู้ใช้กรอกและนำไปแสดงชื่อของหลอดไฟ โดยข้อมูลทั้งหมดจะถูกเก็บไว้ในฐานข้อมูลไฟร์เบส
[![Edit-Lamp.jpg](https://i.postimg.cc/wBpFmYSX/Edit-Lamp.jpg)](https://postimg.cc/68MCkg6q)













