no=int(input("Enter the no"))
sum=0
save=no
count=0
#count logic
while no>0:
    no=no//10
    count=count+1

no=save
while no>0:
    rem=no%10
    sum=sum+(rem**count)
    no=no//10
if sum==save:
    print("The number is Armstrom")
else :
    print("The Number is not Armstrom") 