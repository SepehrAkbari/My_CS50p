import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    n = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    x = re.search(r"^" + n + "\." + n + "\." + n + "\." + n + "$", ip)

    if x:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
