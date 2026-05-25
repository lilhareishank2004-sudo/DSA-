#Stack  follow FILO(First in last out) or LIFO(Last in first out)

import sys 
class Stacks:
    def push(self):
        pass
    def pop (self):
        pass
    def traverse(self):
        pass
    def peek(self):
        pass

if __name__=='__main__':
    obj=Stacks()
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")
        ch= int(input("Select any choice"))
        if ch==1:
            obj.push()
        elif ch==2:
            obj.pop()
        elif ch==3:
            obj.treaverse()
        elif ch==4:
            obj.peek()
        elif ch==0:
            sys.exit(0) 