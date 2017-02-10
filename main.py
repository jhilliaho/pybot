from Sensors import Sensors
from MotorDriver import MotorDriver

import time

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")


while True:
	acc = sensors.getAccelerationData()
	pitch = acc['pitch']
	pitch = int(40 * pitch) - 127

	print("PITCH: " + str(pitch))
	if abs(pitch) > 5
		motors.setSpeeds(-pitch, -pitch)
