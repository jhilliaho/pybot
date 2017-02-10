from Sensors import Sensors
from MotorDriver import MotorDriver

import time

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

min = 0
max = 0

while True:
	acc = sensors.getAccelerationData()
	pitch = acc['pitch']
	pitch = int(40 * pitch) - 127
	if pitch < min:
		min = pitch
	if pitch > max:
		max = pitch
	print("PITCH: " + str(pitch) + " MIN: " + str(min) + " MAX: " + str(max))
	#motors.setSpeeds(-pitch, -pitch)
