int pinDigitron = 2;    //管脚D2连接到数码管的A脚，D3连B... D9连h
const int a=6;
const int b=7;
const int c=9;
const int d=11;
const int e=12;
const int f=5;
const int g=4;
const int h=8;
const int timeup=3;     //green
const int closed=2;       //blue
int num=6;
long int delay_time;
int pins[8]={a,b,c,d,e,f,g,h};
int last=HIGH;
int lastmode=HIGH;
int state,mode,k;
const int control=13;

void setup(){
    pinMode(a, OUTPUT); 
    pinMode(b, OUTPUT);
    pinMode(c, OUTPUT);
    pinMode(d, OUTPUT);
    pinMode(e, OUTPUT);
    pinMode(f, OUTPUT);
    pinMode(g, OUTPUT);
    pinMode(h, OUTPUT);
    pinMode(13,OUTPUT);
    pinMode(timeup,INPUT_PULLUP);
    pinMode(closed,INPUT_PULLUP);
    Serial.begin(9600);
    }
 
void displayDigit(int digit) {      //在数码管中显示数字的函数
    int abcdefgh[][8] = {           //定义一个数组表：不同数字的abcdefgh各段的取值
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
    }

void waittime(){        //设定时间
    state=digitalRead(timeup);
    Serial.println(state);
    Serial.println(num);
    if (last!=state and state==LOW){
        num++;
        last=LOW;
        displayDigit(num);
        }
    else if (last==state and state==LOW){
        displayDigit(num);
        }
    else{
        last=HIGH;
        displayDigit(num);
        }
    }

 void delaytime(){
    while (num>12){
        num=num-12;
    }
    num=num+1;
    for (int i=0;i<num;i++){
        delay_time=num*3600;
        delay(3600);
        k=num-1-i;
        displayDigit(k);
        }
    } 

void confirm(){
    mode=digitalRead(closed);
    while (lastmode==1){
        if (mode!=lastmode and mode==LOW){
            delaytime();
            lastmode=0;
        }
        else {
            waittime();
            displayDigit(num);
            }
        }
    }
void loop() {
    digitalWrite(13,HIGH);
    confirm();
    digitalWrite(13,LOW);
    delay(5400);
    digitalWrite(13,HIGH);
}
