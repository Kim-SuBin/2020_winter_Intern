# Google AI vs. IBM AI

### 인공지능 (AI, Artificial Intelligence)
- 인간의 지능이 갖고 있는 기능을 갖춘 컴퓨터 시스템
- 인간의 지능을 기계 등에 인공적으로 시연(구현)한 것
- 일반적으로 범용 컴퓨터에 적용한다고 가정
- 학습, 문제 해결, 패턴 인식 등 주로 인간 지능과 연결된 인지 문제를 해결하는데 주력하는 컴퓨터 공학 분야
- 공 지능 분야에서 파생된 컴퓨터 과학 분야에는 기계 학습(ML, Machine Learning)과 딥러닝(DL, Deep Learning)이 있음
- 기계를 인간 행도의 지식에서와 같이 행동하게 만드는 것으로 기계로부터 만들어지는 지능 의미
- 진화수준에 따라 크게 약한 인공지능(Weak AI), 강한 인공지능(Strong AI), 초인공지능으로 구분(Super AI)
  - 약한 인공지능 : 스스로 사고하며 문제를 해결하는 능력이 없는 컴퓨터 기반의 AI를 의미하며, Google 알파고, IBM Watson 등 '지능적인 행동'을 함
  - 강한 인공지능 : 스스로 사고하며 문제를 해결하는 능력이 있는 컴퓨터 기반의 AI를 의미하며, 스스로 인식, 지각하며 독립성을 가지고 있음. 정신과 자유 의지를 가지고 거듭 진화 가능. 현존하는 기술은 아니지만 이론적으로 인간형 AI와 비인간형 AI로 나뉨
    - 인간형 AI : 인간의 사고와 같이 컴퓨터 프로그램이 행동하고 사고함
    - 비인간형 AI : 인간과 다른 형태의 지각과 사고 추론을 발전시키는 컴퓨터 프로그램
  - 초인공지능 : 인간보다 1000배 이상 뛰어난 지능을 가진 AI로 효율, 자기보존, 자원 획득, 창의성 등의 원초적 욕구를 기반으로 끊임없이 자기 발전 가능

