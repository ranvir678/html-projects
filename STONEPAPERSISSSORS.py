import random
random_number=random.randint(1,3)

def game():
    computer_turn=""
    player_turn=input("Snake Water or Gun: ")
    if random_number==1:
        computer_turn="Snake"
    elif random_number==2:
        computer_turn="Water"
    else:
        computer_turn="Gun"
    if computer_turn==player_turn:
        print("This is a tie 🤐")
    elif computer_turn=="Gun":
        if player_turn=="Snake":
            print("You Lose 😁")
        elif player_turn=="Water":
            print("You won 😎")
    elif computer_turn=="Water":
        if player_turn=="Gun":
            print("You Lose 😁")
        elif player_turn=="Snake":
            print("You won 😎")
    elif computer_turn=="Snake":
        if player_turn=="Gun":
            print("You Won 😎 ")
        elif player_turn=="Water":
            print("You lose 😁")
    print(f"Since computer's turn is {computer_turn} ")
 

game()