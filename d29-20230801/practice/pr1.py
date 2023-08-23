details=[{"naame":"subin",
          "email":"subinram18@gmail.com",
          "password":"vins123",
          "hobbies":["cricket","football","volleyball"],
          "friends_list":["ajith","vijay"]},

           {"naame":"dhanush",
          "email":"kunush18@gmail.com",
          "password":"kunush123",
          "hobbies":"playing_foot_ball",
          "friends_list":"ajith,vijay",},
          
          {"naame":"sree",
          "email":"sree18@gmail.com",
          "password":"sree123",
          "hobbies":"playing_flying",}
#         
          ]
email=input("enter your email ")
password=(input("enter your password"))
for i in details:
    if i['email']==email and i['password']==password:
        print(i["naame"],("present"))
        i.update({"login":"true"})
        print(i)
        print("hobbies",i["hobbies"])
        print("friends_list",i["friends_list"])
    else:  
       print("absent")


