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
	#pitch = int(pitch)
	print("PITCH: " + str(pitch))
	#motors.setSpeeds(-pitch, -pitch)

	#gyro = sensors.getGyroData()
	#print("x: " + str(round(gyro['x'], 3)) + "y: " + str(round(gyro['y'], 3)) + "z: " + str(round(gyro['z'], 3))) 
	motors.setSpeeds(100, 100)
