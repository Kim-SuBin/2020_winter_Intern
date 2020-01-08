#include "C:/SENSOS/LIB/uart.h" // 헤더 선언
unsigned char uart_set_baudrate(unsigned long _UART_BAUD_RATE) // SFR 레지스터의 TH1 값을 변경해서 baud rate를 설정
{
  switch(_UART_BAUD_RATE)
  {
    case 600 : TH1 = 256-192; break;
    case 1200 : TH1 = 256-96; break;
    case 2400 : TH1 = 256-48; break;
    case 4800 : TH1 = 256-24; break;
    case 9600 : TH1 = 256-12; break;
    case 14400 : TH1 = 256-8; break;
    case 19200 : TH1 = 256-6; break;
    case 38400 : TH1 = 256-3; break;
    case 57600 : TH1 = 256-2; break;
    case 115200 : TH1 = 256-1; break;
    default : return 1;
  }
  return 0;
}
void uart_init2(unsigned long _UART_BAUD_RATE) // UART 통신을 위한 MCU의 특수 제어 레지스터 셋팅, Baud rate는 115200로 설정되어 있음
{
  serial_choice = 0xcc; // IOSEL3신호가 활성화되면서 데이터 0xcc를 D플립플롭(74HC574)에 인가
  TMOD = 0x21; // auto reload mode, Timer0 mode 1
  TCON = 0x51; // Timer1 run for UART communication
  SCON = 0x52; // 8 data, 1 stop, REN = TI = 1
  PCON = 0x8=;
  uart_set_baudrate(_UART_BAUD_RATE);
  //TH = 256-1; // ((2*(221184/12))/(32*1152)); // 115200 bps
  /* Interrupt */
  IE = 0x92; // EX = EX = ET0 = 1
}
void_uart_putc(const char byte) // 하나의 8-비트 아스키코드를 직렬포트에 송신
{
  while(!TI);
  TI = 0;
  SBUF = byte;
}
void uart_puts(const char *str) // uart_putc() 함수를 이용하여 정해진 문자열을 직렬포트에 송신
{
  unsigned char i = 0;
  while ((*(str+i)!='\0')&&(i<255))
  {
    if (*(str+i) == '\n')
    {
      uart)putc('\r');
    }
    uart_putc(*(str+1));
    ++i;
  }
}
unsigned char uart_getc() // 수신단을 통해 수신된 외부 데이터 1byte를 저장
{
  unsigned char byData;
  // Wait till data is received
  while(!RI);
  RI = 0;
  // Read data
  byData = SBUF;
  return byData;
}
unsigned int uart_gets(unsigned char *str, unsigned char str_size) // 수신단을 통해 수신된 문자열 저장
{
  unsigned char *rx_str;
  unsigned char char_cnt;
  unsigned char max_str_size;
  char_cnt = 0;
  rx_str = str;
  max_str_size = str_size;
  while (char_cnt != max_str_size)
  {
    *(rx_str) = uart_getc();
    char_cnt++;
    if (*rx_str == 0x0D)
      break;
    rx_str++;
    if(TI)
    {
      TI = 0;
    }
  }
  str[char_cnt] = '\0';
  return char_cnt;
}
int main() // PC에서 실행한 터미널 창을 통해 UART 통신 확인
{
  char key;
  char str[20];
  uart_init2(115200);
  while(1)
  {
    uart_putc(0x0c);
    uart_puts("\r\n*=========================================*);
    uart_puts("\r\n| SG100F UART TEST (SG100<=>PC(HyperTerminal) |");
    uart_puts("\r\n|----------------------------------------------|");
    uart_puts("\r\n| BaudRate : 115200, DatBit : 8, Parity : x, |");
    uart_puts("\r\n| StopBit : 1, FlowControl : x |");
    uart_puts("\r\n*=========================================*);
    uart_puts("\r\n1.<uart_getC> : Enter 1 characters --> ");
    key = uart_getc(); // HyperTerminal에 메시지 표시하고 1개의 문자를 입력받아 PC로 다시 출력
    uart_puts("\r\n1.<uart_getC> : Return to Pc ==> ");
    uart_putc(key);
    uart_putc("\r\n");
    uart_puts("\r\n2.<uart_getC> : Enter 0~10 characters (Press 'Enter' key End)--> ");
    uart_getc(str, 10); // HyperTerminal로 문자 0~10개의 문자를 입력 받아 PC로 
    uart_puts("\r\n2.<uart_getC> : Return to Pc ==> ");
    uart_putc(str);
    uart_putc("\r\n");
    uart_putc("\r\n3.Press any key ");
    key = uart_getc();
  }
  return 0;
}
