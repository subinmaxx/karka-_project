# electricity bill
consumer_data={"consumer_name":"user",
               "eb_reading":[1100,1200,1350,1650,2050]}
total=0
output=[]
initial=0
for i in range(1,len(consumer_data["eb_reading"])):
    empty={}
    rs=0
    diff=consumer_data["eb_reading"][i]-consumer_data["eb_reading"][i-1]
    if diff<100:
        rs=0
    elif diff>=100 and diff<200 :
        rs=diff*2
    elif diff >=200 and diff<500:
        rs=diff*5
    elif diff >=500 and diff<1000:
        rs=diff*10
    elif diff >=1000:
        rs=diff*14
    
    initial+=1
    empty["month"]=initial
    empty["unit consumed"]=diff
    empty["bill_amount"]=rs
    total+=rs
    output.append(empty)
print(output)
print("total",total)

file=open("/home/subin/maxx/ebreading.txt","w")
file.write(str(output))
file.close()
