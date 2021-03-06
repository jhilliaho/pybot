from MotorDriver import MotorDriver
import time
import threading
from Utilities import *
import PID

# TODO
# IMU:lle oma thread missä lasketaan arvoja niin nopeaan kuin ehditään
# Lasketaan anturin asento gyron avulla
# Lasketaan pitch-arvon keskihajontaa ja resetoidaan gyron laskema arvo pitch-arvolla keskihajonnan ollessa tarpeeksi pieni
# Säädetään robotin asentoa PID-säätimellä gyrosta saatavan asentotiedon avulla

# Global Server variable
Server = None
Sensors = None

class sensorThread(threading.Thread):
	def run(self):
		print("Starting sensor thread")

		global Sensors
		import Sensors
		Sensors.collectData()

class serverThread(threading.Thread):
	def run(self):
		print("Starting server thread")

		global Server
		import Server
		Server.startServer()

class mainThread(threading.Thread):
	def run(self):
		print("Starting main thread")

		global Server

		sensors = Sensors()
		motors = MotorDriver()
		sensors.printAllSensorData()

		pitchCalibration = 0

		def calibrate():
			nonlocal pitchCalibration
			sum = 0
			for i in range(100):
				sum += sensors.getAccelerationData()['pitch']
			pitchCalibration = sum/100
			print("Pitch calibration: " + str(pitchCalibration))

		calibrate()

		controllerData = None
		
		# P I D
		print(PID)
		pid = PID.PID(1, 0, -0.001)
		pid.SetPoint = 0.0
		pid.setSampleTime(0.01)

		while True:
			controllerData = Server.controllerData

			pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
						
			try:
				ctrlx = controllerData['x1']
				ctrly = controllerData['y1']
			except KeyError:
				ctrlx = 0
				ctrly = 0

			ctrlx *= 10
			ctrly *= 10

			pid.update(pitch)

			#print(float2str(pid.output))

			speedValue = pid.output + ctrly
			speedValue *= 100

			motor1Speed = speedValue + ctrlx
			motor2Speed = speedValue - ctrlx


			if abs(motor1Speed) > 10 or abs(motor2Speed) > 10:
				motors.setSpeeds(motor1Speed, motor2Speed)

			print("PITCH: " + float2str(pitch) +
			      " CONTROL X: " + int2str(ctrlx) +
			      " CONTROL Y: " + int2str(ctrly) +
			      " MOTOR 1: " + float2str(motor1Speed) + 
			      " MOTOR 2: " + float2str(motor2Speed)
			)

sensorThread().start()
serverThread().start()
mainThread().start()
