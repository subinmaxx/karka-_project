def eligible(passout):
    if passout>2021:
        return"eligible"
    else:
        return"not eligible"
print (eligible(passout))
passout=int(input("enter the passout year"))