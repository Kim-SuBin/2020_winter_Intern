# Micro SD Card

### Micro SD Card Format
- SD Card Formatter를 다운로드 하고 설치한다 : <br> https://www.sdcard.org/downloads/formatter_4/eula_windows/ <br> ![SDcardFormatter](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/MicroSDcard.png)
- SD 카드 드라이브를 선택한다.
- Quick format을 선택한다
- Volume label은 비워 둔다.
- Format을 클릭 후 Yes를 눌러 포맷을 시작한다.

### Write image file to Micro SD Card
- 이미지(JetPack)를 다운로드 한다 : <br> https://developer.nvidia.com/jetson-nano-sd-card-image-r3231
- Etcher를 다운로드 하여 설치한다 : <br> https://www.balena.io/etcher
<br> ![EtcherSelectImage](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/EtcherSelectImage.PNG)
-	Select Image를 클릭해 다운로드한 이미지 압축파일을 선택한다.
- PC에 Micro SD Card를 삽입한다.
<br> ![EtcherSelectTarget](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/EtcherSelectTarget.PNG)
-	Select Target를 클릭한 후 Micro SD Card에 해당하는 올바른 드라이브를 선택한다.
-	Flash를 클릭한다. 약 10분~30분 정도 소요된다

### Insert Micro SD Card into Jetson Nano
![InsertMicroSD](https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetson_Nano-Getting_Started-Setup-Insert_microSD.png)


### Jetson Nano Power Connection
- 총 3가지 방법이 있다.
  1. Micro USB 단자를 통한 전원(총 5V 2A까지 가능)
  2. Barrel Jack 단자를 통한 전원(총 5V 4A까지 가능, j48핀에 점퍼핀을 연결해야함)
  3. GPIO Header(2개의 5V 3A핀이 존재하며 총 6A까지 가능)를 통한 전원
- 5V 2A로는 Jetson Nano가 저전력 모드로 구동되어 일반 모드로 구동하기 위해서 적어도 Barrel Jack 단자를 통한 5V 4A의 전원은 공급해 주어야한다.
