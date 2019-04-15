int pinDigitron = 2; //管脚D2连接到数码管的A脚，D3连B... D9连h
const int a=6;
const int b=7;
const int c=9;
const int d=11;
const int e=12;
const int f=5;
const int g=4;
const int h=8;
const int timeup=3;//green
const int show=2; //blue
int tim=6;
int mode=0;
long int delaytime;
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
   pinMode(timeup,INPUT_PULLUP);
   pinMode(show,INPUT_PULLUP);
   Serial.begin(9600);
}
//关闭数码管
//void closelights(){
//    for (int x=0; x<8; x++){
//        digitalWrite( pins[x],HIGH);
//    }
//    delay(3000);
//}
 
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
};
while (digit>12){
  digit=digit-12;
}
if (digit<13){
  for (int x=0; x<8; x++){
    digitalWrite( pins[x], abcdefgh[digit][x]);
    }
  }
//delay(1000);
//closelights();
}

void waittime(){
  int b,c;
  int clic=0;
  b=digitalRead(show);
  c=digitalRead(timeup);
  if (c==HIGH){
    
    
  }
}

//void showtime(){
//  int b,c;
//  int clic=0;
//  b=digitalRead(show);
//  c=digitalRead(timeup);
//  if (mode==0 and b==HIGH){
//    mode=1;
//    displayDigit(tim);
//    Serial.println(tim);
//  }
//  else if ( mode==1 and c==HIGH){
//    tim=tim+1;
//    displayDigit(tim);
//    Serial.println(tim);
//  }
//}

void loop() {
showtime();
delaytime=tim*3600*1;
delay(delaytime);
}
