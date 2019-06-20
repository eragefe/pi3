import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# To read the state
state6 = GPIO.input(6)
state13 = GPIO.input(13)

if state6==1:
   GPIO.output(6, GPIO.LOW)
   GPIO.output(13, GPIO.LOW)
   file = open("/boot/input","w")
   file.write("opt")
   file.close()

if state6==0:
   GPIO.output(6, GPIO.LOW)
   GPIO.output(13, GPIO.HIGH)
   file = open("/boot/input","w")
   file.write("streamer")
   file.close()

if state13:
   GPIO.output(6, GPIO.HIGH)
   GPIO.output(13, GPIO.LOW)
   file = open("/boot/input","w")
   file.write("coax")
   file.close()
