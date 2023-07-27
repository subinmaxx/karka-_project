# age message
name=input("enter the name")
age=int(input("ok,"+name+",how old are you"))
if age<16:
    print("you cant able to drive")
elif age==16 or age==17:
    print("you can able to drive ,but not able to vote")
elif age>=18 and age<= 24:
    print("you can vote,but not able to rent a car")
elif age>=25:
    print("you can do pretty do anything")

