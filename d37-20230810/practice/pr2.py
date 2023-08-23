a=[1,2,1,3,2,6,7]
count=0
for i in a:
    for j in a:
        if i==j:
            count+=1
    if count<2:
        print(i)
    count=0