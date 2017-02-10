from Sensors import sensors
from MotorDriver import MotorDriver

sensors = Sensors()
motors = MotorDriver()

sensors.printAllSensorData()
motors.setSpeeds(1000,1000)

print("Alles gut")