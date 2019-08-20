import RPi.GPIO as GPIO
import os
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# To read the state
state26 = GPIO.input(26)
state13 = GPIO.input(13)

if state26==1:
   os.system('mpc pause')
   GPIO.output(13, GPIO.HIGH)
   time.sleep(0.2)
   os.system('aplay /root/coaxial.wav')
   GPIO.output(26, GPIO.LOW)
   GPIO.output(13, GPIO.LOW)
   file = open("/boot/input","w")
   file.write("coax")
   file.close()

if state26==0 and state13==0:
   os.system('mpc pause')
   GPIO.output(13, GPIO.HIGH)
   time.sleep(0.2)
   os.system('aplay /root/streamer.wav')
   GPIO.output(26, GPIO.LOW)
   GPIO.output(13, GPIO.HIGH)
   file = open("/boot/input","w")
   file.write("streamer")
   file.close()

if state13==1:
   os.system('mpc pause')
   time.sleep(0.2)
   os.system('aplay /root/optical.wav')
   GPIO.output(26, GPIO.HIGH)
   GPIO.output(13, GPIO.LOW)
   file = open("/boot/input","w")
   file.write("opt")
   file.close()
