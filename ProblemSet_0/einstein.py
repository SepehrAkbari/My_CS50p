speed_of_light = 300000000

def calculate_energy(mass):
    energy = mass * speed_of_light ** 2
    return energy

def main():
    mass = int(input("m: "))

    energy = calculate_energy(mass)

    print(f"E: {energy}")

if __name__ == "__main__":
    main()
