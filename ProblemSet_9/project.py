from tabulate import tabulate


def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilometer_to_mile(kilometer):
    return kilometer * 0.621371

def mile_to_kilometer(mile):
    return mile * 1.609344

def centimeter_to_inch(centimeter):
    return centimeter * 0.393701

def inch_to_centimeter(inch):
    return inch * 2.54

def kilogram_to_pound(kilogram):
    return kilogram * 2.20462

def pound_to_kilogram(pound):
    return pound * 0.453592

def liter_to_gallon(liter):
    return liter * 0.264172

def gallon_to_liter(gallon):
    return gallon * 3.78541

def celsius_to_fahrenheit(celsius):
    return  (celsius * (9/5)) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


def display_menu():
    menu = [
        ["1", "Convert meters to feet"],
        ["2", "Convert feet to meters"],
        ["3", "Quit"]
    ]
    return tabulate(menu, headers=["Choice", "Option"], tablefmt="rounded_outline")



def main():
    print("UNIT QUIRCKS")
    american= input("Are you an American? (yes/no): ").lower()
    if american == "yes" or american == "y":
        while True:
            print("")
            print(display_menu())

            choice = input("Enter your choice: ")

            if choice == '1':
                meters = float(input("Enter the value in meters: "))
                feet = convert_meters_to_feet(meters)
                print("")
                print(f"{meters} meters is equal to {feet} feet.")
            elif choice == '2':
                feet = float(input("Enter the value in feet: "))
                meters = convert_feet_to_meters(feet)
                print("")
                print(f"{feet} feet is equal to {meters} meters.")
            elif choice == '3':
                print("")
                print("Goodbye!")
                print("")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    elif american == "no" or american == "n":
        pass
    else:
        print("please respond with only 'yes' or 'no'")

if __name__ == "__main__":
    main()
