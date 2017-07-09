#Copyright(C)Thiruselvan Manian@lightshowpi
#DefaultSequence
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)


while True:
	GPIO.output(7,GPIO.HIGH)
	