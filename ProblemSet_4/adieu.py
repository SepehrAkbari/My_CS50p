def x(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        return f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"
      
def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        if names:
            n = x(names)
            print(n)

if __name__ == "__main__":
    main()
