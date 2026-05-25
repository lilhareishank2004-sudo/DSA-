# ABCD
# EFGH
# IJKL
# MNOP

# A-65       a-97        0-48
# B-66       b=98        1-49
# C-67       c=99        2-50

n=65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end="\t")
        n=n+1
    print()