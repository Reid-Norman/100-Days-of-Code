from replit import clear
from art import logo

print(logo)

bidding_complete = False
list_of_bids = {}

def find_highest_bidder(record_of_bids):
    highest_bid = 0
    highest_bidder = ""
    for key in record_of_bids:
        bid_amount = record_of_bids[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = key    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

while bidding_complete is not True:
    name = input("What is your name?: ")
    bid_price = float(input("What is your bid: $"))
    
    list_of_bids[name] = bid_price
    # Testing Code
    #print(list_of_bids)
    
    response = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    clear()
    if response == "no":
        bidding_complete = True
        find_highest_bidder(list_of_bids)
