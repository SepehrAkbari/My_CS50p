def get_media_type(filename):
    lower_filename = filename.lower()

    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    for ext, media_type in media_types.items():
        if lower_filename.endswith(ext):
            return media_type

    return "application/octet-stream"

def main():
    filename = input("File name: ")
    media_type = get_media_type(filename)
    print(media_type)

if __name__ == "__main__":
    main()
