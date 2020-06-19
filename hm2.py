import serial

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	read_serial=ser.readline()
	print (read_serial[0:2]," BPM")
	bpm=read_serial[0:2]
