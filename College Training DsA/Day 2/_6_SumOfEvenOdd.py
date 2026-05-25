li=int(input("Enter size: "))
arr1=[]
odd=[]
even=[]
sum1=0
sum2=0
for i in range(li):
    ele=int(input())
    arr1.append(ele)
    if ele%2==0:
        even.append(ele)
    else:
        odd.append(ele)
print("list:",arr1)

for j in range(len(even)):
    sum1=sum1+even[j]
for k in range(len(odd)):    
    sum2=sum2+odd[j]
print("odd",sum1)
print("even:",sum2)

