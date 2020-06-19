import RPi.GPIO as GPIO
import time

sensor = 23
buzzer = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print ("[info] sos ready.....")
GPIO.setwarnings(False)


def main():

  time.sleep(1)
  if GPIO.input(sensor):
      GPIO.output(buzzer,True)
      print ("SOS Detected")
      time.sleep(1)
      GPIO.output(buzzer,False)
      res=1
      
  else:
      GPIO.output(buzzer,False)
      print("no sos")
      res=0
  return res

#main()


