from IMU import IMU
from Compass import Compass
#from RangeFinder import RangeFinder

class Sensors:
	def __init__(self):
		self.Compass = Compass()
		self.IMU = IMU()
		#self.RangeFinder = RangeFinder()

	def updateSensorData(self):
		#self.range = self.RangeFinder.getRange()
		self.compassBearing = self.Compass.getDirection()
		self.gyro = self.IMU.getGyroData()
		self.acceleration = self.IMU.getAccelerationData()

	def printAllSensorData(self):
		self.updateSensorData()
		
		#print("Range: ", self.range)
		print("compassBearing: ", self.compassBearing)
		print("Roll: ", self.acceleration['roll'])
		print("Pitch: ", self.acceleration['pitch'])

	def getAccelerationData(self):
		self.updateSensorData()
		return self.acceleration

	def getGyroData(self):
		self.updateSensorData()
		return self.gyro

	def getCompassBearing(self):
		self.updateSensorData()
		return self.compassBearing

if __name__ == "__main__":
	sensors = Sensors()
	while True:
		sensors.printAllSensorData()
