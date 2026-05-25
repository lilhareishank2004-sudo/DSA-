def bubbleSort(arr):
 
 for i in range(len(arr)-1):
  for j in range(len(arr)-1-i):
   if arr[j]>arr[j+1]:
    temp=arr[j]
    arr[j]=arr[j+1]
    arr[j+1]=temp
 
if __name__=='__main__':
 arr=[6,23,3,4,1,56,33]
 bubbleSort(arr)
 print(arr)
 print(*arr)