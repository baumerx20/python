int led = 13 ; // LED on arduino
int digitalPin = 0; // linear Hall magnetic sensor digital interface
   //////////////////////////////////////////////
  //        HALL EFFECT SENSOR DEMO           //
 //                                          //
//           http://www.educ8s.tv           //
/////////////////////////////////////////////

int hallSensorPin = A1;     
int ledPin =  A2;    
int state = 0;          

void setup() {
  pinMode(ledPin, OUTPUT);      
  pinMode(hallSensorPin, INPUT);     
}

void loop(){
  
  state = digitalRead(hallSensorPin);

  if (state == LOW) {        
    digitalWrite(ledPin, HIGH);  
  } 
  else {
    digitalWrite(ledPin, LOW); 
  }
}
