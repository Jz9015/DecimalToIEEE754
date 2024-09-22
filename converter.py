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

def addPadding(bin,index):
    while len(bin) != index:
        bin += '0'
    return bin

def IEEE32(integer):
    binary = '0'
    if integer == 0:
        binary = addPadding(binary,32)
        return binary

    sign = signCheck(integer)
    if integer < 0: integer *= -1

    wholeInt = int(integer)
    decInt = integer - wholeInt

    wholeBin = binaryConvert(wholeInt)
    decBin = decimalConvert(decInt)

    expo = findExpo(wholeBin,decBin)
    expoBin = expoToBinary(expo,127)

    if wholeBin == '0':   
        decBin = decBin[(expo*-1):]
        binary = sign + expoBin + decBin
        binary = binary[:32]
        binary = addPadding(binary,32)
    else:
        wholeBin = wholeBin[1:]
        binary = sign + expoBin + wholeBin + decBin
        binary = binary[:32]
        binary = addPadding(binary,32)

    return binary
    

"""test = binaryConvert(int(input("Enter number: ")))
test = test
print(test)"""

print(IEEE32(0))
