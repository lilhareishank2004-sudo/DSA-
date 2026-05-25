# A function is a self-contained block of code used to perform a specific task and return a value.

#Syntax:
# def function():
#     pass

def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a+b
    print("Addition: ",res)
# add()               #this is main function

if __name__=="__main__":                  #this is also main function. We can call function in main function in both the way
    add()


def sub():
    c=int(input("Enter c: "))
    d=int(input("Enter d: "))
    res2=c-d 
    print("Substraction: ",res2)
if __name__ =='__main__':
    sub()