# Eg: 2025 is tech number
# 2025=20   25
#       20+25=45
#       45*45=2025



no=int(input("Enter number:"))
count=0
save=no
while no>0:
    no=no//10
    count=count+1
print(count)
if count%2==0:
    count=count/2
    num1=save%10**count
    no=save//10**count

    sum=num1+no
    mul=sum*sum
    print(num1,"+",no,"=",sum)
    print(sum,"*",sum,"=",mul)

else: 
    print("no tech number")