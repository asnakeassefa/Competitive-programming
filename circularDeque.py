class MyCircularDeque:
    
    
    """
    
    | 1| 2| 3| 4| 5|
            c
    | | 5| 2| 3| 4|
        r     f  t  
      t < 0
      t = max
      
    | | | 3| 4| |
          c   
    """
    def __init__(self, k: int):
        self.queue = [-1] * k
        self.Max = k - 1
        self.front = -1
        self.last = -1
        self.size = 0
    
    def insertFront(self, value: int) -> bool:
        if self.size > self.Max:
            return False
        if self.front == -1:
            self.front = 0
            self.last = 0
        elif self.front==0:
            self.front = self.Max
        else:
            self.front -= 1
        self.queue[self.front] = value
        self.size += 1
        return True
            
    def insertLast(self, value: int) -> bool:
        if self.size > self.Max:
            return False
        else:
            self.last += 1
            if self.last > self.Max:
                self.last = 0
            self.queue[self.last] = value
            self.size += 1
            if self.front == -1:
                self.front += 1
            return True
    def deleteFront(self) -> bool:
        if self.size > 0:
            
            self.front += 1
            if self.front > self.Max:
                self.front = 0
            self.size -= 1
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if self.size > 0:
            self.last -= 1
            if self.last < 0:
                self.last = self.Max
            self.size -= 1
            return True
        else:
            return False
    def getFront(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.front]
    def getRear(self) -> int:
        if self.size == 0:
            return -1
        return self.queue[self.last]
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.size > self.Max:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()