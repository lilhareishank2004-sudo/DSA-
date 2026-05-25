#Queue: follows FIFO(First in First Out)

import sys

class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=-1
        self.front=0
        self.CAPACITY=5
    def isfull(self):
        if self.rear==self.CAPACITY-1:
            return True 
        else:
            return False
    def insert(self,ele):
        if self.isfull():
            print("queue is full")
        else:
            self.rear=self.rear+1
            self.queue[self.rear]=ele
            print("ele is inserted")    
    def traverse(self):
        pass
    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            print("queue is Emoty")
        else:
            print(self.queue[self.rear])
    def delete(self):
        pass
        
   
class Stacks:
    def push(self):
        pass
    def pop (self):
        pass
    def traverse(self):
        pass
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            ele=self.queue[self.rear]
            for i in range(1,raare+1):
                queue[i+1]=queue[i]
            self.rear=self.rear-1
            
if __name__=='__main__':
    obj1=Queue()
    obj2=Stacks()
    for i in range(obj1.CAPACITY):
        ele=int(input("Enter element"))
        obj1.insert(ele)
for x in ranage(10):
    ele=obj1.delete()
    push(ele)