from Sensors import Sensors
from MotorDriver import MotorDriver

import time
import threading

# Global Server variable
Server = None

class serverThread(threading.Thread): #I don't understand this or the next line
	def run(self):
		print("Server thread running")
		global Server
		import Server
		Server.startServer()

class mainThread(threading.Thread):
	def run(self):
		global Server

		sensors = Sensors()
		motors = MotorDriver()
		sensors.printAllSensorData()

		pitchCalibration = 0

		def calibrate():
			global pitchCalibration
			sum = 0
			for i in range(100):
				sum += sensors.getAccelerationData()['pitch']
			pitchCalibration = sum/100
			print("Calibration: " + str(pitchCalibration))

		calibrate()

		controllerData = None

		while True:
			controllerData = Server.controllerData

			pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
			if pitch < 0:
				pitchstr = "{:.3f}".format(pitch) 
			else:
				pitchstr = " {:.3f}".format(pitch) 		
			print("PITCH: " + pitchstr)
			print("MAIN CONTROLLER: " + str(controllerData))

			if abs(pitch) > 0.3:
				motors.setSpeeds(-20 * pitch, -20 * pitch)



serverThread().start()
mainThread().start()
