import random

logo = '''                        
 / _      _   _   _  _/  /  _   /| )     _   /  _  _ 
(__)  (/ (- _)  _)   /  /) (-  / |/  (/ //) () (- /  
'''
print(logo)

Easy_turns = 10
Hard_turns = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

num = random.randint(1,100)

def check_answer(guess,answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if level == "easy":
        return Easy_turns
    else: 
        return Hard_turns
    
turns = set_difficulty()
guess =0
print(f"You have {turns} attempts to guess the number.")

while turns >0:
    guess = int(input("Make a guess: "))
    check_answer(guess,num)
    if guess != num:
        turns -= 1
        print(f"You have {turns} attempts left.")
        if turns == 0:
            print("You Lose.")
    else: 
        turns = 0
    
        
# Finish Project