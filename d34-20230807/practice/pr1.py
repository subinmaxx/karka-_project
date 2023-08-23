# for loop  54321,4321,321,21,1
# for i in range (5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
    
# n=5
# for i in range(5):
#     for j in range(n,0,-1):
#         print(j,end="")
#     n=n-1  
#     print()

n=int(input())
for i in range(n):
  for j in range(n,0,-1):
    print(j,end="")
  n=n-1
  print()