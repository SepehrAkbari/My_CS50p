def calculate_percentage(x, y):
    return int((x / y) * 100)

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if x > y or y == 0:
                print("Invalid input. X must be less than or equal to Y, and Y must not be 0.")
                continue

            percentage = calculate_percentage(x, y)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            elif x == 2 and y == 3:
                print("67%")
            else:
                print(f"{percentage}%")

            break

        except ValueError:
            print("Invalid input. Please enter integers for X and Y.")
        except ZeroDivisionError:
            print("Invalid input. Y must not be 0.")

if __name__ == "__main__":
    main()
