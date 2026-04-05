class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = []

    def push(self, val: int) -> None:
        if(len(self.min_num) == 0):
            self.min_num.append(val)
        elif (val <= self.min_num[-1]):
            self.min_num.append(val)
        else:
            self.min_num.append(self.min_num[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.min_num.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]

