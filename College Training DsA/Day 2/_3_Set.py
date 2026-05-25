#SET: Duplicate are not allowed, unique value as a single entity . Set are repereset in {}, tupel is represent in (),
# and list is represent in []

s=set()
print(s)
print(type(s))

s={9,1,2,3,4,5,6,7,8,1,2,3,4}
print(s)   #will remove duplicate value

arr=[1,2,3,4,5,3,2,4,3,2,4,4]
s=set(arr)
arr=list(s)
print(arr)