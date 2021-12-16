import os
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

other_bidders = 'yes'
bid = {}
aux = 0

while other_bidders == 'yes':
    name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))

    bid[name] = bid_value
    

    other_bidders = input("Are there any other bidders? type 'yes' or 'no'.\n")

    if other_bidders == 'yes':
        cls = lambda: os.system('clear')
        cls()
    else:
        for name in bid:
            if bid[name] > aux:
                aux = bid[name]
                winner = name
                
        print(f"The wunner is {winner} with a bid of ${aux}")