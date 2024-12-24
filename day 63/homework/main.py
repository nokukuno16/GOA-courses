def game(player_1, player_2,):
    if player_1 == "rock" and player_2 == "scissors" or player_1 == "scissors" and player_2 == "paper" or player_1 == "paper" and player_2 == "rock":
        print("player one wins") 
    else:
        print("player two wins")

game("scissors", "paper")