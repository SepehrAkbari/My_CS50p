def main():
    while True:
        try:
            n = input("Fraction: ")
            print(gauge(convert(n)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(n):
    x, y = n.split("/")
    x = int(x)
    y = int(y)
    f = x / y
    if f > 1:
        raise ValueError
    return round(f * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
