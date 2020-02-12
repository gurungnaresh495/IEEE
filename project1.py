"""
    convert_float_binary(n)

    This function takes integer as an arugument and
    returns the equivalent binary number
"""

def convert_float_binary(n):
    # getting whole numbers before decimal point
    frontnumber = int(n //1)

    # getting fraction number after decimal point
    backnumber = n % 1

    #changing front part into binary
    frontbinary = int("{0:b}".format(frontnumber))

    #variable for storing binary of fraction
    backbinary = 0

    # we wonly need upto fourth place, so looping four times
    # we multiply by 2 to the fraction and extract the whole number
    # to concatenate
    for i in range(4):
        backnumber = backnumber * 2
        temp = backnumber // 1
        temp /= 10**(i+1)
        backbinary += temp
        backnumber = backnumber % 1

    return frontbinary + backbinary


""" 
    Calculate_sign_bit(n)
    
    This is the simple function which returns 1 
    if the given number is negative and returns
    0 if the number is positive
"""
def calculate_sign_bit(n):
    if n < 0:
        return 1
    else:
        return 0


"""
     normalize_binary(n)
     
     this function takes an integer as a parameter
     and returns a list of two elements
     first one is the exponential and 
     second one is the normalized binary number   
"""
def normalize_binary(n):
    deci = binarynumber = convert_float_binary(n)
    expo = 0

    #counting exponential
    while binarynumber > 10:
        binarynumber /= 10
        expo += 1
    deci = deci / 10 ** expo
    norm = str(deci)
    norm = norm[2:]
    return [expo, norm]

"""
    calculate_exponent_biased(n)
    
    this function returns takes number as a parameter
    and calls the normalize_binary(n) function to
    normalize the given number. 
    calculates the biased exponent    
"""
def calculate_exponent_biased(n):
    norm = normalize_binary(n)
    temp = (2 **(8-1)) - 1 + norm[0]
    return int(convert_float_binary(temp))

"""
    IEEE754_rep(num)
    
    this function takes the number a sa parameter
    calls above functions to calculate sign bit,
    biased exponent, normalize
    finally returns the IEEE754 representation of the given number
"""
def IEEE754_rep(num):
    sign = calculate_sign_bit(num)
    biased_expo = calculate_exponent_biased(num)
    norm = normalize_binary(num)
    fraction = norm[1] + "0" * (23 - len(norm[1]))
    return str(sign) + "-" + str(biased_expo) + "-" + str(fraction)

"""
    ieee_754_to_float(n)
    
    this function takes string as a parameter which represents 
    IEEEE 754. It performs stepwise conversion and finally returns
    decimal number
"""
def ieee_754_to_float(n):
    ieee_str = n

    #first char of the string is the sign bit
    sign = ieee_str[0]

    #excluding sign bit
    ieee_str = ieee_str[2:]
    biased_expo = ""

    #extracting first 8 binary exponent
    for i in ieee_str:
        biased_expo += i
        if len(biased_expo) == 8:
            break

    #getting binary numbers after binary exponent
    ieee_str = ieee_str[9:]
    #converting binary exponent into biased exponent
    expo_dec = int(biased_expo,2)
    expo_dec = expo_dec-127

    #getting only fraction part
    fraction = float("1." + ieee_str)
    fraction *= 10**expo_dec

    front_binary, back_binary = str(fraction).split(".")
    front_deci = int(front_binary,2)
    back_deci = 0
    counter = 1

    #converting the fraction into decimal
    for i in back_binary:
        if int(i) != 0:
            back_deci += 1/(2 ** counter)
        counter += 1

    #handling sign bit
    result = front_deci + back_deci
    if sign == 1:
        return -1 * result
    else:
        return result
inp = float(input("Please enter the number: "))
ieee = IEEE754_rep(inp)

print("\n The IEEE 754 representation of " + str(inp) + " is" + str(ieee))

print(ieee_754_to_float(str(ieee)))
