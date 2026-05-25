#accept values grom user find sum of list

li=int(input("Enter the size of list: "))
arr=[]
sum=0
for i in range(li):
    ele=int(input())
    arr.append(ele)
print("List",arr)

for j in range(len(arr)):
    sum=sum+arr[j]

print("Total sum of the list",sum)


