from Sensors import Sensors
from MotorDriver import MotorDriver

import time
import threading





# Global Server variable
Server = None

class threadOne(threading.Thread): #I don't understand this or the next line
	def run(self):
		print("Server thread running")
		global Server
		import Server
		Server.startServer()

class threadTwo(threading.Thread):
	def run(self):
		print("Main thread running")

		global Server

		sensors = Sensors()
		motors = MotorDriver()
		sensors.printAllSensorData()
		print("Alles gut")

		pitchCalibration = 0


		def calibrate():
			global pitchCalibration
			sum = 0
			for i in range(100):
				sum += sensors.getAccelerationData()['pitch']
			pitchCalibration = sum/100



		calibrate()
		print("Calibration: " + str(pitchCalibration))


		while True:
			try:
				controllerData = Server.controllerData
			except Exception:
				print("Server not ready")
				print(Server)
				time.sleep(0.5)
				continue

			pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
			if pitch < 0:
				pitchstr = "{:.3f}".format(pitch) 
			else:
				pitchstr = " {:.3f}".format(pitch) 		
			print("PITCH: " + pitchstr)
			print("CONTROLLER: " + Server.controllerData)
			if abs(pitch) > 0.3:
				motors.setSpeeds(-20 * pitch, -20 * pitch)



threadTwo().start()
threadOne().start()
