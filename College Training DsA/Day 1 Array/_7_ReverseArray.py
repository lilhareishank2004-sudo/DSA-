arr=[1,2,3,4,5,6,7,8,9]
j=len(arr)-1
for i in range(len(arr)//2):    #because we have to swap element till middle of the array
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i=i+1
    j=j-1
print(arr)