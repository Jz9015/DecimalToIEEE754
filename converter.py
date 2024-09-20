def binary(decimal):
    x = decimal
    bin = ''
    while x != 0:
        if x % 2 == 0:
            bin = '0'+bin
        else:
            bin = '1'+bin
        x = x//2
    return bin


test = binary(1)
print(test)