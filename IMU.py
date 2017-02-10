# https://github.com/Tijndagamer/mpu6050
# pip install mpu6050-raspberrypi
# Fixed self.-bug in get_all_data
from mpu6050 import mpu6050
import math
import statistics
import smbus

class IMU:
	def __init__(self):
		self.averageFrom = 10

		self.sensor = mpu6050(0x68)
		
		self.acceleration = {'x': [], 'y': [], 'z': [], 'roll': [], 'pitch': []}
		self.gyro = {'x': 0, 'y': 0, 'z': 0}
		self.dataCount = 0

		# IMU Settings from MPU6050 register map:
		self.bus = smbus.SMBus(1)
		
		addr = 0x68
		
		# Register 106 - User control
		self.bus.write_byte_data(addr, 0x6A, 0x00)
		
		# Register 107 - Power management 1
		self.bus.write_byte_data(addr, 0x6B, 0x00)
		
		# Register 55 – INT Pin / Bypass Enable Configuration
		self.bus.write_byte_data(addr, 0x37, 0x02)

		# Digital Low Pass Filter (DLPF) in MPU6050 Register 26 (0x1A)
		# Accelerometer values from vibrating sensor with different settings:
		# 1: Min: -20.1 Max: 78.89 Mean: 7.52 Std: 20.34
		# 2: Min: -10.5 Max: 20.88 Mean: 3.02 Std: 7.6
		# 3: Min: -2.85 Max: 12.09 Mean: 2.54 Std: 3.01
		# 4: Min: -0.63 Max: 5.43  Mean: 2.37 Std: 1.53
		# 5: Min:  0.85 Max: 3.83  Mean: 2.5  Std: 0.8
		# 6: Min:  1.7  Max: 3.47  Mean: 2.51 Std: 0.49
		# Decided to use value 6. It Should remove frequencies below 5Hz
		self.bus.write_byte_data(addr, 0x1A, 0x06)


	def calculateAllData(self):
		data = self.sensor.get_all_data()

		self.acceleration['x'].append(data[0]['x'])
		self.acceleration['y'].append(data[0]['y'])
		self.acceleration['z'].append(data[0]['z'])

		self.gyro = data[1]

		self.acceleration['roll'].append(self.calculateRoll(self.acceleration['y'][-1],self.acceleration['z'][-1]))
		self.acceleration['pitch'].append(self.calculatePitch(self.acceleration['x'][-1],self.acceleration['y'][-1],self.acceleration['z'][-1]))

		self.dataCount += 1

		if self.dataCount > self.averageFrom:
			self.acceleration['x'].pop(0)
			self.acceleration['y'].pop(0)
			self.acceleration['z'].pop(0)

			self.acceleration['pitch'].pop(0)
			self.acceleration['roll'].pop(0)

	def calcAvg(self,L):
		return round(sum(L)/len(L),3)

	def getAccelerationData(self):
		self.calculateAllData()
		acceleration = {
			'x': self.calcAvg(self.acceleration['x']),
			'y': self.calcAvg(self.acceleration['y']),
			'z': self.calcAvg(self.acceleration['z']),
			'roll': self.calcAvg(self.acceleration['roll']),
			'pitch': self.calcAvg(self.acceleration['pitch'])
		}
		
		# Used for calculating basic statistics from accelerometer data
		pitch = self.acceleration['pitch']
		#pmin = str(round(min(pitch),2))
		#pmax = str(round(max(pitch),2))
		print(str(round(statistics.stdev(pitch),2)))
		#pmean = str(round(self.calcAvg(pitch),2))
		#print("Min: " + pmin + " Max: " + pmax + " Mean: " + pmean + " Std: " + pstd)

		return acceleration

	def getGyroData(self):
		self.calculateAllData()
		gyro = {
			'x': self.gyro['x'],
			'y': self.gyro['y'],
			'z': self.gyro['z']
		}
		return gyro

	def calculateRoll(self,y,z):
		return math.atan2(y, z) * 180/math.pi;

	def calculatePitch(self,x,y,z):
		return math.atan2(-x, math.sqrt(y*y + z*z)) * 180/math.pi;

if __name__ == "__main__":
	imu = IMU()
	print("Acceleration: ", imu.getAccelerationData())
	print("Gyroscopes: ", imu.getGyroData())

