import serial

class RangeFinder:
	def __init__(self):
		self.device = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=0.1)

	def getRange(self):
		return int(self.device.readline())

	def closeSerial(self):
		self.device.close()


if __name__ == "__main__":
	dev = RangeFinder()
	print(dev.getRange())
	dev.closeSerial()
