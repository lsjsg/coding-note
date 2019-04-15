#include <Adafruit_NeoPixel.h>
#include <WS2812_Definitions.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include <I2Cdev.h>
#include <MPU6050.h>
#define PIN 4
#define LED_COUNT 20

MPU6050 mpu;
SoftwareSerial
    softSerial(7, 8);
int16_t ax, ay, az;
int16_t gx, gy, gz;
Adafruit_NeoPixel leds = Adafruit_NeoPixel(LED_COUNT, PIN, NEO_GRB + NEO_KHZ800);
int val;
int stat;
int mode = 0;
int last = 1;
int last_num = 2;
const int pin = 2;
const int vib = 3
;

void setup()
{
  pinMode(2, INPUT_PULLUP);
  leds.begin();
  clearLEDs();
  leds.show();
  mpu.initialize();
  Serial.begin(9600); //7 rx, 8 tx
  softSerial.begin(9600);
  softSerial.println("ready");
  softSerial.println("1:reminding,2:commands,3:heart_beat,4:tap,5:lights_up,6:light_off,7:celebrate,8:series");
  pinMode(vib, OUTPUT);
}

void reminding()
{
  digitalWrite(vib, HIGH);
  delay(3000);
  digitalWrite(vib, LOW);
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
    if (val > 47 && val < 58)
    {
      val = val - 48;
      last_num = val;
      softSerial.println("last_number=:");
      softSerial.println(last_num);
    }
  }
}

void lights_up()
{
  softSerial.println("lights_up");
  int rainbowScale = 192 / LED_COUNT;

  for (int a = 0; a < 100; a++)
  {
    for (int i = 0; i < LED_COUNT; i++)
    {
      leds.setPixelColor(i, rainbowOrder(0));
      leds.show();
    }
    Serial.println(a);
    delay(10);
  }
  delay(1000);
}

void light_off()
{
  softSerial.println("lights off");
  for (int a = 100; a >= 0; a--)
  {
    for (int i = 0; i < LED_COUNT; i++)
    {
      leds.setPixelColor(i, rainbowOrder(0));
      leds.show();
    }
    Serial.println(a);
    delay(10);
  }
  delay(1000);
}

void imu()
{
  softSerial.println("imu");
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  int16_t ax1, ay1, az1;
  ax1 = map(ax, -17000, 17000, 0, 255);
  ay1 = map(ay, -17000, 17000, 0, 255);
  az1 = map(az, -17000, 17000, 0, 255);
  for (int a = 0; a < 9; a += 3)
  {
    leds.setPixelColor(a, rainbowOrder(ax1));
  }
  for (int b = 1; b < 9; b += 3)
  {
    leds.setPixelColor(b, rainbowOrder(ay1));
  }
  for (int c = 2; c < 9; c += 3)
  {
    leds.setPixelColor(c, rainbowOrder(az1));
  }
  leds.show();
  delay(100);
}

void heart_beat()
{
  softSerial.println("heart beat");
  int rainbowScale = 192 / LED_COUNT;

  for (int a = 0; a < 100; a++)
  {
    for (int i = 0; i < LED_COUNT; i++)
    {
      leds.setPixelColor(i, a);
      leds.show();
    }
    Serial.println(a);
    delay(10);
  }
  for (int a = 100; a >= 0; a--)
  {
    for (int i = 0; i < LED_COUNT; i++)
    {
      leds.setPixelColor(i, a);
      leds.show();
    }
    Serial.println(a);
    delay(10);
  }
}

void (*resetFunc)(void) = 0;

void tap()
{
  softSerial.println("tap");
  stat = digitalRead(pin);
  if (stat == LOW and last == 1)
  {
    mode = 1;
    last = 0;
  }
  else if (stat == HIGH and last == 0)
  {
    last = 1;
  }
}

void clearLEDs()
{
  for (int i = 0; i < LED_COUNT; i++)
  {
    leds.setPixelColor(i, 0);
  }
}
void rainbow(byte startPosition)
{
  // Need to scale our rainbow. We want a variety of colors, even if there
  // are just 10 or so pixels.
  int rainbowScale = 192 / LED_COUNT;

  // Next we setup each pixel with the right color
  for (int i = 0; i < LED_COUNT; i++)
  {
    // There are 192 total colors we can get out of the rainbowOrder function.
    // It'll return a color between red->orange->green->...->violet for 0-191.
    leds.setPixelColor(i, rainbowOrder((rainbowScale * (i + startPosition)) % 192));
  }
  // Finally, actually turn the LEDs on:
  leds.show();
}

uint32_t rainbowOrder(byte position)
{
  // 6 total zones of color change:
  if (position < 31) // Red -> Yellow (Red = FF, blue = 0, green goes 00-FF)
  {
    return leds.Color(0xFF, position * 8, 0);
  }
  else if (position < 63) // Yellow -> Green (Green = FF, blue = 0, red goes FF->00)
  {
    position -= 31;
    return leds.Color(0xFF - position * 8, 0xFF, 0);
  }
  else if (position < 95) // Green->Aqua (Green = FF, red = 0, blue goes 00->FF)
  {
    position -= 63;
    return leds.Color(0, 0xFF, position * 8);
  }
  else if (position < 127) // Aqua->Blue (Blue = FF, red = 0, green goes FF->00)
  {
    position -= 95;
    return leds.Color(0, 0xFF - position * 8, 0xFF);
  }
  else if (position < 159) // Blue->Fuchsia (Blue = FF, green = 0, red goes 00->FF)
  {
    position -= 127;
    return leds.Color(position * 8, 0, 0xFF);
  }
  else //160 <position< 191   Fuchsia->Red (Red = FF, green = 0, blue goes FF->00)
  {
    position -= 159;
    return leds.Color(0xFF, 0x00, 0xFF - position * 8);
  }
}

void celebrate()
{
  softSerial.println("celebrate");
  for (int i = 0; i < LED_COUNT * 10; i++)
  {
    rainbow(i);
    delay(100);
  }
}

void series()
{
  softSerial.println("series");
  reminding();
  for (int i = 0; i < 1; i++)
  {
    lights_up();
  }
  while (mode == 0)
  {
    tap();
  }
  celebrate();
  for (int i = 0; i < 180; i++)
  {
    imu();
  }
  for (int i = 0; i < 100; i++)
  {
    heart_beat();
  }
  resetFunc();
}

void loop()
{
    series();
  while(true){
    delay(10);
  }
  while (last_num == 2)
  {
    commands();
  }
  if (last_num == 1)
  {
    softSerial.println("case 1");
    reminding();
    resetFunc();
  }
  else if (last_num == 2)
  {
    softSerial.println("case 2");
    commands();
    resetFunc();
  }
  else if (last_num == 3)
  {
    softSerial.println("case 3");
    for(int i;i<30;i++){
    heart_beat();
    }
    resetFunc();
  }
  else if (last_num == 4)
  {
    softSerial.println("case 4");
    tap();
    resetFunc();
  }
  else if (last_num == 5)
  {
    softSerial.println("case 5");
    for(int i;i<30;i++){
    lights_up();
    }
    resetFunc();
  }
  else if (last_num == 6)
  {
    softSerial.println("case 6");
    light_off();
    resetFunc();
  }
  else if (last_num == 7)
  {
    softSerial.println("case 7");
    celebrate();
    resetFunc();
  }
  else if (last_num == 8)
  {
    softSerial.println("case 8");
    series();
    resetFunc();
  }
}
