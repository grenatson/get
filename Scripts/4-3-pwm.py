import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup([31, 20, 16, 12, 7, 8], GPIO.OUT, initial=1)

p = GPIO.PWM(24, 50)
p.start(10)
input('Press enter to stop')
p.stop()

GPIO.cleanup()