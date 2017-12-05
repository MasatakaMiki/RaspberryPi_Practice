import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) #PIR motion sensor
GPIO.setup(3, GPIO.OUT) #LED output pin
while True:
    i = GPIO.input(11)
    if i == 0:
        print "No intruders", i
        GPIO.output(3, 0) #turn off led
        time.sleep(1)
    elif i == 1:
        print "Intruder detected", i
        GPIO.output(3, 1) #turn on led
        time.sleep(1)
        
