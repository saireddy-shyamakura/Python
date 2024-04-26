import random
print("welcome to number guessing game")
print("please enter your first guess you will have a total of 5 chances")
number : int = int(input(" "))
random_number : int  = random.randrange(1,11)

while number!=random_number :
    if number < random_number :
        print("you guessed it lower try again")
        number : int = int(input(" "))
    elif number > random_number :
        print("you guessed it higher")
        number : int = int(input(" "))
    else :
        print(" please enter the correct number")
        number : int = int(input(" "))

if(number==random_number):
    print("you guessed it correctly the number is :" + str(random_number))