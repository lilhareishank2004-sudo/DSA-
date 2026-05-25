#Accept moobile number check that mobile no is 10 digit only. Check number is valid in india or not(6,7,8,9)

no=int(input("Enter mobile number: "))
if no.isdigit():
    if len(no)==10:
        if no.startwith(6) or no.startwith(7):
            pass
        else:
            pass
    else:
        pass
else:
    print("pls enter no is digit format only")
