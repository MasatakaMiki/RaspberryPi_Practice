# -*- coding: utf-8 -*-
#tmp102
#sen-11931
#
#I2C device
#vcc - 3.3v
#gnd - gnd
#sda - i2c sda
#scl - i2c scl
#alt - 
#add0 -
#
import smbus
from time import sleep

def read_temp():
    word_data = bus.read_word_data(address_tmp102, register_tmp102)
    data = (word_data & 0xff00)>>8 | (word_data & 0xff)<<8
    data = data>>4 # 12bit
    if data & 0x800 == 0:
        # plus
        temperature = data * 0.0625
    else:
        # minus
        temperature = ((~data&0xfff) + 1) * -0.0625
    return temperature

bus = smbus.SMBus(1)
address_tmp102 = 0x48
register_tmp102 = 0x00

try:
    while True:
        inputValue = read_temp()
        print(inputValue)
        sleep(1)
except KeyboardInterrupt:
    pass
