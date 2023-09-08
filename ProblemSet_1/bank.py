def main():
    user_input = input("greeting: ").strip().lower()

    if user_input.startswith("hello"):
        print("$0")
    elif user_input.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
