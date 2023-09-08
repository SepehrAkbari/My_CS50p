def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case

def main():
    user_input = input("camelCase: ")
    snake_case_name = camel_to_snake(user_input)
    print(f"snake_case: {snake_case_name}")

if __name__ == "__main__":
    main()
