def main():
    x = input("What time is it? ")
    hours = convert(x)

    if hours >= 7.0 and hours <= 8.0:
        print("breakfast time")
    elif hours >= 12.0 and hours <= 13.0:
        print("lunch time")
    elif hours >= 18.0 and hours <= 19.0:
        print("dinner time")

def convert(x):
    x = x.split(":")
    minutes = float(x[1]) / 60
    return(float(x[0]) + minutes)


if __name__ == "__main__":
    main()
