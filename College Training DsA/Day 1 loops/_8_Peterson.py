#peterson Problem
# no=145=!1+!4+!5

no=145
fact=1
sum=0
save=no
while no>0:
    rem=no%10
    fact=1
    while rem>0:    
        
        fact=fact*rem
        rem=rem-1
    sum=sum+fact
    no=no//10
print(sum)
if sum==save:
    pass