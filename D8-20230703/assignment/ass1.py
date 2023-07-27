def cal(a,b,c):
    if b=='+':
      return a+c
    elif b=='-':
      return a-c
    elif b=='*':
      return a*c
    elif b=='/':
      return a/c
    elif b=='%':
      return a%c
    elif b=='**':
      return a**c
      
   return 0
a=int(input("enter the first nunmber:"))
b=input("enter the operator:")
c=int(input("enter the third number:"))
z=cal(a,b,c)
print(z)

