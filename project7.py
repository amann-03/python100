# HANGMAN PROJECT
# https://ascii.co.uk/art/hangman

import random
import os

logo = ''' _                                                
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   '''
                   
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)

word_list = ["ardvark","baboon","camel"]

chosen_word = random.choice(word_list)
print(f"Solution word is {chosen_word}.")
sol_size = len(chosen_word)
ans_list = []

for i in range(sol_size):
    ans_list.append('_') 

endgame = False
lives = 6
print(stages[6])
print(" ".join(ans_list))

while not endgame:
    
    guess = input("Guess a letter: ").lower()
    
    os.system('cls') # clears terminal screen after every run of loop
    
    i = 0
    for letter in chosen_word:
        if letter == guess:
            ans_list[i] = letter
        i += 1   
        
    print(" ".join(ans_list))
    print(stages[lives])
    
    if guess not in chosen_word:
        lives -= 1
        print(f"\nYou guessed {guess}, that's not in word. You lose a life.")
        print(f"Remaining lives: {lives}\n")
        
        if lives == 0:
            endgame = True
            print("\nYou Lose.")
    
    if "".join(ans_list) == chosen_word:
        endgame = True
        print("\nYou Win.")
    
# FINISH PROJECT



