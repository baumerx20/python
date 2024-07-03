//Garage Door Home Reciever
//Ading Buzzer for Alarm to Sound

#include <heltec.h>

// Define Band Location

#define BAND 915E6

//Hall Sensor definition
#define Hall_Sensor 21

// Garage Open True
bool O_garage = true;

String O_stat = "";

//packet counter

unsigned int counter = 0;
String rssi = "RSSI --";
String packSize = "--";
String packet ;


//Define LED


// Example Setup for testing
// Not used as my Reciever does not use a display
void loraSetup()
{
  //Prime Radio for LORA
  Heltec.begin(true /*DisplayEnable Enable*/, true /*Heltec.Heltec.Heltec.LoRa Disable*/, true /*Serial Enable*/, true /*PABOOST Enable*/, BAND /*long BAND*/);

 //Set up Display Parameters and Initialize
  Heltec.display->init();
  Heltec.display->flipScreenVertically();  
  Heltec.display->setFont(ArialMT_Plain_10);
  
  delay(1500);
  Heltec.display->clear();

  //Display Radio State
  Heltec.display->drawString(0, 0, "Heltec.LoRa Initial success!");
  Heltec.display->display();
  delay(1000);
}

// State Changes 
void doorChanged()
{
  // Detect Change in Hall Sensor
  if(digitalRead(Hall_Sensor) >+ 0){
   O_garage = !O_garage;
   //Set State of Garage to Open
   O_stat = "Open";
   //Send a message: initialize
   Serial.print("Sending packet: OpenLED\r\n");
   // send packet
   LoRa.beginPacket();
   // Packets limited
   // Look up LORA Packet max size
   LoRa.print("Garage Open");
   LoRa.endPacket();
  }
  else {
   // If the garage isnt open, then the STATE is always closed.
   O_stat = "Closed";
   Serial.print("Sending packet: CloseLED\r\n");
   // send packet
   LoRa.beginPacket();
   LoRa.print("Garage Closed");
   LoRa.endPacket();
  }
   
}

// Define the process to run at main
void startGarage()
{
  pinMode(Hall_Sensor, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(Hall_Sensor), doorChanged, O_garage);
}

// LORA Initialization object for display
// NOTE My Alarm does not have a display for recieving
void LoRA()
{
  Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_10);
  
  Heltec.display->drawString(0, 0, "Sending packet: ");
  Heltec.display->drawString(90, 0, String(counter));
  Heltec.display->display();

  // send packet
  LoRa.beginPacket();
  
/*
 * LoRa.setTxPower(txPower,RFOUT_pin);
 * txPower -- 0 ~ 20
 * RFOUT_pin could be RF_PACONFIG_PASELECT_PABOOST or RF_PACONFIG_PASELECT_RFO
 *   - RF_PACONFIG_PASELECT_PABOOST -- LoRa single output via PABOOST, maximum output 20dBm
 *   - RF_PACONFIG_PASELECT_RFO     -- LoRa single output via RFO_HF / RFO_LF, maximum output 14dBm
*/
  LoRa.setTxPower(14,RF_PACONFIG_PASELECT_PABOOST);
  LoRa.print("Garage Status: ");
  LoRa.print(O_stat);
  LoRa.endPacket();

  counter++;
  //digitalWrite(LED, HIGH);   // turn the LED on (HIGH is the voltage level)
  //delay(1000);                       // wait for a second
  digitalWrite(LED, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}


//set up the LORA Serial Connection to Reciever and monitor
//For testng
void setup() {
  //initialize Serial Monitor
  Serial.begin(115200);
  loraSetup();
  startGarage();
  
}
void loop() {
  doorChanged();
  LoRA();

  delay(10000);
}
