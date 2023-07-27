list=[12,34,5,4,67,89,32,45,67,43,66,78,32]
list2=[]
odd=0
even=0
for i in list:
    if i%2!=0:
        odd = odd+1
    else:
        even = even+1
print(odd,"odd numbers in the list.")
print(even,"even numbers in the list")
