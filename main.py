from Sensors import Sensors
from MotorDriver import MotorDriver

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

while True:
	acc = sensors.getAccelerationData()
	pitch = acc['pitch']
	motors.setSpeeds(int(-10 * pitch), int(-10 * pitch))