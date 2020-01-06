### 온도 센서 (Temperature Sensor) &#91;LM35DZ&#93;
- LM35DZ는 0~100&deg;C의 온도 측정 범위를 가지며, 섭씨온도(&deg;C)에 대해 선형적으로 비례하는 전압 출력
- 0&deg;C일 때, 0.00V를 출력하고 1&deg;C 증가 할 때 마다 10.0mV씩 증가되는 아날로그 신호 출력
- 측정된 온도 데이터가 ADC 칩을 통해 디지털 신호로 변환되어 FPGA 내부의 MCU(SU8051)에 입력됨
- **LM35DZ**의 주요 특징
  - Wafer-level 트리밍과 보정으로 가격 저렴
  - 비선형 범위가 &#177;1/4&deg;C
  - 사용 전원 범위가 넒음 (+4V ~ +30V)
  - 누설 전류가 작음 (60&micro;A 이하)
  - 공기 중 자체 발생온도가 작음 (0.08&deg;C)
  - 낮은 임피던스 출력을 가짐 (1mA일 때 0.1&Omega;)
### 조도 센서 (Visible Light Sensor) &#91;GL5537&#93;
- GL5537은 Cds Photocell
- 카드뮴의 황화물인 황화카듀뮴(CdS)은 가시광선에 의해 전기전도율이 달라지는 반도체 특성을 갖고 있어 광전부품의 일반적인 재료로 사용
- GL5537은 광 변화에 따라 저항 특성이 달라지므로 기본적인 저항분배기 회로만을 구성하여 손쉽게 광량 감지 가능
- GL5537은 가격이 저렴하여 센서등, 방범등 같은 조명기구로 많이 사용
- SG100F와 SN100S에서는 측정된 광량이 ADC 칩을 통해 디지털 신호로 변환되어 FPGA 내부의 MCU(SU8051)에 입력됨
- **GL5537**의 특징
  - 전력 소모 (at 25) : 100mV
  - 최대 전압 : 150Vdc or AC
  - 온도 범위 : -30 ~ +70&deg;C
  - Light Resistance at 10 Lux (at 25) : min 20, max 560Kohm
  - Gamma Value at 10 ~ 100 Lux : 0.7typ
  - Dark Resistance at 0 Lux (10 sec after shut off 10 Lux) : min 2Mohm
  - Peak Spectral Response : 540nm
### 연기 센서 (Smoke Sensor) &#91;GSAP61&#93;
- 대기 중의 오염 물질(담배 연기, 연료용 가스, 유기용제 등)을 감지하는 센서
- 오염 물질의 정도를 측정한 아날로그 데이터를 ADC 칩을 통해 디지털 신호로 변환하여 FPGA 내부의 MCU(SU8051)에 전달
- **GSAP61**의 특징
  - 정격
    - 히터 입력 전압 (Heater input voltage) : 5V&#177;1%
    - 저항 (Resistance) : 15.0&Omega;&#177;0.2&Omega;
    - 전력소비 (Power consumption) : 650mW 이하
    - 센서 입력 전압 (Sensor input voltage) : 1~12V
  - 전압출력 별 가스 농도
    - PL : 100k&Omega;, Sensor resitance : 400k&Omega;
    - Vout, air : 1.0V (센서 인가전압 5V)
    - 오차 : &#177;7% (온도, 습도 보상 전)
### 기압 센서 (Pressure Sensor) &#91;MPXH6115A&#93;
- 높은 출력 신호와 온도 보정을 목적으로 Bipolar OP-amp 회로와 박막형 저항기를 내장한 반도체 기압 센서 (절대 기압과 현재 기압의 차이를 이용한 기압센서)
- 기압 측정 범위 : 15~115kPa
- 항공고도계나 기압계 등 다양한 응용에 사용
- SG100F에서는 측정된 기압 데이터가 ADC 칩을 통해 디지털 신호로 변환되어 FPGA 내부의 MCU(SU8051)에 입력됨
- **MPXH6115A** 특징
  - 고습도 및 일반 자동차에 저항
  - 고온에서 정확도 향상
  - 소형 및 초소형 패키지로 제공
  - 1.5% Maximum Error over 0&deg; to 85&deg;C
  - 마이크로프로세서(Microprocessor) 또는 마이크로컨트롤러(Microcontroller) 기반 시스템에 적합
  - Temperature Compensated from -40&deg; to +125&deg;C
  - Durable Thermoplastic (PPS) Surface Mount Package
  - 기압 측정 범위 : 15 ~ 115kPa (2.2 ~ 16.7psi)
  - 출력 전압 (Vout) : 0.2~4.8V
  - 정확도 : 
### PIR 센서 (Pyroelectric Infrared Ray Sensor) &#91;GL5537&#93;
### 거리 센서 (Distance Sensor) &#91;GL5537&#93;
### 터치 센서 (Touch Sensor) &#91;GL5537&#93;
### 온습도 센서 (Humidity & Temperature Sensor) &#91;GL5537&#93;
### 이미지 센서 (Image Sensor) &#91;GL5537&#93;
