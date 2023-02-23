import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(4, GPIO.IN)

try:
    while True:
        pin_value = GPIO.input(4)
        print(pin_value) 
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanip()
