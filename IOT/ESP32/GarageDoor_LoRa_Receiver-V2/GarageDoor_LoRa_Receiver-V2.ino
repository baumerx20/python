#include "heltec.h" 

char Readback[50];
#define BAND    915E6  //band 868E6,915E6
//Define LED GPIO PINS
int redPin = 13;                  // Red LED connected to digital pin 13
int greenPin = 12;                // Green LED connected to digital pin 12

//Define Buzzer Code
// Buzzer disabled
int buzzer_pin = 14;
int button_pin = 27;
int freq = 2000;
int channel = 0;
int resolution = 8;

String rssi = "RSSI --";
String packSize = "--";
String packet ;

void Leds()                      
{
  pinMode(redPin, OUTPUT);        
  pinMode(greenPin, OUTPUT);      
}

void reciever() {
  // try to parse packet
  int packetSize = LoRa.parsePacket();
  
  if (packetSize) {
    // received a packet
    Serial.print("Received packet '");
    // read packet
    while (LoRa.available()) {
    sprintf(Readback+strlen(Readback),"%c",(char)LoRa.read());
    Serial.print(Readback);
    Heltec.display->clear();
    Heltec.display->drawString(0, 0, Readback);
    Heltec.display->display();
     
    }
   
  if(strncmp(Readback, "Garage Open", strlen(Readback)) == 0) {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(buzzer_pin, HIGH);
    
       
   }
  else if(strncmp(Readback, "Garage Closed", strlen(Readback)) == 0) {
    digitalWrite(greenPin, HIGH);
    digitalWrite(redPin, LOW); 
    digitalWrite(buzzer_pin, LOW);  
   }
   memset(Readback,0,50);
   
  }
}

void LoRaData(){
  Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_10);
  Heltec.display->drawString(0 , 15 , "Received "+ packSize + " bytes");
  Heltec.display->display();
}

void cbk(int packetSize) {
  packet ="";
  packSize = String(packetSize,DEC);
  for (int i = 0; i < packetSize; i++) { packet += (char) LoRa.read(); }
  rssi = "RSSI " + String(LoRa.packetRssi(), DEC) ;
  LoRaData();
}

void screen(){
  int packTSize = LoRa.parsePacket();
  if (packTSize) { cbk(packTSize);  }
  delay(10);
}

void buzzer(){
  pinMode(buzzer_pin, OUTPUT);
}

void button(){
  pinMode(button_pin, INPUT_PULLUP);
  int buttonState = digitalRead(button_pin);
  if (buttonState == HIGH) {
    Serial.println("Button Press");
    digitalWrite(buzzer_pin, LOW);
  }
}

void setup() {
  //Serial.begin(115200);
   
  Heltec.begin(true /*DisplayEnable Enable*/, true /*Heltec.Heltec.Heltec.LoRa Disable*/, true /*Serial Enable*/, true /*PABOOST Enable*/, BAND /*long BAND*/);
 
  Heltec.display->init();
  Heltec.display->flipScreenVertically();  
  Heltec.display->setFont(ArialMT_Plain_10);
    
  Heltec.display->drawString(0, 0, "Heltec.LoRa Initial success!");
  Heltec.display->drawString(0, 10, "Waiting for incoming data...");
  Heltec.display->display();
  delay(250);
  //LoRa.onReceive(cbk);
  LoRa.receive();
}


void loop() {
Leds();
reciever();
screen();
button();
}
