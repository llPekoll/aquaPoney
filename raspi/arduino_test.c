/*
  This script will work with an 
    Relais for pump
    LED Screen
    temperature sensor
*/

#include <Wire.h>


// oustside temp
#include "DHT.h"
#define DHTPIN 4 
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

//screen
#include "rgb_lcd.h"
rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 0;


// master code
int             pinPump = 6;
bool            pumpIsOpen=false;
unsigned int    counter=0;
unsigned int    timeLeftOpen=35;
unsigned int    cycleTime=300;
 


void loopScreen(unsigned int timeLeft){
      char            discplayString[99];
      lcd.setCursor(0, 1);
      sprintf(discplayString, "%d sec", timeLeft);
      lcd.print(discplayString);

}


void check()
{
    char            outputString[99]; 
    if(counter == 0)
    {
      if(pumpIsOpen == false){
        digitalWrite(pinPump, LOW); 
        Serial.println("pump open");
        pumpIsOpen = true;
      }
    }
     
    if(counter >timeLeftOpen)
    {
      if(pumpIsOpen == true){
        digitalWrite(pinPump, HIGH);
        Serial.println("pump stoped");
        pumpIsOpen = false;
        }
    }
    counter ++;
    if(counter>cycleTime)
    {
     counter=0;
     Serial.println("cycle finished");
    }
          float t_h_val[2] = {0};
      if (!dht.readTempAndHumidity(t_h_val)) {
        // Humidity
        Serial.println(t_h_val[0]);
        // Temperature
        Serial.println(t_h_val[1]);
    } else {
        Serial.println("Failed to get temprature and humidity value.");
    }
    sprintf(outputString, "ctn: %d,pump: %d, hum: %f, temp: %f", counter, pumpIsOpen, t_h_val[0], t_h_val[1]);
    loopScreen((cycleTime - counter));
    Serial.println(outputString);
    delay(1000);
}

void setupPump(){
  pinMode(pinPump, OUTPUT);
  
}

void setupScreen(){
      lcd.begin(16, 2);
    lcd.setRGB(colorR, colorG, colorB);

    // Print a message to the LCD.
    lcd.print("next Cycle in:");
}
void setupTemp(){
      dht.begin();
  }
void setup() {
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