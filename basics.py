# import datetime
# mynow=datetime.datetime.now()
# print(mynow)
# myname="rrr"
# mynum=69
# print(myname,mynum)
stu_grad=[9.1,8.8,7.5]
stu_gra={"Bit": 8.1,"logan": 3.9,"argon": 7.8}
x=sum(stu_gra.values())
y=len(stu_gra)
# print(x/y)
input ("Enter myno.")

def mean(value):
    if type(value)==dict:
        amean= sum(value.values())/len(value)
    else:
        amean=sum(value)/len(value)
    return amean

print(mean(stu_gra)) 
print (mean(stu_grad))  

