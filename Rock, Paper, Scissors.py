import random

option = ["rock","paper","scissors"]

while True:
    user_choice = input("Enter your choice:").lower()
    if user_choice not in option:
        print("Invalid choice, Please choose rock,paper,scissors : ")
        continue

    computer_choice = random.choice(option)
    print(f"Your choice: {user_choice}")
    print(f"Computer choice is: {computer_choice}")

    print("-" * 30)

    if user_choice == computer_choice:
        print("tie")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win")
    else:
        print("Computer win")

    print("-" * 30)

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break