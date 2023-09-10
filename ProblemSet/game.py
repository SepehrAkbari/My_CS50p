import random

def get_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid positive integer.")

def main():
    level = get_positive_integer("Level: ")
    target_number = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess: ")

        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
