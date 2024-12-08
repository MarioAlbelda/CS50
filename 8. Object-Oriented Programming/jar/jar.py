class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("The number of cookies must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to deposit must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Cookie jar's capacity exceeded")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies to withdraw must be a non-negative integer")
        if self._size - n < 0:
            raise ValueError("There aren't that many cookies in the cookie jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
