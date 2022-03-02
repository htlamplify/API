 
 #A sketch that grabs the frequency signal level measured by the Mixed Signal
 #Integration MSGEQ7. This sketch is designed to work with the MSGEQ7 Breakout Board 
 #available at the Rheingold Heavy website.
 
 #This sketch expects the following pin assignments...
 #STROBE = DIGITAL 7
 #RESET  = DIGITAL 8
 #OUTPUT = ANALOG  5
 
 #Website:   https://rheingoldheavy.com/msgeq7-arduino-tutorial-01-getting-started
 #Datasheet: http://www.mix-sig.com/images/datasheets/MSGEQ7.pdf
 
import RPI.GPIO as GPIO
import time 

strobePin  = GPIO.setup(13, GPIO.OUT)   # Strobe Pin on the MSGEQ7
resetPin   = GPIO.setup(19, GPIO.OUT)   # Reset Pin on the MSGEQ7
level[7]          # An array to hold the values from the 7 frequency bands
audioSample = GPIO.setup(2, GPIO.IN) # Output Pin on the MSGEQ7

  #// Create an initial state for our pins
GPIO.output(19, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
sleep(0.001)

 
  #// Reset the MSGEQ7 as per the datasheet timing diagram
GPIO.output(19, GPIO.HIGH)
sleep(0.001)
GPIO.output(19, GPIO.LOW)
GPIO.output(13, GPIO.HIGH)
sleep(0.001)

 
while true:
  # Cycle through each frequency band by pulsing the strobe.
    for i in range(7):
        GPIO.output(13, GPIO.LOW)
        sleep(0.0001)                   # Delay necessary due to timing diagram
        level[i] = audioSample
        GPIO.output(13, GPIO.HIGH)
        sleep(0.0001)                   # Delay necessary due to timing diagram  
    
    for i in range(7):
        Value(level[i]) 
        