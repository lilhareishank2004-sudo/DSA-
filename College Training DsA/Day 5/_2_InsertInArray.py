arr=[]
n=int(input("Enter size: "))
for i in range(n):
    arr.append(int(input("Enter no: ")))
key=int(input("Enter key element whis is to be inserted: "))
loc=int(input("Enter location :" ))
arr.append(0)  # it is used to add 0 in the end of the list.

for i in range(len(arr)-2,loc-1,-1):
    arr[i+1]=arr[i]
arr[loc]=key

print(arr)