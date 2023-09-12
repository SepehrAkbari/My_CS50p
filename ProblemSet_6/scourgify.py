import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

before = sys.argv[1]
after = sys.argv[2]

def filetype(filename):
    splitfilename = filename.split(".")
    ft = splitfilename[-1]
    return ft

before_type = filetype(before)
after_type = filetype(after)

if after_type != "csv":
    sys.exit("new file should be csv")

if before_type != "csv":
    sys.exit(f"Could not read {before}")
    
b = []

try:
    with open(before) as file:
            reader = csv.DictReader(file)
            for row in reader:
                b.append({"name": row["name"], "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {before}")

with open(after, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['first', 'last', 'house'])

    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    for i in b:
        writer.writerow({'first': i["name"].split(", ")[1], 'last': i["name"].split(", ")[0], 'house': i["house"]})
