from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while 1:
	#returns [accel, gyro, temp]. Accel and Gyro as {x, y, z} and temp as decimal
	data = sensor.get_all_data()
	
	print(data)
