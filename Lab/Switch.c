#include "sensos_api.h" // 헤더 선언
void Init_INT() // Interrupt 관련 레지스터 초기화
{
  TCON = 0x00
  EA = 1;
  EX0 = 1;
  EX1 = 1;
  PX1 = 1;
}
void EX0_int(void) interrupt 0 // 외부 인터럽트 0의 동작을 나타내는 함수
{
  SENSOS_CLCD_CLEAR();
  SENSOS_CLCD_STRING(0,2,"Interrupt0 TEST!"); // 외부 인터럽트 0이 활성화 되는 동안 LCD 화면 0번째 열의 2번째 시작 포인터로 하여 스트링 출력
}
void main()
{
  Init_INT();
  SENSOS_CLCD_CLEAR(); // LCD 초기화 함수
  SENSOS_CLCD_STRING(0,2,"SENSOS EVB TEST!"); // 시작 열, 시작 포인터, 문자열 순으로 작성.
  SENSOS_CLCD_STRING(2,2,"LCD_TEST_EXAMPLE"); // 커서의 위치를 2번째 줄 2번째 부터 'PUSH_SW_EXAMPLE' cnffur
  whlie(1);
}
