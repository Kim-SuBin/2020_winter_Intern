# SENSOS 교육/개발 시스템

### MyUSN 소개
- SENSOS(Seloco USN SOC Solution)
  - 셀로코(주)에서 개발한 유무선 센터 네트워크 SOC(System On Chip) 및 시스템 솔루션
- MyUSN Station
  - SG100F 게이트웨이와 SN100S 센서노드로 구성
    - SG100F : FPGA에 근거한 센서 네트워크 게이트웨이 플랫폼
    - SN100S : UNS SOC로 구현한 센서 노드
  - 각 보드 모델명의 끝자리 'F'와 'S'는 적요오딘 기술을 구분하여 FPGA 기반 또는 SOC기반임을 의미
    - FPGA (Field Programmable Gate Array) : <br> 설계 가능한 논리 소자와 프로그래밍이 가능한 내부 회로가 포함된 반도체 </br>
    - SOC (System On Chip) : <br> 단일 칩 시스템으로 하나의 집적회로에 집적된 컴퓨터나 전자 시스템 부품을 가리킴 </br>
- 범용 8bit MCU와 표준 JPEG encoder가 하나의 칩에 통합된 영상처리 프로세서 기반의 플랫폼
- USN(Ubiquitous Sensor Network) 환경에서 발생하는 다양한 정보 수집 및 제공을 위한 유무선 센서 네트워크 시스템 개발용 플랫폼

### MyUSN 특징
- USN 교육을위한 표준 플랫폼 지원
- 센서 네트워크용 임베디드 OS SenQ51(ETRI 기술이전 : NanoQplus를 8051 MCU에 포팅)
- 홈 네트워크, 빌딩 관리, 환경 모니터링 등 다양한 응용 센서 제공
- 간편한 칩 안테나를 적용한 RF(Radio Frequency) 모듈
- 높은 전송 속도, 신뢰성을 보장하는 유선 Ethernet 통신 지원
- 확장성, 개방성을 보장하는 무선 RF(Radio Frequency) 통신 지원
- 이미지센서 기반의 영상과 환경 센서를 융합한 복합 기술 지원

