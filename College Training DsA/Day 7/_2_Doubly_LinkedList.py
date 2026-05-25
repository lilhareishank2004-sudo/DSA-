import sys
class GetNode:
    def __init__(self):
        self.left=Node 
        self.right=Node 
        self.data=Node 
class LinkedList:
    def __init__(self):
        self.head=Node
    def push(self):
        data=int(input("Enter data: "))
        newNode=GetNode()
        newNode.data=data 
    def append(self):
        data = int(input("Enter Data: ")) 
        newNode= GetNode()
        newNode.data= data
        if self.head is None:
            self.head = newNode
            newNode.left=ptr 
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
                ptr.right=newNode
                newNode.left=ptr
        
    def traverse(self):
        if self.head is None:
            print( "list not present")
        else:
            prt=self.head