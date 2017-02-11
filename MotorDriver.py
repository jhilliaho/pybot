import smbus
import time
import math

LARGEST_MOTOR_SPEED_CHANGE = 2500

class MotorDriver:
	def __init__(self):

		self.averageFrom = 10

		self.bus = smbus.SMBus(1)
		self.address = 0x8

		self.motor1LastSpeed = 0
		self.motor2LastSpeed = 0

	def stopMotors(self):
		self.bus.write_word_data(8,1,0)
		self.bus.write_word_data(8,2,0)

	def setSpeeds(self, motor1Speed, motor2Speed):
		""" Give speeds between -32767 and 32767"""
		# 0 - 32767 = speed in forward
		# 32768 and 0 = stop
		# 32769 - 65535 = speed in backward
		# To reverse speed, just add 32768 to it

		motor1Speed = int(motor1Speed)
		motor2Speed = int(motor2Speed)
		
		if motor1Speed == 0 and motor2Speed == 0:
			self.stopMotors()
			return


		if motor1Speed > self.motor1LastSpeed + LARGEST_MOTOR_SPEED_CHANGE:
			motor1Speed = self.motor1LastSpeed + LARGEST_MOTOR_SPEED_CHANGE

		if motor1Speed < self.motor1LastSpeed - LARGEST_MOTOR_SPEED_CHANGE:
			motor1Speed = self.motor1LastSpeed - LARGEST_MOTOR_SPEED_CHANGE
		
		if motor2Speed > self.motor2LastSpeed + LARGEST_MOTOR_SPEED_CHANGE:
			motor2Speed = self.motor2LastSpeed + LARGEST_MOTOR_SPEED_CHANGE

		if motor2Speed < self.motor2LastSpeed - LARGEST_MOTOR_SPEED_CHANGE:
			motor2Speed = self.motor2LastSpeed - LARGEST_MOTOR_SPEED_CHANGE

		self.motor1LastSpeed = motor1Speed
		self.motor2LastSpeed = motor2Speed

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
	dr.setSpeeds(100,100)




