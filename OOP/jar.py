class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non‑negative integer")
        else: 
            self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cookies do not fit in the Jar")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There are not enough cookies in the Jar")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non‑negative integer")
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0 or value > self.capacity:
            raise ValueError("Size must be between 0 and capacity")
        self._size = value



if __name__ == "__main__":
    Cookies = Jar(10)
    print(Cookies)       
    Cookies.deposit(5)
    print(Cookies)     
    Cookies.withdraw(2)
    print(Cookies)  

    