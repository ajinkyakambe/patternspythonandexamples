def check_amstrong_number(number):
    x = [int(a) for a in str(number)]
    # 1 5 3  = 1^3 + 5^3 + 3^3  = 1 + 125 + 27 = 153

    additionofnumber = 0
    for numvalue in x:
        additionofnumber = additionofnumber + (numvalue * numvalue * numvalue)

    if additionofnumber == number:
        print("Number is armstrong number")
    else:
        print("Number is not armstrong number")


# Driving code

# example 1
number1 = 153
check_amstrong_number(number1)

# example 3
number3 = 125
check_amstrong_number(number3)

# example 2
number2 = 452
check_amstrong_number(number2)