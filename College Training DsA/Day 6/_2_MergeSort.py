# the idea of merge sort is:
# Divide the list into smaller parts
# Sort each smaller part 
# Merge them back together
class MergeSort:
    def merge(self,arr):
        arr3=[]
        if len(arr)>1:
            mid=len(arr)//2
            arr1=arr[:mid]
            arr2=arr[mid:]
            self.merge(arr1)
            self.merge(arr2)
            i=0
            j=0
            k=0
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:     #if you wanted to arrange in ddecending use--> arr1[i]>arr[j]
                    arr[k]=arr1[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2[j]
                    j+=1
                    k+=1
            while i<len(arr1):
                arr[k]=arr1[i]
                i+=1
                k+=1
            while j<len(arr2):
                arr[k]=arr2[j]
                j+=1
                k+=1

if __name__=='__main__':
    obj=MergeSort()
    arr=[1,23,5,3,8,9,2]
    obj.merge(arr)
    print(arr)