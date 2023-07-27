def century(cricketrs):
    century_count =0
    for i in range(len(cricketrs)):
        if cricketrs[i]["centuries"]:
            century_count_+=1
    return century_count

def hatrick(cricketrs):
    hatrick_count=0
    for i in range(len(cricketrs)):
        if cricketrs[i["hatricks"]]>5:
            hatrick_count+=1
    return hatrick_count

def topper(cricketrs):
    top=0
    topplayer=""
    for i in range(len(cricketrs)):
      for j in range(len(cricketrs[i]["bestscore"])):
          if cricketrs [i]["bestscore"][j]>top:
              top=cricketrs[i]["bestscore"][j]
              topplayer=cricketrs[i]["name"]
    return top,topplayer
cricketers=[{"name":"sehwag",
             "country":"india",
             "centuries":30,
             "half_centuries":47,
             "wickets taken":129,
             "hatricks":2,
             "top_score":219}

             {"name":"stevesmith",
              "country":"australia"
              "centuries":40
              "half_centuries":62
              "wickets _taken":86
              "hatricks":2
              "top_score":160}
              
              {"name":"chrisgayle",
               "country":"westindies",
               "centuries":28,
               "half_centuries":65,
               "wiclets_taken":123,
               "hatricks":4,
               "topscore":229}
               
               {"name":"trentboult",
               "country":"newsealand",
               "centuries":0,
               "half_centuries":5,
               "wiclets_taken":223,
               "hatricks":5,
               "topscore":78}

                {"name":"duplesis",
               "country":"southafrica",
               "centuries":22,
               "half_centuries":54,
               "wiclets_taken":0,
               "hatricks":0,
               "topscore":167}
               
               ]
century_count=century(cricketers)
hatrick_count=hatrick(cricketers)
top_score,cricketer_name=topper(cricketers)

print("numberof players score more than 10 centuries in the list is:{century_count})

        