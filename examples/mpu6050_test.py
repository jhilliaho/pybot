from mpu6050 import mpu6050

sensor = mpu6050(0x68)

while 1:
	data = sensor.get_accel_data()
	
	rounded = data
	
	rounded['x'] = round(rounded['x'], 2)
	rounded['y'] = round(rounded['y'], 2)
	rounded['z'] = round(rounded['z'], 2)
	
	print(rounded)
