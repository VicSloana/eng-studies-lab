#mid15

game = ["paper", "rock", "paper", "scissor", "rock", "rock", "scissor", "paper"]
for item in game:
    if item == "scissor":
        print("scissor beats paper")
    elif item == "paper":
        print("paper eats rock")
    elif item == "rock":
        print("rock hits scissor")
