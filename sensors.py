from Compass import Compass
from IMU import IMU
from RangeFinder import RangeFinder

class Sensors:
	def __init__(self):
		self.Compass = Compass()
		self.IMU = IMU()
		self.RangeFinder = RangeFinder()

	def updateSensorData(self):
		self.range = self.RangeFinder.getRange()
		self.direction = self.Compass.getDirection()
		self.orientation = self.IMU.getGyroData()
		self.acceleration = self.IMU.getAccelerationData()

	def printAllSensorData(self):
		self.updateSensorData()
		print("Range: ", self.range)
		print("Direction: ", self.direction)
		print("Orientation: ", self.orientation)
		print("Acceleration: ", self.acceleration)


if __name__ == "__main__":
	sensors = Sensors()
	sensors.printAllSensorData()
