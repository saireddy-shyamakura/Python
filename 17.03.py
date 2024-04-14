person1 = "sai"
person2 = "bye"
person3 = "developer"
person4 = "ram"
person = ''
sai = " reddy"

for a in range(1,5) :
    txt = 'person'+str(a)
    b= "sai"
    print(txt,'=',locals()[txt])
    print(locals()[b])