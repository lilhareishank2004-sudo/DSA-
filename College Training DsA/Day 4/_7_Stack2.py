import sys

class Stacks:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.CAPACITY=5
    def isFull(self):
        if self.top==self.CAPACUITY-1:
            return True
        else:
            return False
    def push(self,ele):
        if self.isFull():
            print("stack is full")
        else:
            self.top=self.top+1
            self.stack.append(ele)
            print(ele,"is pushed")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
    def pop(self):
         obj.pop()
