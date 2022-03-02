from smbus2 import SMBus
import RPI.GPIO as GPIO
import time 

class EQ:
    def __init__(self, strobe, reset, addr, reg):
        strobePin  = strobe
        GPIO.setup(strobePin, GPIO.OUT)   # Strobe Pin on the MSGEQ7
        resetPin   = reset
        GPIO.setup(resetPin, GPIO.OUT)   # Reset Pin on the MSGEQ7
        value[7]          # An array to hold the values from the 7 frequency bands

        i2c_addr = addr
        audioSample = SMBus(1).read_byte_data(i2c_addr, reg) # Output of the MSGEQ7

        #// Create an initial state for our pins
        GPIO.output(resetPin, GPIO.LOW)
        GPIO.output(strobePin, GPIO.LOW)
        sleep(0.001)

        
        #// Reset the MSGEQ7 as per the datasheet timing diagram
        GPIO.output(resetPin, GPIO.HIGH)
        sleep(0.001)
        GPIO.output(resetPin, GPIO.LOW)
        GPIO.output(strobePin, GPIO.HIGH)
        sleep(0.001)

        
    while true:
    # Cycle through each frequency band by pulsing the strobe.
        for i in range(7):
            GPIO.output(strobePin, GPIO.LOW)
            sleep(0.0001)                   # Delay necessary due to timing diagram
            value[i] = audioSample
            GPIO.output(strobePin, GPIO.HIGH)
            sleep(0.0001)                   # Delay necessary due to timing diagram  
        
        for i in range(7):
            value[i]
                