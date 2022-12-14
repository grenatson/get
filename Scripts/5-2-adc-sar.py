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

def adc_new():
    result = 0
    for i in range(len(dac) - 1, -1, -1):
        result += 2 ** i
        GPIO.output(dac, d2b(result))
        time.sleep(0.00005)
        if GPIO.input(comp) == 0:
            result -= 2 ** i
    return result

try:
    while True:
        digital_volt = adc_new()
        time.sleep(0.25)
        voltage = digital_volt / 2 ** len(dac) * max_voltage
        print('Digital "voltage": {}, analog voltage: {}'.format(digital_volt, voltage))

except ValueError:
    print('Voltage cannot be found')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()