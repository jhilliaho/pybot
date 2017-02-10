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
	pitch = int(400 * pitch) - 1270
	print("PITCH: " + str(pitch))
	#motors.setSpeeds(-pitch, -pitch)
