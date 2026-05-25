no=456
rev=0
print("Before reverse: ",no)
while no>0:
  rem=no%10
  rev=rev*10+rem
  no=no//10
print("After Reverse: ",rev)
