def add(a,b):
    res=a+b 
    res2=a-b
    res3=a*b
    return res,res2,res3   #we cannot return multiple value in c++ and java but we can do it in python.

if __name__=='__main__':
    a=int(input("Enter a: "))
    b=int(input("enter b: "))
    r,r2,r3=add(a,b)
    print("addition is ",r)
    print("Substraction: ",r2)
    print("Multiplication: ",r3)