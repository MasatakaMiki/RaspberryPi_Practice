# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep

# read 12bit digital value from MCP3208 by SPI
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum > 7 or adcnum < 0:
        return -1
    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)

    commandout = adcnum
    commandout |= 0x18 # start-bit + single-end-bit
    commandout <<= 3 # send 8th bit from LSB
    for i in range(5):
        # send between 8th bit and 4th bit from LSB
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0

    # read 13bit (null + 12bit data)
    for i in range(13):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i > 0 and GPIO.input(misopin) == GPIO.HIGH:
            adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout

GPIO.setmode(GPIO.BCM)

LED = 25
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

try:
    while True:
        inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
        print(inputVal0)
        if inputVal0 < 300:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
        sleep(0.2)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
