from Sensors import Sensors
from MotorDriver import MotorDriver

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()
motors.setSpeeds(1000,1000)

print("Alles gut")