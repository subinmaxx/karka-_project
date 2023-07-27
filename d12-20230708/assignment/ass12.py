#  little quiz
print("are you ready for the quiz")
print("ok lets play")
score=0
print("which is the capital 0f india ?")
choice=int(input("1.tamilnadu\t 2.delhi\t 3.mumbai\t 4.kerala"))
if choice==2:
    print("the capital of india is delhi")
    score+=1
else:
    print("thats not correct")

print("can you store the value ,cat, in a variable of type int ?")
choice1=int(input("1.yes\t 2.no"))
if choice1==1:
    print("cat is a string ,int can only used in numbers")
else:
    print("option 2 is correct")
    score+=1
print("what is the result of 9+6/3 ?")
choice2=int(input("1.5\t 2.11\t 3.15/3\t"))
if choice2==1:
    print("thats correct")
    score+=1
else:
    print("thats not correct")
print("yourscore is",score)
         
            