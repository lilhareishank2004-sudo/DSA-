# Linear Search     de

def linear_Search(n,arr,target):
    flag=False
    
    for i in range(n):
        if arr[i]!=target:
            pass
        else:
            flag=True
            loc=i;
    if flag==True:
        print("Index:",loc)
        
    
        
      

if __name__== '__main__':
    n=int(input("Enter size: "))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    targer=int(input("Enter no which is to search:"))
    