import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

number_decimal = 10
number_binary = []
for i in range(len(dac)):
    number_binary.append(1)

def binary(n, n_bi):
    n_bi_len = len(n_bi)
    for i in range(n_bi_len):
        n_bi[n_bi_len - 1 - i] = n % 2
        n //= 2 

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

binary(number_decimal, number_binary)

GPIO.output(dac, number_binary)

time.sleep(5)
GPIO.output(dac, 0)
GPIO.cleanup()