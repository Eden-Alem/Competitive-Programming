
class MyCircularDeque:

    def __init__(self, k: int):
        self.array = [None] * k
        self.l = 0
        self.r = 0
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if (self.count == len(self.array)):
            return False

        if (self.array[self.l] or self.array[self.l] == 0):
            self.l -= 1
            self.array[self.l % len(self.array)] = value  

        self.array[self.l % len(self.array)] = value   

        self.count += 1

        return True

    def insertLast(self, value: int) -> bool:
        if (self.count == len(self.array)):
            return False
        
        if (self.array[self.r] or self.array[self.r] == 0):
            self.r += 1
            self.array[self.r % len(self.array)] = value

        self.array[self.r % len(self.array)] = value

        self.count += 1

        return True

    def deleteFront(self) -> bool:
        if (self.count != 0):
            self.array[self.l] = None
            self.l += 1
            self.count -= 1
            if (self.count == 0): 
                self.l = 0
                self.r = 0
            return True

        return False        

    def deleteLast(self) -> bool:
        if (self.count != 0):
            self.array[self.r] = None
            self.r -= 1
            self.count -= 1
            if (self.count == 0): 
                self.l = 0
                self.r = 0
            return True

        return False        

    def getFront(self) -> int:
        if (self.count):
            return self.array[self.l]
        return -1        

    def getRear(self) -> int:
        if (self.count):
            return self.array[self.r]
        return -1        

    def isEmpty(self) -> bool:
        if (self.count == 0):
            return True
        return False        

    def isFull(self) -> bool:
        if (self.count == len(self.array)):
            return True
        return False
        


# [true,true,true,false,2,true,true,true,4]


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