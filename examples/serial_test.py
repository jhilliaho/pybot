import serial

#ser = serial.Serial('/dev/ttyUSB0')
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=0.1)  # open serial port

print(ser.name)         # check which port was really used


text = ''
while 1:
	line = ser.readline()
	print(line)

ser.close()