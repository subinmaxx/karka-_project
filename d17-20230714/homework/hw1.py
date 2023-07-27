def  student(students):
    for i in range(len(students)):
        print("i am ",students[i]["name"],"-i am",students[i]["age"],",and i am from",students[i]["place"])
def above_21(students):   
    for info in students: 
        if info["age"]>21:
            print("i am",info["name"],",and i am from",info["place"])


students=[{"name":"anish","age":24,"place":"mylady"},
          {"name":"navin","age":25,"place":"puthery"},
          {"name":"suthan","age":20,"place":"nagercoil"},
          {"name":"arun","age":17,"place":"peruvilai"}]
student(students)
above_21(students)
