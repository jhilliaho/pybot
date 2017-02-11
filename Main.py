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

		def fl2str(fl):
			if fl < 0:
				flstr = "{:.3f}".format(fl) 
			else:
				flstr = " {:.3f}".format(fl)
			return flstr

		while True:
			controllerData = Server.controllerData

			pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
						
			try:
				ctrlx = controllerData['x1']
				ctrly = controllerData['y1']
			except KeyError:
				ctrlx = 0
				ctrly = 0


			speedValue = -60 * pitch + ctrly/2

			motor1Speed = speedValue + ctrlx/4
			motor2Speed = speedValue - ctrlx/4


			if abs(motor1Speed) > 5 or abs(motor2Speed) > 5:
				motors.setSpeeds(motor1Speed, motor2Speed)






			print("PITCH: " + fl2str(pitch) + " CONTROL DATA:  x: " + str(ctrlx) + " y: " + str(ctrly))
			print("SPEEDS: ", fl2str(motor1Speed), " ", fl2str(motor2Speed))


serverThread().start()
mainThread().start()
