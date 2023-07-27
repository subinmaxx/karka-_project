consumer_data={"consumer_name":"user","eb_reading":[1100,1200,1350,1650,2050]}
total=0
resilt=[]
for i in range(1,len(consumer_data["eb_reading"])):
    diff=consumer_data["eb_reading"][i]-consumer_data["eb_reading"][i-1]
    rs=0
    if diff<100:
        print()
