import random
 
def game():
    print("Welcome to the Rock, Paper, Scissor Game")

     
    choices = ["rock", "paper", "scissor"]
    user_choice = input("Enter rock, paper or scissor: ").strip().lower()

    if user_choice not in choices:
        print(" Invalid choice! Please enter 'rock', 'paper', or 'scissor'.")
        return   
    computer_choice = random.choice(choices)
    print(f"You chose: {user_choice}")  
    print(f"Computer chose: {computer_choice}")


    if user_choice == computer_choice:
        print("It's a tie!")
    elif( user_choice == "rock" and computer_choice == "scissor") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissor" and computer_choice == "paper"):
        print("You won!")

    else:
        print("You lost!")
game()