├── branches
├── config
├── description
├── HEAD
├── hooks
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

----------

#### ผลลัพธ์การทำงานของโปรแกรม
(1) ผลลัพธ์ของการใช้งานไลบรารีโอเพนซีวีในการตรวจจับใบหน้า

[![Capture.png](https://i.postimg.cc/1z7MX7ZP/Capture.png)](https://postimg.cc/cKYf5mH5)

(2) ผลลัพธ์ของการใช้งานไลบรารีโอเพนซีวีในการตรวจจับมือ

[![2020-04-18-174119-1280x720-scrot.png](https://i.postimg.cc/3JQ1kDzy/2020-04-18-174119-1280x720-scrot.png)](https://postimg.cc/K4QBV4GF)

----------
### โครงสร้างการทำงานของระบบ
----------

--123
---111
