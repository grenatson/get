import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

if (GPIO.input(17)):
    GPIO.output(26, 1)
if (not GPIO.input(17)):
    GPIO.output(26, 0)