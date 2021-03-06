import smbus
import time
import math

class Compass:
	def __init__(self):

		self.averageFrom = 4

		self.bus = smbus.SMBus(1)
		self.address = 0x1e

		time.sleep(0.1)
		self.write_byte(0, 0b01111000) # Set to 8 samples @ 75Hz
		self.write_byte(1, 0b00100000) # 1.3 gain LSb / Gauss 1090 (default)
		self.write_byte(2, 0b00000000) # Continuous sampling
		self.scale = 0.92

		self.bearing = []

	def read_byte(self, adr):
	    return self.bus.read_byte_data(address, adr)

	def read_word(self, adr):
	    high = self.bus.read_byte_data(self.address, adr)
	    low = self.bus.read_byte_data(self.address, adr+1)
	    val = (high << 8) + low
	    return val

	def read_word_2c(self, adr):
	    val = self.read_word(adr)
	    if (val >= 0x8000):
	        return -((65535 - val) + 1)
	    else:
	        return val

	def write_byte(self, adr, value):
		"Write a single byte via I2C"
		self.bus.write_byte_data(self.address, adr, value)

	def getDirection(self):
		"Get current compass bearing"
		x_out = self.read_word_2c(3) * self.scale
		y_out = self.read_word_2c(7) * self.scale
		z_out = self.read_word_2c(5) * self.scale

		bearing  = math.atan2(y_out, x_out) 
		if (bearing < 0):
		    bearing += 2 * math.pi

		self.bearing.append(bearing)
		
		if len(self.bearing) > self.averageFrom:
		 	self.bearing.pop(0)

		avgBearing = sum(self.bearing)/len(self.bearing)

		return round(math.degrees(avgBearing), 2)


if __name__ == "__main__":
	com = Compass()
	print(com.getDirection())
