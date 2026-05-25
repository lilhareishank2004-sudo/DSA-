s="hello"
rev=""
for i in s:
    rev=i+rev
print(rev)


#Or:- 
j="welcome"
rv=""
for i in range(len(j)-1,-1,-1):
    rv=rv+j[i]
print(rv)

