# list=[10,20,30,40,50]
# total=0
# for i in list:
#     total=total+i
# average=total/len(list)
# print(average)


marks=[15,25,35,45,55]
total=0
enum_marks=enumerate(marks)
print(type(enum_marks ))
for i,mark in enum_marks:
    print("entering iteration process for item++ :"+str(i))
    print("before sum",total)
    total_marks=total_marks+mark
    print("after sum",total_marks)
    print("exiting iteration process for item++ :"+str(i))
    print("/n")



