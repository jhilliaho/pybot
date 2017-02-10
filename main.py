from Sensors import Sensors
from MotorDriver import MotorDriver

import time

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

#while True:
for i in range(50):
	acc = sensors.getAccelerationData()
	sensors.IMU.averageFrom *= 2

for i in range(50):
	acc = sensors.getAccelerationData()
	sensors.IMU.averageFrom *= 2

for i in range(50):
	acc = sensors.getAccelerationData()
	sensors.IMU.averageFrom *= 2

for i in range(50):
	acc = sensors.getAccelerationData()
	sensors.IMU.averageFrom *= 2





	#pitch = acc['pitch']
	#pitch = int(400 * pitch)
	#print("PITCH: " + str(pitch))
	#motors.setSpeeds(-pitch, -pitch)
