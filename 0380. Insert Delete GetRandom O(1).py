class RandomizedSet:

    def __init__(self):
        # the hashmap's [key: value] pairs will store [value: index] info
        # where the index is the value's location in the array
        self.hash = {}
        self.arr = [] 

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        self.arr.append(val)
        self.hash[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False

        # swap last value in array with value to be removed
        temp = self.arr[-1]
        self.arr[-1] = val
        self.arr[self.hash[val]] = temp
        self.arr.pop()

        # update hashmap to reflect value position change
        self.hash[temp] = self.hash[val]
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
