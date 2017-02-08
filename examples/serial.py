import serial

ser = serial.Serial('/dev/ttyUSB0')  # open serial port

print(ser.name)         # check which port was really used

a = ser.read()     # write a string

print(a)

ser.close()             # close port