# how old are u ifelse
name=input("whats your name")
age=int(input("ok"+name+". how old are you"))
if age<16:
    print("you are not eligible to drive")
elif age<18:
    print("you are not eligible to vote")
elif age<25:
    print("you are not eligible to rent a car")
elif age>=25:
    print("you can do anything thats legal")

