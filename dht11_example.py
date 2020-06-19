import RPi.GPIO as GPIO
import dht11
import time
import datetime


print("[info] temeprature ready")

GPIO.setmode(GPIO.BCM)
count1=0
# read data using pin 14
instance = dht11.DHT11(pin=18)
GPIO.setwarnings(False)
def main():
    count1=0
    res=""
    res1=""
    while True:
        result = instance.read()
        count1=count1+1
        if(count1>10):
            break
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            
            temp=int(result.temperature)
            temp=temp+4
           #print("Temperature: %-3.1f C" % temp)
           
            print("Body Temperature: %d F" % (((result.temperature) * 9/5) +39)) 
            #print("Humidity: %-3.1f %%" % result.humidity)
            res="temp :"+str(int((result.temperature) * 9/5) +39)
            res1=str(int((result.temperature) * 9/5) +39)

        time.sleep(0.5)
        return res,res1
            
main()
