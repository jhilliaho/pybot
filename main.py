from Sensors import Sensors
from MotorDriver import MotorDriver

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()

print("Alles gut")

while True:
	acc = sensors.getAccelerationData()
	pitch = acc['pitch']
	motors.setSpeeds(-10 * pitch, -10 * pitch)