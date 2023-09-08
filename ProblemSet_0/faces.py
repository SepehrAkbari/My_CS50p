def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    i = input()
    x = convert(i)
    print(x)

if __name__ == "__main__":
    main()
