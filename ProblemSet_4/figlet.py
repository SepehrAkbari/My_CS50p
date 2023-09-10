import sys, random
from pyfiglet import Figlet

x = Figlet()

def main(argv):
    if set_figlet_font(argv):
        render_message()
    else:
        sys.exit("Invalid usage")

def set_figlet_font(argv):
    f = x.getFonts()
    n = False
    if len(argv) == 1:
        x.setFont(font = f[random.randint(0, 424)])
        n = True
    elif len(argv) == 3:
        if argv[1] == "-f" or argv[1] == "--font":
            if argv[2] in f:
                x.setFont(font = argv[2])
                n = True
    return n

def render_message():
    out = input("Input: ")
    print("Output:", x.renderText(out), sep="\n")

if __name__ == "__main__":
    main(sys.argv)
