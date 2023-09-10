import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        X, Y = generate_integer(level)
        problem = f"{X} + {Y} = "
        correct_answer = X + Y
        attempts = 0

        while attempts < 3:
            user_answer = input(problem)

            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    #print("Correct!")
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        if attempts == 3:
            print(f"{X}+{Y}: {correct_answer}")

    print(f"Your score is: {score}/10")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid level (1, 2, or 3).")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)

if __name__ == "__main__":
    main()
