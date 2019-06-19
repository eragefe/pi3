import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(31,GPIO.OUT)
GPIO.output(31,GPIO.HIGH)
time.sleep(0.3)
GPIO.output(31,GPIO.LOW)
