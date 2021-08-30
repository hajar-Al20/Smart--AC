import Adafruit_DHT
import RPi.GPIO as GPIO 
from time import sleep

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set relay pins as output
GPIO.setup(27, GPIO.OUT)

# read data using pin 10
def getSensorData():
     Temp, Humi = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11,4)
     return (Temp, Humi)
                        
print("starting now....")
while True:
     H,T = getSensorData()
     print(f"Tempretuer : {T}")
     print(f"Humi : {H}")

     relay = T
     if relay >= 25:
         GPIO.output(27, GPIO.LOW)
         print("AC is oN")

     #turn GPIO pin 21 on
     elif relay < 25:
         GPIO.output(27, GPIO.HIGH) #Turn GPIO pin 21 off
         print("AC is oFF")

time.sleep(2)
