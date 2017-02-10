# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050
import math

class IMU:
	def __init__(self):
		self.sensor = mpu6050(0x68)

	def getAllData(self):
		data = self.sensor.get_all_data()
		self.acceleration = data[0]
		self.gyro = data[1]
		self.temperature = data[2]

		x = self.acceleration['x']
		y = self.acceleration['y']
		z = self.acceleration['z']

		self.acceleration['roll'] = math.atan2(y, z) * 180/math.pi;
		self.acceleration.['pitch'] = math.atan2(-x, sqrt(y*y + z*z)) * 180/math.pi;

	def getAccelerationData(self):
		self.getAllData()
		return self.acceleration

	def getGyroData(self):
		self.getAllData()
		return self.gyro


if __name__ == "__main__":
	imu = IMU()
	print("Acceleration: ", imu.getAccelerationData())
	print("Gyroscopes: ", imu.getGyroData())

