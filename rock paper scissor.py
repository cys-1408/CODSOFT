import random

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or 
         (user_choice == 'scissors' and computer_choice == 'paper') or 
         (user_choice == 'paper' and computer_choice == 'rock')):
        return "You win!"
    else:
        return "You lose!"

def play():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("\nYour choice:",user_choice)
    print("Computer's choice:",computer_choice)

    result = winner(user_choice, computer_choice)
    print(result)

def main():
    play()

    while input("Do you want to play again? (yes/no): ").lower() == 'yes':
        play()
main()
