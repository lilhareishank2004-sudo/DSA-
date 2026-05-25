# sum of number means:  we have no=123
#  result will be 1+2+3  //using loops

no=int(input("Enter no:"))
sum=0
while no>0:
    rem=no%10
    sum=sum+rem
    no=no//10
print(sum)