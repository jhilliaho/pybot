# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050
import math
import numpy

class IMU:
	def __init__(self):
		self.averageFrom = 16

		self.sensor = mpu6050(0x68)
		
		self.acceleration = {'x': [], 'y': [], 'z': [], 'roll': [], 'pitch': []}
		self.gyro = {'x': [], 'y': [], 'z': []}
		self.dataCount = 0

	def calculateAllData(self):
		data = self.sensor.get_all_data()

		self.acceleration['x'].append(data[0]['x'])
		self.acceleration['y'].append(data[0]['y'])
		self.acceleration['z'].append(data[0]['z'])

		self.gyro['x'].append(data[1]['x'])
		self.gyro['y'].append(data[1]['y'])
		self.gyro['z'].append(data[1]['z'])

		self.temperature.append(data[2])

		self.acceleration['roll'].append(self.calculateRoll(self.acceleration['y'],self.acceleration['z']))
		self.acceleration['pitch'].append(self.calculatePitch(self.acceleration['x'],self.acceleration['y'],self.acceleration['z']))

		dataCount += 1

		if dataCount > averageFrom:
			self.acceleration['x'].pop(0)
			self.acceleration['y'].pop(0)
			self.acceleration['z'].pop(0)

			self.gyro['x'].pop(0)
			self.gyro['y'].pop(0)
			self.gyro['z'].pop(0)

			self.temperature.pop(0)

			self.acceleration['pitch'].pop(0)
			self.acceleration['roll'].pop(0)

	def getAccelerationData(self):
		self.calculateAllData()
		acceleration = {'x': numpy.mean(self.acceleration['x']), 'y': numpy.mean(self.acceleration['y']), 'z': numpy.mean(self.acceleration['z']), 'roll': numpy.mean(self.acceleration['roll']), 'pitch': numpy.mean(self.acceleration['pitch'])}
		return acceleration

	def getGyroData(self):
		self.calculateAllData()
		gyro = {'x': numpy.mean(self.gyro['x']), 'y': numpy.mean(self.gyro['y']), 'z': numpy.mean(self.gyro['z'])}
		return gyro

	def calculateRoll(y,z):
		return math.atan2(y, z) * 180/math.pi;

	def calculatePitch(x,y,z):
		return math.atan2(-x, math.sqrt(y*y + z*z)) * 180/math.pi;

if __name__ == "__main__":
	imu = IMU()
	print("Acceleration: ", imu.getAccelerationData())
	print("Gyroscopes: ", imu.getGyroData())

