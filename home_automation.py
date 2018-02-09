# client side
import time
# import RPi.GPIO as GPIO
from RTk import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
def motor_control(direction):
#  print direction
  
  
  if (direction == "fwd"):
    GPIO.output(12, True)
    GPIO.output(13, False)
    GPIO.output(5, False)
    GPIO.output(6, False)

    print ("forward position led flow")

 
  if (direction == "bwd"):
   
    GPIO.output(13, True)
    GPIO.output(12, False)
    GPIO.output(5, False)
    GPIO.output(6, False)

    print ("backward position led flow")
   
  if (direction == "left"):     
    GPIO.output(5, True)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(6, False)

    print ("LEFT position led flow")
   
  if (direction == "right"):
    GPIO.output(6, True)
    GPIO.output(5, False)
    GPIO.output(12, False)
    GPIO.output(13, False)
    print ("RIGHT position led flow")
  if (direction == "stop"):
    GPIO.setmode(GPIO.BCM)
    GPIO.output(12, False)
    GPIO.output(13, False)
    GPIO.output(5, False)
    GPIO.output(6, False)


    print ("STOP position led flow")


  
