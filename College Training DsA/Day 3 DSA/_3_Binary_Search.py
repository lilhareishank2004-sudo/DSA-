def Binary_Search(n,arr,target):
    flag=False
    ll=0
    ul=n-1
    loc=0
    while ll<ul:
        mid=(ll+ul)//2
        if target==arr[mid]:
            flag=True
            loc=mid
            break;
        elif target<arr[mid]:
            ul=mid-1
        else:
            ll=mid+1
    return loc

if __name__=='__main__':
    n=int(input("Enter size: "))
    print("Enter element ofd array: ")
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    target=int(input("enter element to search: "))
    res=Binary_Search(n,arr,target)
    print("Element lies in index",res)
    