# BLACKJACK CAPSTONE PROJECT

import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
play = input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ")
want_continue = False

def random_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def decide_winner(user_score,comp_score):
    
    if user_score > 21:
        return "You went over. You lose 🥺"
    elif comp_score > 21:
        return "Opponent went over. You Win 😁"
    elif comp_score == user_score:
        return "It's a Draw. 😐"
    elif user_score > comp_score :
        return "You Win 😁"
    else:
        return "You lose 🥺"
        
if play=="Y":
    
    os.system('cls')
    while not want_continue:
        print(logo)
        
        user_cards = [random_cards(),random_cards()]
        computer_cards = [random_cards(),random_cards()]
        current_score = sum(user_cards)
        computer_score = sum(computer_cards)
        
        print(f"\n\tYour cards: {user_cards} , current score: {current_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        
        more_card = False
        
        while not more_card:
            
            new_card = input("Type 'Y' to get another card, type 'N' to pass: ")
            if new_card == "Y":
                user_cards.append(random_cards())
                current_score = sum(user_cards)
                
                print(f"\tYour cards: {user_cards}, current score: {current_score}")
                print(f"\tComputer's first card: {computer_cards[0]}")
                
                if current_score > 21:
                    more_card = True
                    
            else:
                more_card = True
            
        while computer_score < 17:
            computer_cards.append(random_cards())
            computer_score = sum(computer_cards)
        
        print(f"\tYour final hand: {user_cards}, final score: {current_score}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
        
        result = decide_winner(user_score=current_score,comp_score=computer_score)
        print(result)
               
        play_again = input("Do you want to play a game of Blackjack again? type 'Y' to play again or 'N' to exit: ")
        if play_again == "Y":
            continue
        else: 
            want_continue = True
    
# FINISH PROJECT