#define Hall_Sensor D2

void setup()
{
  Serial.begin(9600);
 
  pinMode(Hall_Sensor, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(Hall_Sensor), doorChanged, CHANGE);
}

void doorChanged()
{
  if(digitalRead(Hall_Sensor) == 0)
    Serial.println("The door got closed");
  else
    Serial.println("The door got opened!");
}

void loop()
{}
