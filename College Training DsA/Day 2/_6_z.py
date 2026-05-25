#sum of even number and odd number

li=int(input("Enter size: "))
arr=[]
sum1=0
sum2=0
for i in range(li):
    ele=int(input())
    if ele%2==0:
        sum1=sum1+ele
    else:
        sum2=sum2+ele
print("Sum of even no:",sum1)
print("Sum of odd no: ",sum2)
