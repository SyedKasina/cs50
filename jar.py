# https://cs50.harvard.edu/python/2022/psets/8/jar/

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity isn't non-negative")

        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError("Adding more cookies than max capacity")
        elif n < 0:
            raise ValueError("Not enough cookies to remove")

        self._size = n
