#The inverse factorial function
#New comment

def inverse_factorial(number):
    factorial_test = number
    divisor = 2.0
    count = 1.0
    
    while number > 1.0:
        number = number / divisor
        divisor = divisor + 1.0
        count += 1.0
    
    if number == 1.0:
        if count > 1.0:
            a = "{0}!".format(count)
            print(a)
            return a
        elif count == 1.0:
            c = "{0}! or 0!".format(count)
            print(c)
            return c
    elif number != 1.0:
        b = "NONE"
        print(b)
        return b
