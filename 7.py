
def decToBinary(number):
    binary = ""
    while True:
        # print(number)
        binary = str(number % 2)+binary
        number = number //2
        if number == 0:
            break
    return binary

def decimalToOctal(number):
    octal = ""
    while True:
        octal = str(number % 8)+octal
        number = number //8
        if number == 0:
            break
    
    return octal
def decimalToHexadecimal(number):
    hexadecimal = ""
    values = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    while True:
        rest = number % 16
        number = number // 16
        hexadecimal = str(values[rest]) + hexadecimal
        if number == 0:
            break
    return hexadecimal

def print_formatted(number):
    maxDeximal = 0
    maxOctal = 0
    maxHex = 0
    maxBin = 0

    arrayVars = []

    for i in range(1,number+1):
        decimal = str(i)
        octal = str(decimalToOctal(i))
        hexadecimal =  str(decimalToHexadecimal(i))
        binary = str(decToBinary(i))

        if len(decimal) > maxDeximal:
            maxDeximal = len(decimal)
        if len(octal) > maxOctal:
            maxOctal = len(octal)
        if len(hexadecimal) > maxHex:
            maxHex = len(hexadecimal)
        if len(binary) > maxBin:
            maxBin = len(binary)

        arrayVars.append([decimal,octal, hexadecimal, binary])
    for item in arrayVars:
        curDec = maxDeximal - len(item[0])
        curOct = maxOctal - len(item[1])
        curHex = maxHex - len(item[2])
        curBin = maxBin - len(item[3])
        for i in range(0,curDec):
            print(end=" ")
        print(item[0],end=" ")
        for i in range(0,curOct):
            print(end=" ")
        print(item[1],end=" ")
        for i in range(0,curHex):
            print(end=" ")
        print(item[2],end=" ")
        for i in range(0,curBin):
            print(end=" ")
        print(item[3])
        
        




        
           
# for i in range(1,number):
    #     print(str(i)+" "+str(i))
if __name__ == '__main__':
    n = 10
    print_formatted(n)