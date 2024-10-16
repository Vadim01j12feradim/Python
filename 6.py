if __name__ == '__main__':
    s = "qA2"
    R1 = False
    R2 = False
    R3 = False
    R4 = False
    R5 = False

    for char in s:
        if char.isalnum() and R1 == False:
            R1 = True
        if char.isalpha() and  R2 == False:
            R2 = True
        if char.isdigit() and  R3 == False:
            R3 = True
        if char.islower() and  R4 == False:
            R4 = True
        if char.isupper() and  R5 == False:
            R5 = True

    print(R1)
    print(R2)
    print(R3)
    print(R4)
    print(R5)

