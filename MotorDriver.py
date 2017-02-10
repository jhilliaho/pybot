
import smbus
import time
import math

class MotorDriver:
	def __init__(self):

		self.averageFrom = 10

		self.bus = smbus.SMBus(1)
		self.address = 0x8

	def setSpeeds(self, motor1Speed, motor2Speed):
		""" Give speeds between -32767 and 32767"""
		# 0 - 32767 = speed in forward
		# 32768 and 0 = stop
		# 32769 - 65535 = speed in backward
		# To reverse speed, just add 32768 to it
		
		if motor1Speed < -32767 or motor1Speed > 32767:
			motor1Speed = 0
		
		if motor2Speed < -32767 or motor2Speed > 32767:
			motor2Speed = 0

		if motor1Speed < 0:
			motor1Speed = (motor1Speed * -1) + 32768

		if motor2Speed < 0:
			motor2Speed = (motor2Speed * -1) + 32768 

		self.bus.write_word_data(8,1,motor1Speed)
		self.bus.write_word_data(8,2,motor2Speed)

if __name__ == "__main__":
	dr = MotorDriver()
	
	for i in range(0, 31):
		dr.setSpeeds(i*1000,i*1000)
		time.sleep(0.2)




