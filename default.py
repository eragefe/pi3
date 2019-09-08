import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

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
