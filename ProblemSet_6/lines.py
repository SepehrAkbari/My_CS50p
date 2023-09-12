import sys

if len(sys.argv) == 1:
    sys.exit("More lines are needed")

if len(sys.argv) > 2:
    sys.exit("Too many lines")

x = sys.argv[1]
y = x.split(".")
m = y[-1]

if m != "py":
    sys.exit("file must be fomated as .py")

n = 0
try:
    with open(x) as file:
        for line in file:
            if line.strip() != "" and line.strip().startswith("#") == False:
                n += 1

except FileNotFoundError:
    sys.exit("not found")

print(n)
