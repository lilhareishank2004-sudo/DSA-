arr=[-1,2,-3,4,5,-6]
neg=[]
pos=[]
for i in range(len(arr)):
    if arr[i]<0:
        neg.append(arr[i])
    else :
        pos.append(arr[i])
res=[]
for i in range(len(neg)):
    res.append(neg[i])
    res.append(pos[i])
print(res)
