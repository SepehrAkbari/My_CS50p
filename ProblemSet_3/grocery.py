def main():
    x()

def x():
    gl = {}
    while True:
        try:
            i = input().upper()
            if i in gl:
                gl[i] += 1
            else:
                gl[i] = 1
        except EOFError:
            for k, v in sorted(gl.items()):
                        print(v, k)
            break


if __name__ == "__main__":
    main()
