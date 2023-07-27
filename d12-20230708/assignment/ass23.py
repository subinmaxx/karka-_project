# fizz buzz
numb=range(1,101)
for i in numb:
    if i%3==0 and i%5==0:
        print(i,"FIZZBUZZ")
    if i%3==0:
        print(i,"FIZZ")
    if i%5==0:
        print(i,"BUZZ")


