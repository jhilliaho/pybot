# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while 1:
	#returns [accel, gyro, temp]. Accel and Gyro as {x, y, z} and temp as decimal
	data = sensor.get_all_data()
	
	print(data)
	print("\n")
	print("\n")

class imu:
	def __init__(self):
		self.sensor = mpu6050(0x68)

	def getAllData(self):
		data = sensor.get_all_data()
		print(data)



