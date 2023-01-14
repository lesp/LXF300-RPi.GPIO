import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
LED = 17
button = 27
delay = 0.1
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
LED_state = 0
try:
    while True:
        if GPIO.input(button) == GPIO.LOW and LED_state == 0:
            LED_state = 1
            GPIO.output(LED,GPIO.HIGH)
            print("LED ON")
            sleep(delay)
        elif GPIO.input(button) == GPIO.LOW and LED_state == 1:
            LED_state = 0
            GPIO.output(LED,GPIO.LOW)
            print("LED OFF")
            sleep(delay)
        sleep(delay)
except KeyboardInterrupt:
    GPIO.cleanup()
