int a=2;
int b=3;
int last, stats;
void setup() {
  // put your setup code here, to run once:
pinMode(2,INPUT_PULLUP);
pinMode(3,INPUT_PULLUP);
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
stats=digitalRead(2);
last=digitalRead(3);
Serial.println(stats);

}
