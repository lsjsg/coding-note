char c = ' ';
byte AtmodePin = 2;
 
void setup() 
{
    pinMode(AtmodePin, OUTPUT);
    digitalWrite(AtmodePin, LOW);
    
    Serial.begin(9600);
    Serial.println("Serial 0 ON");
 
    Serial1.begin(9600);  
    Serial.println("Serial 1 ON");
}
 
void loop()
{
    if (Serial1.available())
    {  
        c = Serial1.read();
        Serial.write(c);
    }
 
    if (Serial.available())
    {
        c =  Serial.read();

        if (c == '#')
        {
          digitalWrite(AtmodePin, HIGH);
          Serial.print("AT mode ON. $ zeby wyjsc");
        }

        else if (c == '$')
        {
          digitalWrite(AtmodePin, LOW);
          Serial1.print("AT+RESET\n\r");
          Serial.print("AT+RESET\n\r");
        }

        else
        { 
        Serial.write(c);
        Serial1.write(c);  
        }
    }
 
}
