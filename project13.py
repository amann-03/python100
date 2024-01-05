# Higher-Lower Game Project

from gameData_project13 import data
import random 
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
print(logo)

score = 0
want_continue = True
account_b = random.choice(data)

def check_answer(guess,a_followers,b_followers):
        '''Take user's guess and followers's count and returns bool if they got true.'''
        if a_followers > b_followers:
            return guess=="a"
        else:
            return guess=="b"
        
 # data is list of dictionaries that is key-value pairs

def format_data(account):
    '''format the account data into printable format'''
    acoount_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{acoount_name}, a {account_descr}, from {account_country}"

while want_continue:
    
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a==account_b:
        account_b = random.choice(data )

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}\n")

    guess = input("Who has more followers? Type A or B: ").lower()

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess,a_followers,b_followers)

    os.system('cls')
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right!, Current score: {score}")
    else:
        want_continue = False
        print(f"Sorry,that's wrong. Final Score: {score}")  

# Finish Project.