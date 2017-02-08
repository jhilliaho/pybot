#!/usr/bin/python
#

import smbus
import time
import math

bus = smbus.SMBus(1)
address = 0x1e

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def write_byte(adr, value):
    bus.write_byte_data(address, adr, value)

def openGY87():
	DEVICE_ADDRESS = 0x68
	DEVICE_REG_MODE1 = 0x00
	DEVICE_REG_LEDOUT0 = 0x1d

	ledout_values = [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00]
	bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)

openGY87();

write_byte(0, 0b01110000) # Set to 8 samples @ 15Hz
write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
write_byte(2, 0b00000000) # Continuous sampling

scale = 0.92

while True:

	x_out = read_word_2c(3) * scale
	y_out = read_word_2c(7) * scale
	z_out = read_word_2c(5) * scale

	bearing  = math.atan2(y_out, x_out) 
	if (bearing < 0):
	    bearing += 2 * math.pi

	print ("Bearing: ", math.degrees(bearing))
	time.sleep(0.1)