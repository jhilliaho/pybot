from Sensors import Sensors
from MotorDriver import MotorDriver

import time

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

