a = input()
if a.find("?") < 0:
    digit1 = eval(a[0]) * 2
    digit2 = eval(a[1]) * 3
    digit3 = eval(a[2]) * 5
    digit4 = eval(a[3]) * 7
    checkdigit = (digit1 + digit2 + digit3 + digit4) % 11
    if a[5] == "X":
        if checkdigit == 10:
            print("VALID")
        else:
            print("INVALID")
    if a[5] != "X":
        if checkdigit == 10:
            print("INVALID")
        else:
            if checkdigit == eval(a[5]):
                print("VALID")
            else:
                print("INVALID")
elif 0 <= a.find("?") < 4:
    # First digit is missing
    if a.find("?") == 0:
        digit2 = eval(a[1]) * 3
        digit3 = eval(a[2]) * 5
        digit4 = eval(a[3]) * 7
        sumdigit = digit2 + digit3 + digit4
        modsumdigit = sumdigit % 11
        if a[5] == "X":
            if modsumdigit < 10:
                nmodsumdigit = 10 + 11 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 2 // 11
                new2 = new * 2 - mul * 11
                new3 = (new2 ** 9) % 11
                print(str(new3) + a[1:])
            else:
                nmodsumdigit = 10 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 2 // 11
                new2 = new * 2 - mul * 11
                new3 = (new2 ** 9) % 11
                print(str(new3) + a[1:])
        elif modsumdigit < eval(a[5]):
            nmodsumdigit = eval(a[5]) + 11 - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 2 // 11
            new2 = new * 2 - mul * 11
            new3 = (new2 ** 9) % 11
            print(str(new3) + a[1:])
        else:
            nmodsumdigit = eval(a[5]) - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 2 // 11
            new2 = new * 2 - mul * 11
            new3 = (new2 ** 9) % 11
            print(str(new3) + a[1:])
    # Second digit is missing
    elif a.find("?") == 1:
        digit1 = eval(a[0]) * 2
        digit3 = eval(a[2]) * 5
        digit4 = eval(a[3]) * 7
        sumdigit = digit1 + digit3 + digit4
        modsumdigit = sumdigit % 11
        if a[5] == "X":
            if modsumdigit < 10:
                nmodsumdigit = 10 + 11 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 3 // 11
                new2 = new * 3 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0] + str(new3) + a[2:])
            else:
                nmodsumdigit = 10 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 3 // 11
                new2 = new * 3 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0] + str(new3) + a[2:])
        elif modsumdigit < eval(a[5]):
            nmodsumdigit = eval(a[5]) + 11 - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 3 // 11
            new2 = new * 3 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0] + str(new3) + a[2:])
        else:
            nmodsumdigit = eval(a[5]) - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 3 // 11
            new2 = new * 3 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0] + str(new3) + a[2:])
    # Third digit is missing
    elif a.find("?") == 2:
        digit1 = eval(a[0]) * 2
        digit2 = eval(a[1]) * 3
        digit4 = eval(a[3]) * 7
        sumdigit = digit1 + digit2 + digit4
        modsumdigit = sumdigit % 11
        if a[5] == "X":
            if modsumdigit < 10:
                nmodsumdigit = 10 + 11 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 5 // 11
                new2 = new * 5 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0:2] + str(new3) + a[3:])
            else:
                nmodsumdigit = 10 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 5 // 11
                new2 = new * 5 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0:2] + str(new3) + a[3:])
        elif modsumdigit < eval(a[5]):
            nmodsumdigit = eval(a[5]) + 11 - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 5 // 11
            new2 = new * 5 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0:2] + str(new3) + a[3:])
        else:
            nmodsumdigit = eval(a[5]) - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 5 // 11
            new2 = new * 5 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0:2] + str(new3) + a[3:])
    # Fourth digit is missing
    elif a.find("?") == 3:
        digit1 = eval(a[0]) * 2
        digit2 = eval(a[1]) * 3
        digit3 = eval(a[2]) * 5
        sumdigit = digit1 + digit2 + digit3
        modsumdigit = sumdigit % 11
        if a[5] == "X":
            if modsumdigit < 10:
                nmodsumdigit = 10 + 11 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 7 // 11
                new2 = new * 7 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0:3] + str(new3) + a[4:])
            else:
                nmodsumdigit = 10 - modsumdigit
                new = (nmodsumdigit ** 9) % 11
                mul = new * 7 // 11
                new2 = new * 7 - mul * 11
                new3 = (new2 ** 9) % 11
                print(a[0:3] + str(new3) + a[4:])
        elif modsumdigit < eval(a[5]):
            nmodsumdigit = eval(a[5]) + 11 - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 7 // 11
            new2 = new * 7 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0:3] + str(new3) + a[4:])
        else:
            nmodsumdigit = eval(a[5]) - modsumdigit
            new = (nmodsumdigit ** 9) % 11
            mul = new * 7 // 11
            new2 = new * 7 - mul * 11
            new3 = (new2 ** 9) % 11
            print(a[0:3] + str(new3) + a[4:])
elif a.find("?") == 5:
    digit1 = eval(a[0]) * 2
    digit2 = eval(a[1]) * 3
    digit3 = eval(a[2]) * 5
    digit4 = eval(a[3]) * 7
    checkdigit = (digit1 + digit2 + digit3 + digit4) % 11
    if checkdigit == 10:
        print(a[0:5] + "X")
    else:
        print(a[0:5] + str(checkdigit))