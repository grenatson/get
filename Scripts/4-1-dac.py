import RPi.GPIO as GPIO

dac = [26, 19 ,13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

try:
    while True:
        print("Enter a number: ")
        my_input = input()
        if (my_input == "q"):
            break
        if not my_input.isdigit():
            print("ERROR: input is not an integer")
            break
        number = int(my_input)
        if not(0 <= number <= 255) or number < 0:
            print("ERROR: input is out of range")
            break
        GPIO.output(dac, decimal2binary(number))
        print("voltage: " + str(number * 3.3 / 2 ** 8))

#except ValueError:
#    print("ERROR: input is not an integer")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()