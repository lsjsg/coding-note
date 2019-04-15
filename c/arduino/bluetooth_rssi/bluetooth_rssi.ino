#include <SoftwareSerial.h>
SoftwareSerial test(6,7);
char c;
void setup() {
  Serial.begin(9600);
  test.begin(9600);
  Serial.println("init serial peor AT");
  test.println("init serial port AT");
}

void loop() {
  if (test.available()){
    Serial.write(test.read());
  }
  if (Serial.available()){
    c = Serial.read();
    if (c == '#')
        {
          Serial.print("AT mode ON. $ zeby wyjsc");
        }

        else if (c == "a")
        {
          test.write("AT+inq\n\r");
          Serial.write("AT+inq\n\r");
        }

        else if (c == '$')
        {
          test.write("AT+RESET\n\r");
          Serial.write("AT+RESET\n\r");
        }

        else
        { 
        Serial.write(c);
        test.write(c);  
        }
  }
}
