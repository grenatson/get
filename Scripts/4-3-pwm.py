import RPi.GPIO as GPIO
from dec2bin import d2b

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]

pwm = GPIO.PWM(24, 1)
pwm.start(0)

try:
    while True:
        new_dc = int(input('Enter Duty Cycle value: '))
        pwm.ChangeDutyCycle(new_dc)
        print('Voltage: ' + str(3.3 * new_dc / 100))

finally:
    GPIO.output(24, 0)
    GPIO.cleanup()