import random

user_wins = 0
computer_wins = 0
options = [ "rock","paper","scissors"]

while True :
    user_input = input("please enter \n Rock \n Paper \n Scissors \n q to quit \n").lower()
    if user_input == "q":
        break

    if user_input not in options :
        print("please enter the correct option : ")
        continue

    random_number = random.randint(0,2)

    computer_input = options[random_number]
    print("computer picked "+ computer_input+"." )

    if user_input=="rock" and computer_input == "scissors":
        print("you won!")
        user_wins +=1
    elif user_input=="paper" and computer_input == "rock":
        print("you won!")
        user_wins +=1
    elif user_input=="scissors" and computer_input == "paper":
        print("you won!")
        user_wins +=1
    else:
        print("you lost!")
        computer_wins +=1


print("you won",user_wins,"times")
print("you won",computer_wins,"times")
print("goodbye")

