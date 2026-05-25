#function with parameter
def add(a,b):
    res=a+b
    print("Addition :",res)

def sub(c,d):
    res2=c-d
    print("Substraction:  ",res2)

if __name__=='__main__':
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b: "))
    add(a,b)
    c=int(input("Enter c: "))
    d=int(input("Enter d: "))
    sub(c,d)
