
#include <Adafruit_NeoPixel.h>
#include <WS2812_Definitions.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
#define PIN 4
#define LED_COUNT 9
MPU6050 mpu;
SoftwareSerial
softSerial(7, 8);
int16_t ax, ay, az;
int16_t gx, gy, gz;
const int tap = 2;
Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ800);
int val;
int last = 0;
int type = 1;
int stat;
void setup()
{
  pinMode(2, INPUT_PULLUP);
  //leds.begin();
// clearLEDs();
 // leds.show();
  //mpu.initialize();
  Serial.begin(9600); //7 rx, 8 tx
  Serial.println("ready");
  softSerial.begin(9600);
  softSerial.println("ready");
}
void clearLEDs()
{
  for (int i = 0; i < LED_COUNT; i++)
  {
    leds.setPixelColor(i, 0);
  }
}
void commands()
{
  if (Serial.available())
  {
    val = Serial.read();
    softSerial.print(val);
  }
  if (softSerial.available())
  {
    val = softSerial.read();
    Serial.print("val:   ");
    Serial.println(val);
    if (val>13){
    val = val - 48;
    last = val;
    }
  }
}
void loop() {
commands();
Serial.print("last=" );
Serial.println(last);
}
