no=int(input("Enter No:"))
rev=0
n1=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10

if rev==n1:
    print("The no is palindrom")

else:
    print("The No is not palindrom")

