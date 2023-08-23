

my_resume={"Name" :"subin.s",
            "E-mail":"subinram18@gmail.com",
            "Mobile-No":9360363507,
            "Soft skills" : "coding",
            "Hard skills" : ["planting"],
            "Educational Qualification" :[{"SSLC-2014","slb govt high school"},
                                          {"HSC-2016","Slb govt higher seondry school"},
                                          {"B.Sc-2023","vins christian college of engineering"}],
            "Project" : "Android Development-compose input",
            "Experience":[{"company name":"amazon","role":"developer","duration":"3"},
                          {"company name":"clovion","role":"back end developer","duration":"2"},
                          {"company name":"TCS","role":"developer","duration":"4"},
                          ],
            "Hobbies" : ["planting","hearing music","drawing"],
            "Personal Details": {"Fathers name" :"subbiah",
                                 "Father's Occupation" :"driver",
                                 "Languages Known" :["Tamil","English"],
                                 "DOB" :"18-07-1998",
                                 "Genter":"Male",
                                 "Martial Status" :"Not Married",
                                 "Address" : {"Door No":"4/22b",
                                              "Street Name" :"sudalai madan swamy compound","east peruvilai"
                                              "District" :"kanyakumari",
                                              "pin code": 629003
                                             }
                                    } 
            }
district=my_resume["Personal Details"]["Address"]["District"]

for resume in my_resume["Hobbies"]:
    print(resume)
   
for lang in my_resume["Personal Details"]["Languages Known"]:
    print(lang)
   
for hard in my_resume["Hard skills"]:
    print(hard)
   
for edu in my_resume["Educational Qualification"]:
    print(edu)
