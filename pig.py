import random

def roll():
    min_value = 1
    max_value = 6
    roll=random.randint(min_value,max_value)
    return roll

while True :
    players = input("enter the number of players (2-4) : ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4 :
            break
        else:
            print("please enter any number between 2 to  4")
    else :
        print("please enter a number")

print("the number of players are : ",players)

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score :
    for players_idx in range(players):
        print("\n player",players_idx+1, "turn just started")
        print("your total score is :",player_scores[players_idx],"\n")
        current_score = 0

        while True :
            should_roll = input("would you like to roll (y/n) ?")
            if should_roll.lower() != "y" :
                break

            value= roll()
            if value == 1:
                print("you rolled a one")
                current_score = 0
            else :
                current_score += value
                print("you rolled :",value)

            print("your current score is :",current_score)

    player_scores[players_idx]+= current_score
    print("your total score is :" ,player_scores[players_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("player ", winning_idx+1," is the winner with the socre of: ",max_score)

