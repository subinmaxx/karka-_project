# password
p=input()
print(len(p))
if len(p)<6:
        print("weak password")
elif len(p)>=6 and len(p)<=10:
        print("moderate")
elif len(p)>=11 and len(p)<=15:
        print("strong")
elif len(p)>15:
        print("very strong")
    