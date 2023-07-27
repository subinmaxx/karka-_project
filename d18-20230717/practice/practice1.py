def name(students):
    for student in students:
        total=sum(student["sslc".values()])
        average=total/len(student["sslc"].values())
        if average>90:
            print("you are eligible to get maths biology")
        elif average>85:
            print("you are eligible to get computer science")
        elif average>75 and students["sslc"]["maths"]>=98:
            print("you are eligible to get maths biology")
        elif average>70 and students["sslc"]["maths"]>=98:
            print("you are eligible to get computerscience")
        else:
            print("choose any group nexcept maths biology and computer sience")


students=[
          {
            "name":"subin",
           "place":"peruvilai",
           "sslc":{
               "tamil":83,
               "english":78,
               "maths":72,
               "science":92,
               "social":95}
          },
         
           { "name":"robin",
           "place":"thirunelveli",
           "sslc":{
               "tamil":95,
               "english":85,
               "maths":95,
               "science":92,
               "social":95 }
           
          }
          

]
        



print("average")