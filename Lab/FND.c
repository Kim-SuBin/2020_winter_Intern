#include "sensos_api.h" # 헤더 선언
void main() # 7-SEGMENT를 초기화 셋팅한 후 1초 간격으로 숫자값 출력
{
  unsigned int i;
  while(1)
  {
    /* 세그먼트 세팅 */
    SENSOS_SEGMENT_SET(0,1,0); // 표시 위치, 표시 값, dot(점) 활성화 여부 순으로 설정
    SENSOS_SEGMENT_SET(1,2,0);
    SENSOS_SEGMENT_SET(2,3,1); // 세 번째 digit에 숫자 3을 소수점 활성화하여 세팅
    SENSOS_SEGMENT_SET(3,4,0);
    /* 세그먼트 디스플레이 */
    for(i=0; i<1000; i++){
      SENSOS_SEGMENT_DISPLAY(); # SENSOS_SEGMENT_SET() 함수로 셋팅한 내용을 7-SEGMENT에 출력하는 기능 수행
    }
    /* 세그먼트 세팅 */
    SENSOS_SEGMENT_SET(0,5,0);
    SENSOS_SEGMENT_SET(1,6,0);
    SENSOS_SEGMENT_SET(2,7,1);
    SENSOS_SEGMENT_SET(3,8,0);
    /* 세그먼트 디스플레이 */
    for(i=0; i<1000; i++){
      SENSOS_SEGMENT_DISPLAY();
    }
  }
}
