import RPi.GPIO as GPIO
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

eth = os.popen('ip addr show eth0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
wlan = os.popen('ip addr show wlan0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()

if eth != "":
   GPIO.output(13, GPIO.HIGH)
   GPIO.output(26, GPIO.LOW)
   os.system('aplay /root/ethernet.wav')

if wlan != "":
   GPIO.output(13, GPIO.HIGH)
   GPIO.output(26, GPIO.LOW)
   os.system('aplay /root/wifi.wav')

with open("/boot/input") as file:
   contents = file.read()
   if "streamer" in contents:
      GPIO.output(13, GPIO.HIGH)
      GPIO.output(26, GPIO.LOW)

with open("/boot/input") as file:
   contents = file.read()
   if "coax" in contents:
      GPIO.output(13, GPIO.LOW)
      GPIO.output(26, GPIO.LOW)

with open("/boot/input") as file:
   contents = file.read()
   if "opt" in contents:
      GPIO.output(26, GPIO.HIGH)
      GPIO.output(13, GPIO.LOW)
