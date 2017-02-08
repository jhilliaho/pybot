# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050

class IMU:
	def __init__(self):
		self.sensor = mpu6050(0x68)

	def getAllData(self):
		data = self.sensor.get_all_data()
		self.acceleration = data[0]
		self.gyro = data[1]
		self.temperature = data[2]

	def getAccelerationData(self):
		self.getAllData()
		return self.acceleration

	def getGyroData(self):
		self.getAllData()
		return self.acceleration


if __name__ == "__main__":
	imu = IMU()
	print("Acceleration: ", imu.getAccelerationData())
	print("Gyroscopes: ", imu.getGyroData())

