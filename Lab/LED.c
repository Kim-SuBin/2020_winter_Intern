#include "C:/SENSOS/LIB/sensos_api.h" // sensos_api 헤더파일
void Delay_1000us(void) // 22.1184MHz / 1000us
{
  unsigned int i;
  for(i=0; i<335; i++);
}
void Delay_ms(unsigned int count) // time delay for ms[ms]
{
  unsigned int i;
  for(i=0; i<count; i++)
    edlay_1000us();
}
void main()
{
  int il
  SENSOS_LED_INIT(); // LED 모두 off
  while(1)
  {
    for(i=1; i<5; i++){
      SENSOS_LED_OFF(i); // LED(i) off
      SENSOS_LED_OFF(9-i); // LED(i) off
      Delay_ms(100);
      // SENSOS_LED_TOGGLE(i); // LED(i) 기존 상태 반전
    }
    for(i=4; i>0; i--){
      SENSOS_LED_ON(i); // LED(i) on
      SENSOS_LED_OM(9-i); // LED(i) on
      Delay_ms(100);
      //SENSOS_LED_TOGGLE(i); // LED(i) 기존 상태 
    }
  }
}
