#include <Wire.h>

// oustside temp
#include "DHT.h"
#define DHTPIN 4
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

//screen
#include "rgb_lcd.h"
rgb_lcd lcd;

// master code
const int pinPump = 6;
bool pumpIsOpen = false;
unsigned int counter = 0;
unsigned int cycleNumber = 0;

void loopScreen(unsigned int timeLeft, unsigned int cycleNumber)
{
  char discplayString[16];
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Nxt cycl,cycl Nb");
  lcd.setCursor(0, 1);
  discplayString[0] = '\0';
  sprintf(discplayString, "%d s, %d c", timeLeft, cycleNumber);
  lcd.print(discplayString);
}

void check()
{
  const unsigned int timeLeftOpen = 32;
  const unsigned int cycleTime = 300;
  if (counter == 0)
  {
    if (!pumpIsOpen)
    {
      digitalWrite(pinPump, LOW);
      Serial.println("pump open");
      pumpIsOpen = true;
    }
  }

  if (counter > timeLeftOpen)
  {
    if (pumpIsOpen)
    {
      digitalWrite(pinPump, HIGH);
      Serial.println("pump stoped");
      pumpIsOpen = false;
    }
  }
  float temp_hum_val[2] = {0};
  if (!dht.readTempAndHumidity(temp_hum_val))
  {
    // Humidity
    Serial.println(temp_hum_val[0]);
    // Temperature
    Serial.println(temp_hum_val[1]);
  }
  else
  {
    Serial.println("Failed to get temprature and humidity value.");
  }

  counter++;
  if (counter > cycleTime)
  {
    cycleNumber++;
    counter = 0;
    Serial.println("cycle finished");
  }

  unsigned int timeLeft = cycleTime - counter;
  loopScreen(timeLeft, cycleNumber);
  Serial.print("ctn: ");
  Serial.print(counter);
  Serial.print(",pump: ");
  Serial.print(pumpIsOpen);
  Serial.print(",humi: ");
  Serial.print(temp_hum_val[0]);
  Serial.print(",temp: ");
  Serial.print(temp_hum_val[1]);
  Serial.print("\n");
  delay(1000);
}

void setupPump()
{
  pinMode(pinPump, OUTPUT);
}

void setupScreen()
{
  const int colorR = 255;
  const int colorG = 0;
  const int colorB = 0;

  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
}
void setupTemp()
{
  dht.begin();
}
void setup()
{
  Wire.begin();
  Serial.begin(115200);
  setupPump();
  setupTemp();
  setupScreen();
}

void loop()
{
  check();
}