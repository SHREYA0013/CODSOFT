import random

def display_instructions():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Instructions:")
    print("Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.")
    print("Enter your choice when prompted.")
    print("To exit the game, type 'exit'.")
    print("Let's play!\n")

def display_score(player_score, computer_score):
    print(f"Score - Player: {player_score}, Computer: {computer_score}\n")

def main():
    Options = ("Rock", "Paper", "Scissors")
    player_score = 0
    computer_score = 0

    display_instructions()

    while True:
        player = None
        computer = random.choice(Options)

        while player not in Options:
            player = input("Enter your choice (Rock, Paper, Scissors): ").capitalize()

            if player == 'Exit':
                print("Thanks for playing. Exiting the game.")
                return

        print(f"\nPlayer: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("It's a tie!\n")
        elif (
            (player == "Rock" and computer == "Scissors") or
            (player == "Scissors" and computer == "Paper") or
            (player == "Paper" and computer == "Rock")
        ):
            print("Congratulations! You win!!\n")
            player_score += 1
        else:
            print("Oops! You lose!\n")
            computer_score += 1

        display_score(player_score, computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Final score:")
            display_score(player_score, computer_score)
            break

if __name__ == "__main__":
    main()
