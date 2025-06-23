import random

option= ['r', 'p', 's']
computer = random.choice(option)
while True:
    choice = input("Enter your choice (r, p, s): ").lower()
    if computer == 'r' and choice == 'p':
        print('computer chose', computer)
        print("You win! Paper beats rock.")

    elif computer == 'r' and choice == 's':
        print('computer chose', computer)
        print("You lose! Rock beats scissors.")
        
    elif computer == 'p' and choice == 'r':
        print('computer chose', computer)
        print("You lose! Paper beats rock.")
        
    elif computer == 'p' and choice == 's':
        print('computer chose', computer)
        print("You win! Scissors beats paper.")
        
    elif computer == 's' and choice == 'r':
        print('computer chose', computer)
        print("You win! Rock beats scissors.")
        
    elif computer == 's' and choice == 'p':
        print('computer chose', computer)
        print("You lose! Scissors beats paper.")
        
    elif computer == choice :
        print("It's a tie! You both chose", choice)
        
    else:
        print("Invalid choice")
    print("Play again? (y/n)")
    play_again = str(input()).lower()
    if play_again == 'y':
        continue
    else:
        print("Thanks for playing!")
        break
