print("welcome to my computer quiz!")

playing_status = input("doy you want to play : ")
if playing_status.lower() == "no":
    quit()
print("okay lets play")
score = 0
print("you score is : ", score)

answer1 = input("what does the cpu stands for :")
if answer1.lower() == "central processing unit":
    print("you got it correct")
    score+=1
else :
    print("please check you answer! ")

answer2 = input("what does the ram stands for :")
if answer2.lower() == "random access memory":
    print("you got it correct")
    score+=1
else :
    print("please check you answer! ")

answer3 = input("what does the rom stands for :")
if answer3.lower() == "read only memory":
    print("you got it correct")
    score+=1
else :
    print("please check you answer! ")

answer4 = input("what does the mu stands for :")
if answer4.lower() == "memory unit":
    print("you got it correct")
    score+=1
else :
    print("please check you answer! ")

answer5 = input("what does the ups stands for :")
if answer5.lower() == "unified power supply":
    print("you got it correct")
    score+=1
else :
    print("please check you answer! ")

print("your total score is : ", score)
print("thanks for playing")