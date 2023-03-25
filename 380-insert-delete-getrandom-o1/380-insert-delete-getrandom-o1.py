class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.array = []
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        
        self.array.append(val)
        self.hashMap[val] = self.count
        self.count += 1
        
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        
        index = self.hashMap[val]
        last_value = self.array[-1]
        
        self.array[index] = last_value
        self.array.pop()
        
        self.hashMap[last_value] = index
        del self.hashMap[val]
        self.count -= 1
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()