#accept values from user & print it

n=int(input("Enter size:"))
print("Enter list element: ")
arr=[]
for i in range(n):
    ele=int(input())
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i], end=" ") 
s=set(arr)
print(type(s))

