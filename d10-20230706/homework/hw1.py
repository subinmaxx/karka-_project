list=[1,100,300,4]
large=list[0]
for i in range (1,len(list)):
    if large<list[i]:
        large=list[i]
print(large)