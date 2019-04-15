const int contr=2;
void setup(){
  pinMode(contr,OUTPUT);
}
void loop(){
  digitalWrite(contr,1);
  Serial.println("HIGH");
  delay(3000);
  digitalWrite(contr,0);
  Serial.println("LOW");
  delay(3000);
}

