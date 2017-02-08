from mpu6050 import mpu6050

sensor = mpu6050(0x68)

x = []
y = []
z = []

while 1:
	data = sensor.get_accel_data()
	x.extend(data.x)
	if len(x) > 10:
		x.pop(0)

	print(sum(x)/len(x))