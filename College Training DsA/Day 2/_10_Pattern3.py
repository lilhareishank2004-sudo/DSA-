# 1
# 22
# 333
# 4444

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("________In Alphabate_____________")

n=65
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(n),end=" ")
        n=n+1
    print()
