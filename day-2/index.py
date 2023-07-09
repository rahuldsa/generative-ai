import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
        if user_choice.lower() in ["rock", "paper", "scissors"]:
            return user_choice.lower()
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        print("--------------------")
        print("Rock, Paper, Scissors")
        print("--------------------")

        user_choice = get_user_choice()
        if user_choice == "quit":
            break

        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "draw":
            print("It's a draw!")
            draws += 1
        elif winner == "user":
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

        print(f"Score: User {user_wins} - Computer {computer_wins} - Draws {draws}")

    print("--------------------")
    print("Thanks for playing!")
    print(f"Final score: User {user_wins} - Computer {computer_wins} - Draws {draws}")

play_game()
