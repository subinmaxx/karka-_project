# space boxing
weight=int(input("enter the current weight on the earth"))
print("\n")
print("i have the information of the following planet")
print("1.venus/t 2.mars/t 3.jupiter/t 4.saturn\t 5.uranus/t 6.neptune/t")
mark=int(input("which planet you are visiting"))
if mark==1:
    a=weight*0.78
    print("your weight on venus ",a)
if mark==2:
    a=weight*0.39
    print(" your weight on mars",a)
if mark==3:
    a=weight*2.65
    print(" your weight on jupiter",a)
if mark==4:
    a=weight*1.17
    print(" your weight on saturn",a)
if mark==5:
    a=weight*1.05
    print("enter your weight on uranus",a)
elif mark==6:
    a=weight*1.23
    print("enter your weight on neptune",a)

