# # row=5
# # column=5
# a=input()
# print(a)
# # for i in a
    
# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print("")
# a=int(input("enter your number : "))
# for i in range(a):
    # print('*'*a)

# a=int(input("enter the number"))
# for i in range(a):
#     print(a)

# n=5
# for i in range(n):
#     for j in range(n):
#         print("",end="")
#     print("")           
a=int(input("enter your number : "))
for i in range(1,(a*a)+1):
    print(i,end=" ")
    if i%a==0:
      print("")  

a=int(input("enter your number :"))
for i in 