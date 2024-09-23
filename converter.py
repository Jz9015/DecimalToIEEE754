from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

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
        if len(bin) == 237:
            break
    return bin

def signCheck(x):
    if x >= 0:
        return '0'
    else:
        return '1'
    
def getExpoWidth(size):
    if size == 16:
        return 5
    elif size == 32:
        return 8
    if size == 64:
        return 11
    if size == 128:
        return 15
    if size == 256:
        return 19

def getOffset(size):
    if size == 16:
        return 15
    elif size == 32:
        return 127
    if size == 64:
        return 1023
    if size == 128:
        return 16383
    if size == 256:
        return 262143

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

def expoToBinary(exponent,expoWidth,offset):
    tempExpo = exponent + offset
    bin = binaryConvert(tempExpo)
    while len(bin) != expoWidth:
        bin = '0'+bin
    return bin

def addPadding(bin,index):
    while len(bin) != index:
        bin += '0'
    return bin

def IEEE754(integer,size):
    binary = '0'
    if integer == 0:
        binary = addPadding(binary,size)
        return binary

    sign = signCheck(integer)
    if integer < 0: integer *= -1

    wholeInt = int(integer)
    decInt = integer - wholeInt

    wholeBin = binaryConvert(wholeInt)
    decBin = decimalConvert(decInt)

    expo = findExpo(wholeBin,decBin)
    expoBin = expoToBinary(expo,getExpoWidth(size),getOffset(size))

    if wholeBin == '0':   
        decBin = decBin[(expo*-1):]
        binary = sign + expoBin + decBin
        binary = binary[:size]
        binary = addPadding(binary,size)
    else:
        wholeBin = wholeBin[1:]
        binary = sign + expoBin + wholeBin + decBin
        binary = binary[:size]
        binary = addPadding(binary,size)

    return binary

@app.route('/') 
def my_Form():
    return render_template('main.html')

@app.route('/', methods=['POST'])
def my_form_post():
    userNum = request.form['userNum']
    bitSize = request.form['bitSize']
    if userNum == '':
        userNum = 0
    output = IEEE754(float(userNum),int(bitSize))
    return render_template('main.html',out=output)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)