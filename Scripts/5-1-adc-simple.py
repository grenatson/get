import RPi.GPIO as GPIO
from dec2bin import d2b
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
max_voltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    for i in range(0, 2 ** len(dac)):
        GPIO.output(dac, d2b(i))
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            return i
    raise ValueError

try:
    while True:
        digital_vol = adc()
        voltage = digital_vol / 2 ** len(dac) * max_voltage
        print('Digital "voltage": {}, analog voltage: {}'.format(digital_vol, voltage))

except ValueError:
    print('Voltage cannot be found')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()