from Compass import Compass
from IMU import IMU
from RangeFinder import RangeFinder

class Sensors:
	def __init__(self):
		self.compass = Compass()
		self.IMU = IMU()
		self.RangeFinder = RangeFinder()

	def updateSensorData(self):
		self.range = RangeFinder.getRange()
		self.direction = Compass.getDirection()
		self.orientation = IMU.getGyroData()
		self.acceleration = IMU.getAccelerationData()

	def printAllSensorData(self):
		self.updateSensorData()
		print("Range: ", self.range)
		print("Direction: ", self.direction)
		print("Orientation: ", self.orientation)
		print("Acceleration: ", self.acceleration)


if __name__ == "__main__":
	sensors = Sensors()
	sensors.printAllSensorData()
