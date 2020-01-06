# SENSOS 교육/개발 시스템

### MyUSN 소개
- SENSOS(Seloco USN SOC Solutin)
  - 셀로코(주)에서 개발한 유무선 센터 네트워크 SOC(System On Chip) 및 시스템 솔루션
- MyUSN Station
  - SG100F 게이트웨이와 SN100S 센서노드로 구성
    - SG100F : FPGA에 근거한 센서 네트워크 게이트웨이 플랫폼
    - SN100S : UNS SOC로 구현한 센서 노드
  - 각 보드 모델며으이 끝자리 'F'와 'S'는 적요오딘 기술을 구분하여 FPGA 기반 또는 SOC기반임을 의미
    - FPGA (Field Programmable Gate Array) : <br/> 설계 가능한 논리 소자와 프로그래밍이 가능한 내부 회로가 포함된 반도체 </br>
    - SOC (System On Chip) : <br/> 단일 칩 시스템으로 하나의 집적회로에 집적된 컴퓨터나 전자 시스템 부품을 가리킴 </br>
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
- MyUSN을 구성하는 패키지 목록 <br/> ![MyUSNConfiguration](./img/MyUSNConfiguration.PNG) </br>
- MyUSN 패키지 <br/> </br>
