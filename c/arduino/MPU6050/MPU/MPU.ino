# include <Wire.h>
# include <I2Cdev.h>
# include <MPU6050.h>
MPU6050 mpu;
int16_t ax, ay, az;
int16_t gx, gy, gz;
void setup(){
    mpu.initialize();
    Serial.begin(9600);
    pinMode(12,OUTPUT);
    pinMode(5,OUTPUT);
    pinMode(10,OUTPUT);
    pinMode(8,OUTPUT);   
    pinMode(pin,INPUT_PULLUP);
}
void loop(){
    mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
    ax = map(ax, -17000, 17000, 0, 99);
    ay = map(ay, -17000, 17000, 0, 99);
    az = map(az, -17000, 17000, 0, 99);
    for(int i=0;i<4;i++){
      Serial.print(ax);
      Serial.print("  ");
      Serial.print(ay);
      Serial.print("  ");
      Serial.print(az);
      Serial.print("  ");
      Serial.print(gx);
      Serial.print("  ");
      Serial.print(gy);
      Serial.print("  ");
      Serial.print(gz);
      Serial.print("\n");
    }
}
