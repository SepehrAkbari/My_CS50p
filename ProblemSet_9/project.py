from tabulate import tabulate

def main():
    x = True
    z = True
    print(" ")
    print("UNIT QUIRCKS")

    while z:
        print(main_menu())
        american = input("Enter your choice: ")

        if american == '1':
            while x:
                print("")
                print(US_menu())

                choice = input("Enter your choice: ")

                if choice == '0':
                    print(" ")
                    x == False
                    break
                elif choice == '1':
                    feet = float(input("Enter the value in feets: "))
                    meters = feet_to_meters(feet)
                    print("")
                    print(f"{feet} feet is equal to {meters} meter.")
                elif choice == '2':
                    mile = float(input("Enter the value in miles: "))
                    kilometer = mile_to_kilometer(mile)
                    print("")
                    print(f"{mile} mile is equal to {kilometer} Kilometer.")
                elif choice == '3':
                    inch = float(input("Enter the value in inches: "))
                    centimeter = inch_to_centimeter(inch)
                    print("")
                    print(f"{inch} inch is equal to {centimeter} centimeter.")
                elif choice == '4':
                    pound = float(input("Enter the value in pounds: "))
                    kilogram = pound_to_kilogram(pound)
                    print("")
                    print(f"{pound} pound is equal to {kilogram} kilogram.")
                elif choice == '5':
                    gallon = float(input("Enter the value in gallons: "))
                    liter = gallon_to_liter(gallon)
                    print("")
                    print(f"{gallon} gallon is equal to {liter} liter.")
                elif choice == '6':
                    fahrenheit = float(input("Enter the value in fahrenheits: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print("")
                    print(f"{fahrenheit} fahrenheit is equal to {celsius} celsius.")
                else:
                    print("Invalid choice. Please select a valid option.")

        elif american == '2':
            while x:
                print("")
                print(other_menu())

                choice = input("Enter your choice: ")

                if choice == '0':
                    print(" ")
                    x == False
                    break
                elif choice == '1':
                    meters = float(input("Enter the value in meters: "))
                    feet = meters_to_feet(meters)
                    print("")
                    print(f"{meters} meter is equal to {feet} feet.")
                elif choice == '2':
                    kilometer = float(input("Enter the value in kilometers: "))
                    mile = kilometer_to_mile(kilometer)
                    print("")
                    print(f"{kilometer} kilometer is equal to {mile} mile.")
                elif choice == '3':
                    cm = float(input("Enter the value in centimeters: "))
                    inch = centimeter_to_inch(cm)
                    print("")
                    print(f"{cm} centimeter is equal to {inch} inch.")
                elif choice == '4':
                    kilogram = float(input("Enter the value in kilograms: "))
                    pound = kilogram_to_pound(kilogram)
                    print("")
                    print(f"{kilogram} kilogram is equal to {pound} pound.")
                elif choice == '5':
                    liter = float(input("Enter the value in liters: "))
                    gallon = liter_to_gallon(liter)
                    print("")
                    print(f"{liter} liter is equal to {gallon} gallon.")
                elif choice == '6':
                    celsius = float(input("Enter the value in celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print("")
                    print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit.")
                else:
                    print("Invalid choice. Please select a valid option.")
                    

        elif american == '0':
            print("")
            print("Goodbye!")
            print("")
            z == False
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

def meters_to_feet(meters):
    feet = meters * 3.28084
    return round(feet, 2)

def feet_to_meters(feet):
    meter = feet / 3.28084
    return round(meter, 2)

def kilometer_to_mile(kilometer):
    mile = kilometer * 0.621371
    return round(mile, 2)

def mile_to_kilometer(mile):
    km = mile * 1.609344
    return round(km, 2)

def centimeter_to_inch(centimeter):
    inch = centimeter * 0.393701
    return round(inch, 2)

def inch_to_centimeter(inch):
    cm = inch * 2.54
    return round(cm, 2)

def kilogram_to_pound(kilogram):
    pound = kilogram * 2.20462
    return round(pound, 2)

def pound_to_kilogram(pound):
    kg = pound * 0.453592
    return round(kg, 2)

def liter_to_gallon(liter):
    gallon = liter * 0.264172
    return round(gallon, 2)

def gallon_to_liter(gallon):
    liter = gallon * 3.78541
    return round(liter, 2)

def celsius_to_fahrenheit(celsius):
    f = (celsius * (9/5)) + 32
    return round(f, 2)

def fahrenheit_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * (5/9)
    return round(c, 2)


def main_menu():
    menu = [
        ["0", "Quit"],
        ["1", "I am an American"],
        ["2", "I am NOT an American"]
    ]
    return tabulate(menu,headers=["Choice", "Option"], tablefmt="rounded_outline")

def US_menu():
    menu = [
        ["0", "Back"],
        ["1", "Convert feet to meter"],
        ["2", "Convert mile to kilometer"],
        ["3", "Convert inch to centimeter"],
        ["4", "Convert pound to kilogram"],
        ["5", "Convert gallon to liter"],
        ["6", "Convert fahrenheit to celsius"]
    ]
    return tabulate(menu, headers=["Choice", "Option"], tablefmt="rounded_outline")

def other_menu():
    menu = [
        ["0", "Back"],
        ["1", "Convert meter to feet"],
        ["2", "Convert kilometer to mile"],
        ["3", "Convert centimeter to inch"],
        ["4", "Convert kilogram to pound"],
        ["5", "Convert liter to gallon"],
        ["6", "Convert celsius to fahrenheit"]
    ]
    return tabulate(menu, headers=["Choice", "Option"], tablefmt="rounded_outline")

if __name__ == "__main__":
    main()
