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



while True:
	pitch = sensors.getAccelerationData()['pitch'] - pitchCalibration
	if pitch < 0:
		pitchstr = "{:.3f}".format(pitch) 
	else
		pitchstr = " {:.3f}".format(pitch) 		
	print("PITCH: " + pitchstr)
	if abs(pitch) > 0.3:
		motors.setSpeeds(-20 * pitch, -20 * pitch)
