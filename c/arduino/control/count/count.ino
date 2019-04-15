int timeup=2;
int show=3;
int num=0;
int last;
int state;
void setup() {
  // put your setup code here, to run once:
pinMode(timeup,INPUT_PULLUP);
pinMode(show,INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
state=digitalRead(timeup);
  if (last!=state and state==LOW){
    num++;
    last=LOW;
    Serial.println(num);
    }
  else if (last==state and state==LOW){
    Serial.println("the same");
  }
  else{
    last=HIGH;
    Serial.println("rest");
    Serial.println(num);
    }
}
