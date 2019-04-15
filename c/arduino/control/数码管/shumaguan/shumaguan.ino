int pinDigitron = 2; //管脚D2连接到数码管的A脚，D3连B... D9连h
const int a=6;
const int b=7;
const int c=9;
const int d=11;
const int e=12;
const int f=5;
const int g=4;
const int h=8;
int pins[8]={a,b,c,d,e,f,g,h};
void setup() {
   pinMode(a, OUTPUT); //设置各脚为输出状态
   pinMode(b, OUTPUT);
   pinMode(c, OUTPUT);
   pinMode(d, OUTPUT);
   pinMode(e, OUTPUT);
   pinMode(f, OUTPUT);
   pinMode(g, OUTPUT);
   pinMode(h, OUTPUT);
   Serial.begin(9600);
}
 
//在数码管中显示数字的函数
void displayDigit(int digit) {
  //定义一个数组表：不同数字的abcdefgh各段的取值
  int abcdefgh[][8] = {
    {0,0,0,0,0,0,1,1},  //0
    {1,0,0,1,1,1,1,1},  //1
    {0,0,1,0,0,1,0,1},  //2
    {0,0,0,0,1,1,0,1},  //3
    {1,0,0,1,1,0,0,1},  //4
    {0,1,0,0,1,0,0,1},  //5
    {0,1,0,0,0,0,0,1},  //6
    {0,0,0,1,1,1,1,1},  //7
    {0,0,0,0,0,0,0,1},  //8
    {0,0,0,0,1,0,0,1},  //9
    {0,0,0,0,0,0,1,0},  //10
    {1,0,0,1,1,1,1,0},  //11
    {0,0,1,0,0,1,0,0},  //12
//    {1,1,1,0,1,1,1,0},  //A
//    {1,0,0,1,1,1,0,0},  //C
//    {1,1,1,1,1,1,0,0},  //0
//    {0,1,1,0,0,0,0,0},  //1
//    {1,1,0,1,1,0,1,0},  //2
//    {1,1,1,1,0,0,1,0},  //3
//    {0,1,1,0,0,1,1,0},  //4
//    {1,0,1,1,0,1,1,0},  //5
//    {1,0,1,1,1,1,1,0},  //6
//    {1,1,1,0,0,0,0,0},  //7
//    {1,1,1,1,1,1,1,0},  //8
//    {1,1,1,1,0,1,1,0},  //9
//    {1,1,1,0,1,1,1,0},  //A
//    {1,0,0,1,1,1,0,0},  //C
};
if (digit<13){
    for (int x=0; x<8; x++){
        digitalWrite( pins[x], abcdefgh[digit][x]);
        }
    }
}
void loop() {
  for(int i=0;i<13;i++){
  displayDigit(i);
  delay(1000);
  }
}
