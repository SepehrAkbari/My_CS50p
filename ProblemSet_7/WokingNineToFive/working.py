import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)$'

    match = re.match(pattern, s)

    if match:
        start_hour = int(match.group(1))
        start_minute = int(match.group(2)[1:]) if match.group(2) else 0
        start_meridiem = match.group(3)
        end_hour = int(match.group(4))
        end_minute = int(match.group(5)[1:]) if match.group(5) else 0
        end_meridiem = match.group(6)

        if start_meridiem == "PM" and start_hour != 12:
            start_hour += 12
        elif start_meridiem == "AM" and start_hour == 12:
            start_hour = 0

        if end_meridiem == "PM" and end_hour != 12:
            end_hour += 12
        elif end_meridiem == "AM" and end_hour == 12:
            end_hour = 0

        if 0 <= start_hour <= 23 and 0 <= start_minute <= 59 and 0 <= end_hour <= 23 and 0 <= end_minute <= 59:
            start_time = f"{start_hour:02d}:{start_minute:02d}"
            end_time = f"{end_hour:02d}:{end_minute:02d}"
            return f"{start_time} to {end_time}"

    raise ValueError("Invalid input format or invalid time")

if __name__ == "__main__":
    main()
