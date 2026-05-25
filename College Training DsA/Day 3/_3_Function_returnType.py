#function with parameter with return type.
def add(a,b):
    res=a+b 
    
    return res    #we cannot return multiple value in c++ and java but we can do it in python.

if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("enter b: "))
    r=add(a,b)
    print("addition is ",r)