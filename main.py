from Sensors import Sensors
from MotorDriver import MotorDriver

import time

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

pitchCalibration = 0

def calibrate():
	sum = 0
	for i in range(100):
		sum += sensors.getAccelerationData()['pitch']
	pitchCalibration = sum/100
	print("Calibration: " + str(pitchCalibration))

calibrate()



while True:
	pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration

	print("PITCH: " + str(pitch))
	#if abs(pitch) > 20:
	#	motors.setSpeeds(-pitch, -pitch)
