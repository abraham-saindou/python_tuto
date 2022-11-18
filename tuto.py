import random

def get_choices():

    player_choice = input("Enter a choice (rock, paper, scissors): ")
    
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    
    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie !"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors ! You win !"
        else: 
            return "Paper fold rock ! You lost."
    elif player == "paper":
        if computer == "rock":
            return "Paper fold rock ! You win !"
        else: 
            return "Paper is cut by scissors ! You lost."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper ! You win !"
        else: 
            return "Scissors is destroyed by rock ! You lost."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

