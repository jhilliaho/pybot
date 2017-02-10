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
	pitch = int(400*pitch)
	#print("PITCH: " + str(pitch))
	#motors.setSpeeds(-pitch, -pitch)

	gyro = sensors.getGyroData()
	print(gyro)
