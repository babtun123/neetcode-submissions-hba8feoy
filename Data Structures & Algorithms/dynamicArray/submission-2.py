class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # check size
        if self.size == self.capacity:
            self.resize()
        
        # insert at next empty position
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        # resize the array
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # copy current array into the temp array
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        # copy the temp arr back to the dynamic array
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
