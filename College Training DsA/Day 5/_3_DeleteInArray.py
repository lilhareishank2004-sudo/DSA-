arr=[]
n=int(input("enter size: "))
for i in range(n):
    arr.append(int(input("Enter no:")))
loc=int(input("Enter location: "))
for i in range(loc+1,len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(arr)