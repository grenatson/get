import RPi.GPIO as GPIO
from dec2bin import d2b

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
max_voltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    dac_len = len(dac)
    bin_value = d2b(2 ** (dac_len - 1))
    for i in range(dac_len):
        GPIO.output(dac, bin_value)
        if GPIO.input(comp) == 0:
            bin_value[i] = 0
        else:
            bin_value[i] = 1
    if GPIO.input(comp) == 1:
        raise ValueError
    return sum([bin_value[i] * 2 ** (dac_len - 1 - i) for i in range(dac_len)])


try:
    while True:
        digital_volt = adc()
        voltage = digital_volt / 2 ** (len(dac) + 1) * max_voltage
        print('Digital "voltage": {}, analog voltage: {}'.format(digital_volt, voltage))

except ValueError:
    print('Voltage cannot be found')

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()