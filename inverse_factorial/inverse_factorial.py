
def inverse_factorial(number):
    factorial_test = number
    divisor = 2
    count = 1
    
    while number > 1:
        number = number / divisor
        divisor = divisor + 1
        count += 1
    
    if number == 1:
        if count > 1:
            a = "{0}!".format(count)
            print(a)
            return a
        elif count == 1:
            c = "{0}! or 0!".format(count)
            print(c)
            return c
    elif number != 1:
        b = "NONE"
        print(b)
        return b
