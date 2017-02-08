from mpu6050 import mpu6050

import smbus

bus = smbus.SMBus(1)
address = 0x68

bus.write_byte_data(address, 0x00, 0x37)
bus.write_byte_data(address, 0x00, 0x02)
bus.write_byte_data(address, 0x00, 0x6A)
bus.write_byte_data(address, 0x00, 0x00)
bus.write_byte_data(address, 0x00, 0x6B)
bus.write_byte_data(address, 0x00, 0x00)
#bus.write_byte_data(address, [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00])

sensor = mpu6050(0x68)

while 1:
	#returns [accel, gyro, temp]. Accel and Gyro as {x, y, z} and temp as decimal
	data = sensor.get_all_data()
	
	print(data)