### Google Cloud Platform (GCP)
- Google Cloud는 Google의 데이터센터 인프라를 기반으로 Compute, Storage, Networking, Big Data, Machine Learning 등의 서비스를 제공하는 글로벌 Cloud
![GoogleCloudPlatform](https://t1.daumcdn.net/cfile/tistory/997F5D3359CC9BE217)
- 현재 미국, 유럽, 아시아에 걸쳐 서비스를 제공하고 있으며, 계속해서 추가 데이터센터 건립 중
- AI engine 이용
  - Faces(얼굴 인식): 이미지에서 여러 얼굴을 감지하고 감정상태, wearing headwear 등의 주요 얼굴 관련 속성 제공
  - Logos(로고 감지): 이미지에서 인기 제품 로고를 감지하는 기능
  - Labels(라벨 감지): 이미지에서 교통수단부터 동물까지 광범위한 카테고리를 감지
  - Crop Hints(자르기 힌트): 이미지에서 잘라낼 영역의 꼭지점을 제안
  - Landmarks(랜드마크 감지): 이미지에서 유명한 자연 경관과 인공 구조물을 감지
  - Text Detection(텍스트 감지): 광학 문자 인식(OCR)을 수행. 이미지 내에서 텍스트를 감지하고 추출하며, 광범위한 언어를 지원, 자동 언어 식별이 제공
  - Document / Handwriting Text Detection(문서 텍스트 감지): 광학 문자 인식을 수행하여 이미지의 밀집 문서 텍스트를 감지
  - Image Properties(이미지 속성): 이미지의 주요 색상과 같은 일반적인 속성을 감지
  - Safe Search Properties(세이프 서치 감지): 이미지에서 폭력물 등의 유해 콘텐츠를 감지
  - Web Entities and Pages(웹감지): 이미지에 대한 웹 참조
  - Object Detection(객체 현지화): 이미지의 여러 객체를 감지하여 추출

### IBM Watson
- 자연어 형식으로 된 질문들에 답할 수 있는 인공지능 컴퓨터 시스템
- 정해지지 않은 분야의 질의 응답을 위해 첨단 자연언어처리, 정보획득, 지식표현, 자동추론, 기계학습 기술 등을 적용
- 금융, 방송, 의학, 교육, 쇼핑 등의 분야에 적용됨.
- AI engine 이용
- AI Assistant : <br> 빠르게 챗봇 및 가상 에이전트를 개발하여 모바일 디바이스, 메시징 플랫폼, 로봇을 포함한 다양한 채널에 배치 가능함.
- Discovery : <br> 최첨단 cloud native insight engine으로 데이터에 숨어 있는 가치를 발굴하여 문제를 해결하고 트렌드를 모니터링하며 패턴을 찾아낼 수 있음.
  - Natural Language Understanding : 고급 텍스트 분석을 위한 자연어 처리
  - Discovery News : Watson을 이용하여 더 똑똑한 뉴스를 Application에서 제공할 수 있음.
  - Watson Knowledge Studio : 특정 도메인의 언어를 Watson에게 가르침.
- Language
  - Language Translator : 텍스트를 한 언어에서 다른 언어로 번역함. 전 세계의 뉴스를 자국어로 제공하거나, 고객의 언어로 고객과 소통하는 등 다양한 기능을 제공함.
  - 번역 지원 언어 : 영어, 아랍어, 불어, 독일어, 이탈리아어, 일본어, 포르투갈어, 한국어, 스페인어
  - Natural Language Classifier : 높은 신뢰도롤 자연어를 해석하고 분류함.
- Empathy
  - Personality Insights : 글을 통해 사람의 개성, 필요, 가치관을 예측함. 다수의 고객을 대상으로 개개인의 습관과 기호를 파악할 수 있음.
  - Tone Aalyzer: 텍스트를 통해 감정 및 커뮤니케이션 스타일을 이해함.
- Vision Recognition : <br> 머신 러닝 기술을 사용하여 빠르고 정확하게 시각적 컨텐츠에 테그를 지정하고 컨텐츠를 분류 및 검색함.
- Speech
  - Speech to Text : 손쉽게 소리와 음성을 글로 변환하여 신속하게 내용을 파악할 수 있음.
  - Text to speech : 텍스트를 다양한 언어와 자연스러운 음성 오디오로 변환함.

### Google AlphaGo vs. IBM Watson
|Google AlphaGo|vs.|IBM Watson|
|:---:|:---:|:---:|
|구글 딥마인드|개발사|IBM|
|데미스 허사비스|개발자|데이비드 페루치|
|심층 신경망 기술을 이용한 집중 학습 <br> (가치망+정책망)|학습 방법|기계학습을 통한 셀프러닝|
|2016년 이세돌과 바둑 게임 승리|전적|2013 제퍼디 퀴즈게임 우승|
|의사결정 시스템|특징|자연어 인식 (코그니티브 컴퓨팅)|
|텐서플로우 (TensorFlow)|활용 시스템|클라우드(Cloud)|
|게임, 헬스|주요 응용 산업 분야|의료, 금융 등|

### Google AI vs. IBM AI

|활용 분야|구글|IBM|
|:---:|:---:|:---:|
|언어 영역|자동 번역|자연어 처리|
|언어 이외 영역|무인 자동차, 로봇, 의료생명과학, 검색, 지도, 사진 인식, 동영상 인식 등|언어 영역 외의 연구 프로젝트에 대하여 외부에 알려지지 않았음|
|Big Data 처리 전략|Brain OS (소프트웨어 접근)|시스템 OS (하드웨어 접근)|
|알고리즘|Machine Learning 알고리즘 중심|언어학적 접근/확률 통계적 분석|

### 출처 <br>
https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5 <br>
http://www.itnews.or.kr/?p=18241 
