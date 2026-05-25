def selectionSort(arr):
 
 for i in range(len(arr)):
  min=arr[i]  
  for j in range(i+1,len(arr)-1):
   if min<arr[j]:
    min=arr[j]
    loc =j
  
  temp=arr[i]
  arr[i]=arr[loc]
  arr[loc]=temp
  

if __name__=='__main__':
 arr=[6,23,3,4,1,56,33]
 selectionSort(arr)
 print(arr)
 print(*arr)