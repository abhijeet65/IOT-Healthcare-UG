import RPi.GPIO as GPIO
import time

sensor = 7 //rapberry-pi-pin-number
buzzer = 24

print("[info] moisture ready")

GPIO.setwarnings(False)

def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(sensor,GPIO.IN)
  GPIO.setup(buzzer,GPIO.OUT)

  GPIO.output(buzzer,False)
  if GPIO.input(sensor):
      GPIO.output(buzzer,True)
      print ("moisture Detected")
      time.sleep(1)
      GPIO.output(buzzer,False)
      res=1
      
  else:
      GPIO.output(buzzer,False)
      print("no moisture")
      res=0
  return res




