class MinStack:

    def __init__(self):
        self.mainstack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.mainstack.append(val)

        # only push when the new value is smaller than the previous one
        # for first time we just push
        # new val is smaller than the old val
        # 0 < 1
        #  -2 -2 -3 -3
        #  -2 -3
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self) -> None:
        top = self.mainstack.pop()
        if top == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self) -> int:
        return self.mainstack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        

