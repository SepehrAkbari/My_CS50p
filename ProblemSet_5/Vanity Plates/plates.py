def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    n = abc + num
    c = []

    c = []
    for i in s:
        if n.count(i) == 0:
            c.append(False)
        else:
            c.append(True)
    y = all(c)
    if y == True:
        c.append(True)
    else:
        c.append(False)

    if 2 <= len(s) <= 6:
        c.append(True)
    else:
        c.append(False)

    if len(s) >= 2:
        if abc.count(s[0]) == 0 or abc.count(s[1]) == 0:
            c.append(False)
        else:
            c.append(True)

    check = ""
    for i in s:
        if abc.count(i) != 0:
            check = check + "1"
        if num.count(i) != 0:
            check = check + "0"
    if check.count("01") != 0:
        c.append(False)
    else:
        c.append(True)

    for i in s:
        if num.count(i) == 0:
            c.append(True)
        else:
            snum = ""
            for i in s:
                if num.count(i) != 0:
                    snum = snum + i
            if snum[0] == "0":
                 c.append(False)
            else:
                c.append(True)

    x = all(c)
    if x == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
