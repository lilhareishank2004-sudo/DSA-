#WAP to accept cost price from user and ask whether from user and ask whether the user is student or not
cp=int(input("Enter Cost Price:"))

st=str(input("Are you Student y/n"))

if st=="y":
    print("the person is student")
    discount=cp*20/100
    
else:
    print("The Person is not student")
    discount=cp*10/100

net=cp-discount
print(net)