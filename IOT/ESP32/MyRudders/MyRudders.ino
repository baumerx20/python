#include <Joystick.h>

Joystick_ Joystick;

int zAxis_ = 0; 
int RxAxis_ = 0;                    
int RyAxis_ = 0; 
int val_left = 0;
int val_right = 0;
int val_remap_left = 0;
int val_remap_right = 0;
int rudder = 0;

// A4 176 870
//A1 = Right Toe Brake  723 774    <769
//A2 = Rudder 383 569 844
//A3 = Left Toe Brake 592 496 <585

const bool initAutoSendState = true; 

void setup()
{
      Joystick.begin();
       Joystick.setXAxisRange(0, 1024); 
       Joystick.setYAxisRange(0, 1024);
       Joystick.setZAxisRange(0, 1024);
  }
   
void loop(){

 
zAxis_ = analogRead(A4);  
//zAxis_ = map(zAxis_,0,1024);
  if (zAxis_ >= 540)
  zAxis_ = 540;
  if (zAxis_ <= 0)
  zAxis_ = 0;
Joystick.setZAxis(zAxis_);  

RxAxis_ = analogRead(A3);
  if (RxAxis_ >=570)
  RxAxis_ = 570;
  if (RxAxis_ <=0)
  RxAxis_ = 0;
Joystick.setRxAxis(RxAxis_);
  
 RyAxis_ = analogRead(A2);
  if (RyAxis_ >=570)
  RyAxis_ = 570;
  if (RyAxis_ <=0)
  RyAxis_ = 0;
Joystick.setRyAxis(RyAxis_);   

//The 'If' functions are here to hard code a 'dead zone' into the toe brakes

}
