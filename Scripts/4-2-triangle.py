import RPi.GPIO as GPIO
import time

dac = [26, 19 ,13, 6, 5, 11, 9, 10]
period = int(input("Enter period in seconds: "))
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    signal = 0
    while True:
        GPIO.output(dac, dec2bin(signal % 256))
        time.sleep(period / 256)
        signal += 1

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()