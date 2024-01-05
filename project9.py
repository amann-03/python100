# SECRET AUCTION

import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("\nWelcome to the Secret Auction Bid Program.")

bids = {}
bidding = False

def max_bid(bid_record):
    max = 0
    for bidder in bid_record:
        value = bid_record[bidder]
        if value > max:
            max = value
            winner = bidder
        else:
            continue
    
    print(f"The winner is {winner} with a bid of {max}$. ")

while not bidding:
    
    name = input("\nWhat is your name? - ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    want_continue = input("Is there other persons to bid? type 'yes' or 'no'. \n")
    
    if want_continue == "no":
        bidding = True
        max_bid(bids)
    elif  want_continue =="yes":
        os.system('cls')

# FINISH PROJECT 
        
        