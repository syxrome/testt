import random

input("Welcome to AI Rock, Paper, Scissors! Press Enter to start.")
print()

user_wins = 0
computer_wins = 0

choices = ["rock", "paper", "scissors"]
user_history = {"rock": 0, "paper": 0, "scissors": 0}

while True:
    total_games = sum(user_history.values())
    
    if total_games < 3:
        cpu_choice = random.choice(choices)
    else:
        predicted_user_move = max(user_history, key=user_history.get)
        
        if predicted_user_move == "rock":
            cpu_choice = "paper"
        elif predicted_user_move == "paper":
            cpu_choice = "scissors"
        else:
            cpu_choice = "rock"

    user_choice = input("Rock, Paper, or Scissors? ").lower()
    while user_choice not in choices:
        user_choice = input("That is not a valid choice. Please try again: ").lower()

    user_history[user_choice] += 1

    print()
    print("Your choice:", user_choice)
    print("Computer's choice (AI Predicted):", cpu_choice)
    print()

    if user_choice == cpu_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and cpu_choice == 'scissors') or \
         (user_choice == 'paper' and cpu_choice == 'rock') or \
         (user_choice == 'scissors' and cpu_choice == 'paper'):
        print("You win!")
        user_wins += 1
    else:
        print("You lose!")
        computer_wins += 1

    print()
    print("You have "+str(user_wins)+" wins")
    print("The computer has "+str(computer_wins)+" wins")
    print()

    repeat = input("Play again? (Y/N) ").lower()
    while repeat not in ['y', 'n']:
        repeat = input("That is not a valid choice. Please try again: ").lower()

    if repeat == 'n':
        print("Bye bye!")
        break

    print("\n----------------------------\n")