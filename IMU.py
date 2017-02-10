# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050
import math

class IMU:
	def __init__(self):
		self.averageFrom = 10

		self.sensor = mpu6050(0x68)
		
		self.acceleration = {'x': [], 'y': [], 'z': [], 'roll': [], 'pitch': []}
		self.gyro = {'x': 0, 'y': 0, 'z': 0}
		self.dataCount = 0

	def calculateAllData(self):
		data = self.sensor.get_all_data()

		self.acceleration['x'].append(data[0]['x'])
		self.acceleration['y'].append(data[0]['y'])
		self.acceleration['z'].append(data[0]['z'])

		self.gyro = data[1]

		self.acceleration['roll'].append(self.calculateRoll(self.acceleration['y'][-1],self.acceleration['z'][-1]))
		self.acceleration['pitch'].append(self.calculatePitch(self.acceleration['x'][-1],self.acceleration['y'][-1],self.acceleration['z'][-1]))

		self.dataCount += 1

		if self.dataCount > self.averageFrom:
			self.acceleration['x'].pop(0)
			self.acceleration['y'].pop(0)
			self.acceleration['z'].pop(0)

			self.acceleration['pitch'].pop(0)
			self.acceleration['roll'].pop(0)

	def calcAvg(self,L):
		return round(sum(L)/len(L),3)

	def getAccelerationData(self):
		self.calculateAllData()
		acceleration = {
			'x': self.calcAvg(self.acceleration['x']),
			'y': self.calcAvg(self.acceleration['y']),
			'z': self.calcAvg(self.acceleration['z']),
			'roll': self.calcAvg(self.acceleration['roll']),
			'pitch': self.calcAvg(self.acceleration['pitch'])
		}
		return acceleration

	def getGyroData(self):
		self.calculateAllData()
		gyro = {
			'x': self.gyro['x'],
			'y': self.gyro['y'],
			'z': self.gyro['z']
		}
		return gyro

	def calculateRoll(self,y,z):
		return math.atan2(y, z) * 180/math.pi;

	def calculatePitch(self,x,y,z):
		return math.atan2(-x, math.sqrt(y*y + z*z)) * 180/math.pi;

if __name__ == "__main__":
	imu = IMU()
	print("Acceleration: ", imu.getAccelerationData())
	print("Gyroscopes: ", imu.getGyroData())

