import RPi.GPIO as GPIO
import time

print("[info] buzzer ready")
buzzer = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
GPIO.setwarnings(False)


def main():
  
      GPIO.output(buzzer,True)
      time.sleep(2)
      print("buzzer")
      GPIO.output(buzzer,False)

#main()
