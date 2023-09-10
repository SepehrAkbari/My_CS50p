import emoji

def main():
    emojize()

def emojize():
    i = input("Input: ")
    print(f"Output: {emoji.emojize(i)}")

if __name__ == "__main__":
    main()
