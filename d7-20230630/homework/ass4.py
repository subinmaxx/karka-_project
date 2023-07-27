a=int(input("enter the amount of a:"))
b=int(input("enter the amount of b:"))
c=int(input("enter the amount of c:"))
d=int(input("enter the amount of e:"))
total=a+b+c+d
if total>500 and total<1000:
    print("you have owned silver token")
elif(total>1000):
    print("you have owned goldern token")
else:
    print("you have no token")
    