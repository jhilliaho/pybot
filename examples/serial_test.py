import serial

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=0.1)  # open serial port
#ser = serial.Serial(port='/dev/cu.usbserial-AM01TQUH', baudrate=115200, timeout=0.1)  # open serial port

print(ser.name)         # check which port was really used


text = ''
while 1:
	line = ser.readline()
	line = lstrip(rstrip(line))
	print(line)

ser.close()