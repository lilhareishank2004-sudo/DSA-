class MergeSort:
    def merge(self,arr1,arr2):
       i=0
       j=0
       k=0
       arr3=[]
       while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
           arr3.append(arr1[i])
           i=i+1
           k=k+1
        else:
           arr3.append(arr2[j])
           j+=1
           k+=1
        
       while len(arr1)>i:
           arr3.append(arr1[i])
           i+=1
           k+=1
       while j<len(arr2):
           arr3.append(arr2[j])
           j+=1
           k+=1
       return arr3
if __name__=='__main__':
  obj=MergeSort()
  arr1=[1,3,5,7,9]
  arr2=[2,4,6,8,10]  
  ans=obj.merge(arr1,arr2)
  print(ans)