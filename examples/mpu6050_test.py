from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while 1:
	data = sensor.get_accel_data()
	print(data['x'], data['y'], data['z'])
