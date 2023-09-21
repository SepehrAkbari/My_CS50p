import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe .*?src=["\'](https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+))["\']'

    match = re.search(pattern, s)
sz
    if match:
        video_id = match.group(2)

        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
