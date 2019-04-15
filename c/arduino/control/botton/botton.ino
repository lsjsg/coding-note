const int timeup=2;
const int show=3;
int tim=6;
int a;
void setup() {
  // put your setup code here, to run once:
  pinMode(timeup,INPUT_PULLUP);
  pinMode(timedown,INPUT_PULLUP);
  Serial.begin(9600);
}

void showtime(){
  int b;
  int clic=0
  b=digitalRead(show);
  if b==HIGH){
    Serial.println(tim);
  }
  
}

void runtime(){
  a=digitalRead(timeup);
  if (a==HIGH){
    tim=tim+1;
    Serial.println(tim);
  }
  else{
    tim=tim-1;
    Serial.println(tim);
  }
}
void loop() {
  // put your main code here, to run repeatedly:
  runtime();
}
