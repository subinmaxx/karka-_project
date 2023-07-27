year=int(input("enter the year"))
if((year%4==0)and
(year%100!=0)or
(year%400==0)):
    print("given year is a leapyear")
else:
    print("given year is not leapyear")
print(year%4==0,year%100!=0,year%400==0)