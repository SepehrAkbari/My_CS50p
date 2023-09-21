import re

def main():
    print(count(input("Input: ")))

def count(s):
    um_pattern = r'\bum\b'
    um_count = len(re.findall(um_pattern, s, re.IGNORECASE))
    return um_count

if __name__ == "__main__":
    main()
