class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
        return

    def push(self, val: int) -> None:
        self.stack.append(val)
        try:
            if val <= self.mins[-1]:
                self.mins.append(val)
        except IndexError:
            self.mins.append(val)
        return

    def pop(self) -> None:
        val = self.stack.pop()
        if self.mins[-1] == val:
            self.mins.pop()
        return 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
