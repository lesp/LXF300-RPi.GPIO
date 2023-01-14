import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
LED = 17
delay = 1
GPIO.setup(LED, GPIO.OUT)

for i in range(10):
    GPIO.output(LED,GPIO.HIGH)
    print("LED ON")
    sleep(delay)
    GPIO.output(LED,GPIO.LOW)
    print("LED OFF")
    sleep(delay)

GPIO.cleanup()
