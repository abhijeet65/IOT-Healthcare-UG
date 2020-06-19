import time
import serial

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import dht11_example 
import subprocess
import sos 
import moist
import buzzer


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



from firebase import firebase
firebase = firebase.FirebaseApplication('https://hospital-management-6a752.firebaseio.com/', None)


ser = serial.Serial('/dev/ttyACM0',9600)
# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

print("[info] heart beat ready")
def heartbeat():
    read_serial=ser.readline()
    print (read_serial[0:2]," BPM")
    bpm=read_serial[0:2]
    
    firebase.put("","bpm",str(bpm))
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    # Write two lines of text.
    draw.text((x+40, top+25),    str(bpm),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(3)
    disp.display()
    

def temp():
    count1=0
    res=""
    res1=""
    while True:
        result = instance.read()
        count1=count1+1
        if(count1>5):
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

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    firebase.put("","temp",res1)
    # Write two lines of text.
    draw.text((x+40, top+25),    str(res),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(3)
    disp.display()

def moisture():
    res=moist.main()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    firebase.put("","moist",res)

    res="moist "+str(res)
    # Write two lines of text.
    draw.text((x+40, top+25),    str(res),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(3)
    disp.display()


def sos1():
    res=sos.main()
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    firebase.put("","sos",res)

    res="sos"+str(res)
    # Write two lines of text.
    draw.text((x+40, top+25),    str(res),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(3)
    disp.display()



    
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)











while True:
    firebase.put("","bed",1)
    heartbeat()
    temp()
    moisture()
    sos1()
    

