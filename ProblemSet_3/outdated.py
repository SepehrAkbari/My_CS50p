months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def x(input_date):
    try:
        sec = input_date.split()
        if len(sec) == 1:
            month, day, year = map(int, sec[0].split('/'))
        elif len(sec) == 3:
            month = months.index(sec[0]) + 1
            day = int(sec[1][:-1])
            year = int(sec[2])
        else:
            raise ValueError

        if month < 1 or month > 12 or day < 1 or day > 31:
            raise ValueError

        return f"{year:04d}-{month:02d}-{day:02d}"
    except (ValueError, IndexError):
        return None

def main():
    while True:
        inp = input("Date: ").strip()
        formatted_date = x(inp)

        if formatted_date:
            print(formatted_date)
            break

if __name__ == "__main__":
    main()