### MyUSN 구성
- MyUSN은 다양한 센서 네트워크 응용에 활용할 수 있도록 다양한 센서와 네트워크 인터페이스 지원
- MyUSN을 구성하는 패키지 목록 <br> ![MyUSNConfiguration](./img/MyUSNConfiguration.PNG) </br>
- MyUSN 패키지 <br> ![MyUSNPackage](./img/MyUSNPackage.PNG) </br>
- **SG100F**
  - FPGA 기반의8051 MUC와 JPEG encoder를 중심으로 UART, Ethernet, ZigBee, WiFi 등의 통신 모듈과 오도, 조도, 연기, 기압, 동작, 거리, 터치, 온습도, 이미지 등의 센서 모듈 및 LCD, LED와 Push Switch 등 다양한 입출력 소자들 포함
  - 메모리맵
    - SG100F의 FPGA에는 8bit MCU인 SU8051과 JPEG encoder가 내장되어 있음
    - 64kByte의 프로그램 메모리와 64kByte의 외부 데이터 메모리를 갖고 있음
    - 프로로그램 메모리 : 사용자가 만든 응용 프로그램이 저자오디는 메모리, Pm39LV010 Flash 메모리 적용
    - 외부 데이터 메모리 : 프로그램 수행 중 필요한 데이터 저장용 메모리, IDT71V124SA SRAM 적용
    - 데이터 메모리 : 8000h ~ FFFFh (9p ~ 11p)
      - E000h ~ FFFFh : Ethernet 통신 데이터 수신용 내부 buffer 영역
      - C000h ~ DFFFh : Ethernet 통신 데이터 송신용 내부 buffer 영역
      - A300h ~ A3FFh : RTC(Real Time Clock) 모듈 구동을 위한 영역
      - A000h ~ A2FFh : IO Select 영역
      - 9400h ~ 97FFh : 간접 어드레싱 방식에 의한 JPCON 제어 영역
      - 8000h ~ 8FFFh : Ethernet 제어 관련 영역
  - Clock 인터페이스
    - SG100F는 안정적인 동작 클럭(Clock) 공급을 위해 48MHz OSC를 이용
    - FPGA 내부에서 클럭을 관리하는 리소스인 DCM(Digital Clock Management) 모듈을 통하여 22.1184MHz로 변환시켜 MCU 블록과 JPEG 블록에 제공
    -  SU8051 MCU와 JPEG encoder의 동작 주파수는 22.1884MHz이며, CMOS 이미지 센서 모듈에는 22.1184MHz의 클럭이 공급됨
  - 센서부
    - SG100F에는 총 9종의 센서가 장착되어 있음
    - FPGA에 직접 연결되어 있는 CMOS 이미지 센서와 온습도 센서를 제외하고 기압, 온도, 조도, 움직임, 연기, 거리, 터치 세서는 아날로그 출력값을 갖기 때문에 별도의 ADC IC와 연결되어 있음
    - [각 센서들의 인터페이스와 특징](https://github.com/Kim-SuBin/USN_system_study/blob/master/SG100F_Sensor.md)
  - 통신부
    - UART
      - 2개의 스위치 소자의 enable신호를 제어하여 Host PC &leftrightarrow; MCU, MCU &leftrightarrow; ZigBee, Host PC &leftrightarrow; ZigBee 간의 UART 통신을 수행하도록 설정
      - SU8051 프로그래밍을 통한 스위치 제어가 아니라 수동으로 제어할 수 있도록 제공되는 DIP 스위치(SW4)를 조작하면 Host PC &leftrightarrow; MCU 간의 UART 통신을 수행하도록 설정 가능
    - ZigBee (LM2455-EM)
      - LM2455-EM은 2.4GHz의 비허가 ISM 주파수 대역에 기반을 둔 ZigBee RF 모듈
      - LM2455-EM은 2개의 UART가 있어서 UART0(Z0_TXD, Z0_RXD)는 외부 device와의 시리얼 통신을 수행하고, UART1(Z1_TXD, Z1_RXD)은 ZigBee 프로그래밍 동작을 수행
    - Ethernet
      - 인터넷망을 통해 웹서버에 접속하거나 원활한 데이터 송수신을 위한 유선 Ethernet 기능 지원
      - FPGA에 내장된 8-bit MCU에서는 Ethernet 모듈을 일반 SRAM access 하듯이 제어 가능
      - Ethernet 모듈을 이용한 웹 기반의 네트워크 카메라 기능 제공
      - 특별한 영상 전송 프로토콜을 가지며, 이미지 요청과 전송은 HTTP 프로토콜 그대로 사용
      - Ethernet 모듈 특징
        - Supports 10/100 Base TX
        - Supports half/full duplex operation
        - Supports auto-negotiation and auto crossover detection
        - IEEE 802.3/802.3u Complaints
        - Operates 3.3V with 5V I/O signal tolerance
        - Includes Hardware Internet protocols : TCP, IP Ver 4, UDP, ICMP, ARP, PPPoE, IGMP
        - Includes Hardware Ethernet protocols : DLC, MAC
        - Supports 4 independent connections simultaneously
        - Supports MCU bus Interface and SPI Interface
        - Supports Direct/Indirect mode bus access
        - Supports Socket API for easy application programming
    - WiFi
      - SG100F에 적용된 WiFi 모듈 WizFi630은 RS-232 프로토콜과 TCP/IP 프로토콜을 IEEE802.11 b/g/n 무선 랜 프로토콜로 변환시키는 모듈
      - WizFi630은 RS-232시리얼 인터페이스가 장ㅊㄱ된 장비를 LAN 또는 WLAN 망에 연결하여 원격측정, 관리 및 제어를 가능하게 하는 모듈
      - WizFi630은 Embedded Switch를 내장하고 있어 IP 공유기로서의 기능도 수행
      - WizFi630은 802.11b/g/n 규격을 따르면서, 무선 인터페이스에서 150Mbps의 속도까지 지원
      - WiFi 모듈 특징
        - Complies with IEEE802.11b/g/n
        - Gateway / AP(Bridge) / AP-Client / client(Station) / Ad-hoc Mode,  WDS / Repeater supports
        - 1T1R RF Interface
        - Physical link rate up to 150Mbps
        - Built-in 3 Ethernet Ports
        - 2 Serial Ports supports
        - Working as Wi-Fi Router
        - WEP 64/128bit, WPA/WPA2-PSK TKIP, AES
        - 802.1x (Only in AP mode)
        - 802.11e and WMM (Wi-Fi Multimedia)
        - Router and Firewall function supports
  - 입출력부
    - PUSH Switch
      - 외부 입력 신호 제어를 위해 사용
      - Push Switch와 연결된 p3.2와 p3.3은 FPGA에 내장된 MCU(SU8051)의 외부 인터럽트 INTO와 외부 인터럽트 INT1의 역할 수행
    - LED / 7-Segment / CLCD / GLCD
      - UC5000C의 데이터 버스(GPIO의 Port0)를 사용하며 이를 제어하기 위해 외부 데이터 메모리 A000h번지와 A100h번지를 액세스 하며 /IOSEL1신호와 /IOSEL2신호를 활성화시켜 신호 전달
    - External GPIO
      - External GPIO를 사용하지 않는 핀의 경우 우측으로 설정해야만 보드 내부 디바이스의 기능을 정상적으로 수행 가능
    - FPGA Extension Pin (FPGA 확장 핀)
      - 사용자가 FPGA 확장 핀을 활용한다는 것은, FPGA 내부에 구현된 UC5000C 기능에 Hardware level에서 원하는 기능을 사용자 모듈로 추가 설계/통합 한 후 다시 FPGA에 구현해야 함을 의미
      - 사용자는 다음 과정을 수행해야 함
        -RTL level에서 HDL 설계언어(VHDL, Verilog)를 사용하여 사용자가 원하는 기능의 block(User Designed Module)을 설계하고 Function simulation 검증 tool(Modelsim, NCsim 등)을 통한 기능 검증 수행
        - 사용자 block과 UC5000C IP를 통합 (RTL level로 통합 설계)
        - UCF 파일에서 사용자 용도에 맞게 FPGA핀을 재선언
        - Xilinx사의 ISE에서 컴파일/합성 수행, 비트 파일(.bit) 생성
        - Xilinx사의 ISE에서 PROM 다운로드용 파일(.mcs)생성
        - Xilinx사의 ISE에서 FPGA configuration PROM에 다운
      - Extension Pin을 활용하기 위해 추가적으로 필요한 사항
        - Xilinx사의 ISE 프로그램은 HDL synthesis tool로 이 tool을 사용하면 HDL로 기술한 회로를 Xilinx사에서 개발한 FPGA에 합성 가능. ISE 프로그램은 Xilinx 홈페이지에서 회원가입 후 무료 배포 버전인 Xilinx WebPACK을 다운받아 사용 가능
        - FPGA configuration을 위해서는 PC와 SG100F 보드를 연결하는 JTAG cable이 필요. 세로코(주)에 구매 신청하면 됨
        - SG100F에 내장된 UC5000C IP는 edif 형태로 공급되며, 셀로코(주)에서 별도로 구매 신청하여 배포 받을 수 있음
      - 출력소자 연결 시 : FPGA의 보호와 안정적인 동작을 위해 풀업 저항 권장
      - 입력소자 연결 시 : FPGA를 손상시키지 않도록 직렬 저항 설치
    - Switch
      |Part Name|SWITCH Name|Description|
      |:===:|:===:|:===:|
      |SW1|FPGA configuration S/W	|ON : JTAC mode <br> OFF : operation mode </br>|
      SW2	Power S/W	ON : Power ON
OFF : Power OFF
SW3	RESET push S/W	Reset switch
SW4	Serial 통신 Manual S/W	1 : 스위치 회로 소자 전원 ON/OFF
2 : Port3.1(TXD) manually connection ON/OFF
3 : Port3.0(RXD) manually connection ON/OFF

SW5	ZigBee ISP S/W	ON : ISP mode
OFF : normal mode
SW6	LCD & FND Power S/W	1 : LCD power ON/OFF
2 : FND power ON/OFF

SW7	Port3.2(/INT0) push S/W	Port3.2 switch
SW8	Port3.3(/INT1) push S/W	Port3.3 switch
SW27	ISP mode S/W	ON : ZigBee programming 설정
OFF : Flash programming 설정
SW28	Ethernet/WiFi SELECT S/W
(TXOP, TXON 신호)	1-2(UP) : Ethernet SELECT
2-3(DOWN) : WiFi SELECt
SW29	Ethernet/WiFi SELECT S/W
(RXIP, RXIN 신호)	1-2(UP) : Ethernet SELECT
2-3(DOWN) : WiFi SELECT
    - RTC(Real Time Clock)부
      - RTC 모듈 DS12C887은 별도의 어드레스 입력이 없으며 내부에 배터리가 내장되어 있어 외부 전원공급 없이 10년 동안 동작 가능
      - 비휘발성 메모리 113바이트가 있어서 전원이 없어도 데이터 값이 지워지지 않음
      - 8-bit 데이터 버스에 연결되어 있으며 FPGA에 내장된 8-bit MCU의 제어에 의해 LCD 모듈로 시간 정보를 출력해 볼 수 있음 (DATA, /RD, /WR, ALE, /RTC_CS)
- **SN100S**

- **MyUSN 하드웨어 연결**
