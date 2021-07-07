#import dependency
import random

print("Let's play Rock, Paper, Scissors")

run="y"
while run=="y":
    
    options = ["r", "p", "s"]

    computer_choice = random.choice(options)

    user_choice = input("Make your choice: r(ock), p(aper), s(cissors)")

    if user_choice == "r" and computer_choice == "s":
        print("you chose rock and the computer chose scissors")
        print("You win! Rock beats scissors.")

    elif user_choice == "p" and computer_choice == "r":
        print("you chose paper and the computer chose rock")
        print("You win! Paper beats rock.")  

    elif user_choice == "s" and computer_choice == "p":
        print("you chose scissors and the computer chose paper")
        print("You win! Scissors beats paper.")  

    elif user_choice == "r" and computer_choice == "p":
        print("you chose rock and the computer chose paper")
        print("You lose! Paper beats rock.")

    elif user_choice == "p" and computer_choice == "s":
        print("you chose paper and the computer chose scissors")
        print("You lose! Scissors beats paper.")  

    elif user_choice == "s" and computer_choice == "r":
        print("you chose scissors and the computer chose rock")
        print("You lose! Rock beats scissors.") 

    elif user_choice == "r" and computer_choice == "r":
        print("you both choose rock. Tie!")

    elif user_choice == "p" and computer_choice == "p":
        print("you both choose paper. Tie!")

    elif user_choice == "s" and computer_choice == "s":
        print("you both choose scissors. Tie!")

    else: 
        print("I dont understand your selection. Make your choice from 'r', 'p', 's'")
    
    run = input("would you like to play again 'y' : ")