#Array Rotation
arr=[1,2,3,4,5]
k=int(input("Enter how many time do you want to rotate: "))   
for i in range(k):
    temp=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
print(arr)