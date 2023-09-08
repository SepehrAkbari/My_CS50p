def calculate(expression):
    x, operator, z = expression.split()

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    return result

def main():
    user_input = input("Expression: ")
    try:
        result = calculate(user_input)
        print(f"{result:.1f}")
    except ValueError:
        print("Invalid input format. Please use 'x + z' format.")

if __name__ == "__main__":
    main()
