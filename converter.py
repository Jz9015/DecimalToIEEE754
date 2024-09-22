def binary(integer):
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

"""test = binary(int(input("Enter number: ")))
test = test
print(test)"""

print(decimalConvert(.09375))
