import math

def binaryConvert(integer):
    if integer == 0 : return '0'
    dec = integer
    bin = ''
    while dec != 0:
        if dec % 2 == 0:
            bin = '0'+bin
        else:
            bin = '1'+bin
        dec //= 2
    return bin

def decimalConvert(decimal):
    dec = decimal
    bin = ''
    while dec != 1:
        dec *= 2
        if dec >= 1:
            dec -= 1
            bin += '1'
        else:
            bin += '0'
        if len(bin) == 24:
            break
    return bin

def signCheck(x):
    if x >= 0:
        return '0'
    else:
        return '1'

def findExpo(whole,decimal):
    count = 0
    if whole == '0':
        while True:
            if decimal[count] == '0':
                count += 1
            elif decimal[count] == '1':
                count += 1
                break
        return count*-1
    return len(whole)-1
    

            


def expoToBinary(exponent,offset):
    tempExpo = exponent + offset
    bin = binaryConvert(tempExpo)
    while len(bin) != 8:
        bin = '0'+bin
    return bin

def IEE32(integer):
    sign = signCheck(integer)
    if integer < 0: integer *= -1

    wholeInt = int(integer)
    decInt = integer - wholeInt

    wholeInt = binaryConvert(wholeInt)
    decInt = decimalConvert(decInt)

    expo = findExpo(wholeInt,decInt)
    expoBin = expoToBinary(expo,127)
    
    binary = wholeInt + decInt

    return expoBin
    

"""test = binaryConvert(int(input("Enter number: ")))
test = test
print(test)"""

print(findExpo('0','001'))
