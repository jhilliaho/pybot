from Sensors import Sensors
from MotorDriver import MotorDriver

import time

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

while True:
	acc = sensors.getAccelerationData()
	pitch = acc['pitch'] - 2.7
	pitch = int(pitch)
	print(pitch)
	#motors.setSpeeds(int(-10 * pitch), int(-10 * pitch))
