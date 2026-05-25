# ****
# ***
# **
# *

for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


print("___________________")
#  ****
#   ***
#    **
#     *
sp=0
for i in range(4,0,-1):
    for j in range(sp):
        print(" ",end=" ")
    for x in range(1,i+1):
        print("* ",end="")
    print()
    sp=sp+1