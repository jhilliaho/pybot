from mpu6050 import mpu6050

import smbus

bus = smbus.SMBus(1)
address = 0x68


DEVICE_ADDRESS = 0x68
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
ledout_values = [0x37, 0x02, 0x6A, 0x00, 0x6B, 0x00]
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)



sensor = mpu6050(0x68)

while 1:
	#returns [accel, gyro, temp]. Accel and Gyro as {x, y, z} and temp as decimal
	data = sensor.get_all_data()
	
	print(data)
