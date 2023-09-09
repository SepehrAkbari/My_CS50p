menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    t = 0.00

    try:
        while True:
            i = input("Item: ").strip().title()

            if i in menu:
                t += menu[i]
                print(f"Total: ${t:.2f}")
            else:
                continue

    except EOFError:
        pass

if __name__ == "__main__":
    main()
