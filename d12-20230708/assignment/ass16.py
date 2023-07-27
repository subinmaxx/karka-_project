gender=input("enter your gender(male or female) ")
firstname=input("enter your first name ")
secondname=input("enter your second name ")
age=int(input("enter your age "))
marriage=input("are you married"+firstname+ ("yes or no") )
if gender=="female":
   if marriage=="yes":
      print("i will call you as mrs "+firstname+secondname)
   elif marriage=="no":
      print("i will call you as ms "+firstname+secondname)
elif gender=="male":
   if marriage=="yes":
      print("i will call you as mr "+firstname+secondname)
   elif marriage=="no":
      print("i will call you as  "+firstname+secondname)
      
      

