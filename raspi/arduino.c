#include <Wire.h>
 
#ifdef ARDUINO_SAMD_VARIANT_COMPLIANCE
#define SERIAL SerialUSB
#else
#define SERIAL Serial
#endif
 
unsigned char low_data[8] = {0};
unsigned char high_data[12] = {0};
int           pinPump = 6;
int           waterLevel=0;
int           serialValue=115200;
int           closedDelay=30000;
int           openDelay=100;
 
 
#define NO_TOUCH       0xFE
#define THRESHOLD      100
#define ATTINY1_HIGH_ADDR   0x78
#define ATTINY2_LOW_ADDR   0x77
 
void getHigh12SectionValue(void)
{
  memset(high_data, 0, sizeof(high_data));
  Wire.requestFrom(ATTINY1_HIGH_ADDR, 12);
  while (12 != Wire.available());
 
  for (int i = 0; i < 12; i++) {
    high_data[i] = Wire.read();
  }
  delay(10);
}
 
void getLow8SectionValue(void)
{
  memset(low_data, 0, sizeof(low_data));
  Wire.requestFrom(ATTINY2_LOW_ADDR, 8);
  while (8 != Wire.available());
 
  for (int i = 0; i < 8 ; i++) {
    low_data[i] = Wire.read(); // receive a byte as character
  }
  delay(10);
}

void closePump(void)
{
    digitalWrite(pinPump, HIGH);
    SERIAL.println("colsed");
    delay(closedDelay);
}

void openPump(void)
{
     digitalWrite(pinPump, LOW); 
    SERIAL.println("open");
    delay(openDelay);
}

void check()
{
  int sensorvalue_min = 250;
  int sensorvalue_max = 255;
  int low_count = 0;
  int high_count = 0;
  
  while (1)
  {
    
    uint32_t touch_val = 0;
    uint8_t trig_section = 0;
    low_count = 0;
    high_count = 0;
    getLow8SectionValue();
    getHigh12SectionValue();
    SERIAL.println("looping");
    for (int i = 0; i < 8; i++)
    {
      if (low_data[i] >= sensorvalue_min && low_data[i] <= sensorvalue_max)
      {
        low_count++;
      }
    }
    for (int i = 0; i < 12; i++)
    {
 
      if (high_data[i] >= sensorvalue_min && high_data[i] <= sensorvalue_max)
      {
        high_count++;
      }
    }

    for (int i = 0 ; i < 8; i++) {
      if (low_data[i] > THRESHOLD) {
        touch_val |= 1 << i;
      }
    }
    for (int i = 0 ; i < 12; i++) {
      if (high_data[i] > THRESHOLD) {
        touch_val |= (uint32_t)1 << (8 + i);
      }
    }
    while (touch_val & 0x01)
    {
      trig_section++;
      touch_val >>= 1;
    }
    waterLevel = trig_section * 5;
    if(waterLevel>50)
    {
      closePump();  
    }
    if(waterLevel<0)
    {
      openPump();
    }
    SERIAL.println(waterLevel);
  }
}
 
void setup() {
  pinMode(pinPump, OUTPUT);

  SERIAL.begin(serialValue);
  Wire.begin();
}
 
void loop()
{
  check();
}