class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size = self.size + n

    def withdraw(self, n):
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 1:
            raise ValueError("Jars capacity can't be lower than 1")
        if n < self._size:
            raise ValueError("Capacity can't be lower than size")
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError("Exceeded jar capacity")
        if n < 0:
            raise ValueError("Jar doesn't have that many cookies")
        self._size = n
