import random
print("Welcome to ROCK PAPER SCISSORS GAME!\n")

user_choice = int(input("What do you chosose? Type 0 for rock, 1 for Paper or 2 for scissors.\n"))
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")

if user_choice>=3 or user_choice<0:
    print("You typed an invalid number. You Lose.")
elif user_choice==0 and computer_choice==2:
    print("You Win.")
elif computer_choice > user_choice:    
    print("You Lose.")
elif computer_choice==user_choice :
    print("It's a Draw.")
elif computer_choice==0 and user_choice==2:
    print("You Lose.")
elif user_choice > computer_choice:
    print("You Win.")

      
    