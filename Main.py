from Sensors import Sensors
from MotorDriver import MotorDriver
import time
import threading

# Global Server variable
Server = None

class serverThread(threading.Thread): #I don't understand this or the next line
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

		while True:
			controllerData = Server.controllerData

			pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
			
			if pitch < 0:
				pitchstr = "{:.3f}".format(pitch) 
			else:
				pitchstr = " {:.3f}".format(pitch) 		
			
			try:
				ctrlx = controllerData['x1']
				ctrly = controllerData['y1']
			except KeyError:
				ctrlx = 0
				ctrly = 0

			print("PITCH: " + pitchstr + " CONTROL DATA:  x: " + str(ctrlx) + " y: " + str(ctrly))

			speedValue = -20 * pitch + ctrly/10

			motor1Speed = speedValue + ctrlx
			motor2Speed = speedValue - ctrlx

			if abs(motor1Speed) > 0.3 or abs(motor2Speed) > 0.3:
				motors.setSpeeds(motor1Speed, motor2Speed)
				print("SPEEDS: ", str(motor1Speed), " ", str(motor2Speed))


serverThread().start()
mainThread().start()
