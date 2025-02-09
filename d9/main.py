# 1. Make a dictionary to store the bidder name and respective bid amount.
# 2. Print the welcome message.
# 3. Validate the bid amount to be a number before adding it to the dictionary.
# 4. Calculate the bid winner based on the highest bid made.
# 5. Display the winner.

auction_info = []
auction = True

def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {}
    new_bidder["bid"] = bidder_amount
    new_bidder["name"] = bidder_name
    auction_info.append(new_bidder)

def welcome():
    print("Welcome to the private bidding auction")
  
def bid_validator(name, bid):
	if(bid.isdigit()):
		add_new_bidder(bidder_name = name, bidder_amount = int(bid))
	else:
		print("Inappropriate bid amount.")

def bid_winner_calculator():
	highest_bidder = 0
	count = -1
	for e in auction_info:
		if e['bid'] > highest_bidder:
			highest_bidder = e['bid']
			count += 1
		winner = auction_info[count]['name']
	print(f"The highest bidder is {winner} with a ${highest_bidder}")
	print("Thank you for your participation.")
	
welcome()
while auction:
	name  = input("What is your name?: ").title()
	bid = input("How much would you like to bid?: $")
	bid_validator(name, bid)

	others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n")
	if others == 'no':
		auction = False
		if len(auction_info):
			bid_winner_calculator()
		else: 
			print("No bids were made.")
	elif others == 'yes':
		continue
	else:
		print("The acution ended with an interruption!...")
		bid_winner_calculator()
		break
