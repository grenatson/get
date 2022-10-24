#возвращает список двоичной записи десятичного числа
def d2b(value, digits = 8):
    if value < 0:
        raise NameError("Sorry, function doesn't work with negatives.")
    if value >= 2 ** digits:
        raise NameError("Use a smaller value or more digits for the output.")
    return [int(item) for item in bin(value)[2:].zfill(digits)]

def adc_bin():
    result = 0
    for i in range(len(dac) - 1, -1, -1):
        result += 2 ** i
        GPIO.output(dac, d2b(result))
        time.sleep(0.005)
        if GPIO.input(comp) == 0:
            result -= 2 ** i
    return result