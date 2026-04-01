class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = []

    def get(self, i: int) -> int:
        if i < self.size:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < self.size:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        self.resize()
        self.arr.append(n)
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr.pop()

    def resize(self) -> None:
        if self.size >= self.capacity:
            self.capacity = self.size * 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
