import serial

RASPIPORT = '/dev/ttyUSB0'
MACPORT = '/dev/cu.usbserial-AM01TQUH'

class RangeFinder:
	def __init__(self):
		self.device = serial.Serial(port=RASPIPORT, baudrate=115200, timeout=0.1)

	def getRange(self):
		self.device.flush()
		while True:
			line = self.device.readline()
			try: 
				line = int(line)
				if line < 20:
					continue
				else:
					break
			except ValueError:
				continue
		return line

	def closeSerial(self):
		self.device.close()

if __name__ == "__main__":
	dev = RangeFinder()
	for i in range(50):
		print(dev.getRange())
	dev.closeSerial()
