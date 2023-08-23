# find the largest word
# a=("hi i am subin from nagercoil")
# a=a.split()
# ans=a[0]
# for i in a:
#     if len(ans)<len(i):
#         ans=i
# print(ans)

a=("hi i am subin from nagercoil")+''
str=''
ans=''
for i in a:
    if i!='':
        str+=i
    elif len(ans)<len(str):
        ans=str
        str=''
    else:
        str=''
print(ans)



    
