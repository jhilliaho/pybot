from mpu6050 import mpu6050
import math
import statistics
import threading
import smbus
import time

class IMU:
	def __init__(self):
		addr = 0x68
		self.bus = smbus.SMBus(1)
		self.bus.write_byte_data(addr, 0x6A, 0x00)	# Register 106 - User control
		self.bus.write_byte_data(addr, 0x6B, 0x00)	# Register 107 - Power management 1
		self.bus.write_byte_data(addr, 0x37, 0x02)	# Register 55  – INT Pin / Bypass Enable Configuration
		self.bus.write_byte_data(addr, 0x1A, 0x06)	# Register 26  - Digital Low Pass Filter below 5Hz
		self.sensor = mpu6050(addr)

		self.acceleration = {'x': 0, 'y': 0, 'z': 0, 'roll': 0, 'pitch': 0}
		self.gyro = {'x': 0, 'y': 0, 'z': 0}

		self.gyroDistance = {'x': 0, 'y': 0, 'z': 0}

		self.dataTime = 0
		self.lastTime = 0

	def getAllData(self):
		data = self.sensor.get_all_data()
		self.acceleration = data[0]
		self.acceleration['roll'] = self.calculateRoll(self.acceleration['y'][-1],self.acceleration['z'][-1])
		self.acceleration['pitch'] = self.calculatePitch(self.acceleration['x'][-1],self.acceleration['y'][-1],self.acceleration['z'][-1])
		self.gyro = data[1]

		timeNow = time.time()
		self.dataTime = timeNow - self.lastTime
		self.lastTime = timeNow

		self.gyroDistance['x'] += (self.dataTime * self.gyro['x'])
		self.gyroDistance['y'] += (self.dataTime * self.gyro['y'])
		self.gyroDistance['z'] += (self.dataTime * self.gyro['z'])

	def calcAvg(self,L):
		return round(sum(L)/len(L),3)

	def calculateRoll(self,y,z):
		return math.atan2(y, z) * 180/math.pi;

	def calculatePitch(self,x,y,z):
		return math.atan2(-x, math.sqrt(y*y + z*z)) * 180/math.pi;

if __name__ == "__main__":
	imu = IMU()

	while True:
		imu.getAllData()
		print(self.gyroDistance)

