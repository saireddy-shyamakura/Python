import random
global guess = str(5)
r = random.randrange(1,101)
a = int(input("guess the number"))

def guessing():
    if a==r:
        result = 5- guess
        print("congratulations you won the correct number is "+str(r)+ "and you gessed it in" + result+ " chances")
        exit
    elif a>r:
        guess=guess-1
        print(" you gessed it higher")
        print(guess," chances left")
        guessing()
    elif a<r :
        print(" you gessed it lower")
        print(guess," chances left")
        guessing()
    else :
        print("please enter correct number")
        guessing()

guessing()