print("think of something and i will try to guess it")
ques1=input("does it belong inside or outside or both")
ques2=input("is it a alive or not ")

if ques1=="inside" and ques2=="alive":
    print("it is a living inside and it is a living thing(houseplant)")
if ques1=="outside" and ques2=="alive":
    print("it is living outside and it is a living thing(bison)")
if ques1=="both" and ques2=="alive":
    print("it is living both sides and it is a living thing(dog)")

if ques1=="inside" and ques2=="not alive":
    print("it is living inside and not alive(showe curtain)")
if ques1=="outside" and ques2=="not alive":
    print("it is living outside and not alive(billboard)")
if ques1=="both" and ques2=="not alive":
    print("it is living both sides and non not alive(cell phone)")