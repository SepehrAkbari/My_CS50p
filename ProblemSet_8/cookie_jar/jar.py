class Jar:
    def __init__(self, capacity: int = 12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, x: int):
        if x > self.capacity or x + self.size > self.capacity:
            raise ValueError
        self._size += x

    def withdraw(self, x: int):
        if x > self.size:
            raise ValueError
        self._size -= x

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)

if __name__ == "__main__":
    main()
