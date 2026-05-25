no=int(input("Enter No"))   #123
n1=no%10   #3
no=no//10  #12
n2=no%10    #2
no=no//10   #1
n3=no%10    #1

res=n1+n2+n3
print(res)



print("____________________________________")
nn=456
nn1=nn%10  #6
nn=nn//10 #45
nn2=nn%10 #5
nn=nn//10  #4
nn3=nn%10   #4
res2=nn1+nn2+nn3
print(res)