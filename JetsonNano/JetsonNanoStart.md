# Jetson Nano Start

### Jetson Nano Power Connection
- 총 3가지 방법이 있다.
  1. Micro USB 단자를 통한 전원(총 5V 2A까지 가능)
  2. Barrel Jack 단자를 통한 전원(총 5V 4A까지 가능, j48핀에 점퍼핀을 연결해야함)
  3. GPIO Header(2개의 5V 3A핀이 존재하며 총 6A까지 가능)를 통한 전원
- 5V 2A로는 Jetson Nano가 저전력 모드로 구동되어 일반 모드로 구동하기 위해서 적어도 Barrel Jack 단자를 통한 5V 4A의 전원은 공급해 주어야한다.

### Connection port
- Connect keyboard, mouse, monitor and power adapter ( + J48 pin) to Jetson Nano. <br>
![connectionPort](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/connectionPort.jpg)

### Start
- press 'continue' <br>
![JetsonNAnoStart](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/JetsonNanoStart.jpg)
- Enter the information. <br>
![InsertInformation](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/InsertInformation.jpg)

### Assign IP
- Select Network folder <br>
![NetworkDirectory](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/NetworkDirectory.jpg)
- Select connected ethernet <br>
![AddIP](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/AddIP.jpg)
- Assign IPv4 via Add after clicking 'IPv4 Settings' <br>
![AddIPv4](https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/img/AddIPv4.jpg)
