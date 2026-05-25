#We are printing reversing three digit no without loop

no=int(input("enter no:"))
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10

res=n1*100+n2*10+n3*1
print(res)



#Accept 9 digit no and find sum of 1st and last digit(in 3 steps)

no=123456789

n1=no%10
n2=no//100000000
res=n1+n2
print(res) 