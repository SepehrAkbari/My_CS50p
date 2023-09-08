def remove_vowels(text):
    vowels = "AEIOUaeiou"
    x = ''.join([char for char in text if char not in vowels])
    return x

def main():
    i = input("Input: ")
    x = remove_vowels(i)
    print("Output", x)

if __name__ == "__main__":
    main()
