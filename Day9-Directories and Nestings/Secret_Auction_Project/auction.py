
bids={}
continue_bidding=True
def highest_bidder(bidding_dictionary):
    highest_bid =0
    winner=""
    for bidder in bidding_dictionary:
        bid_amount =  bidding_dictionary[bidder]
        if bid_amount > highest_bid :
            highest_bid=bid_amount
            winner = bidder

    print(f'The winner is {winner} and the highes bid is ${highest_bid}')



while continue_bidding :
    name = input("What is your name?\t")
    price = int(input("How much is your bid?\t$ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type Yes or No\n").lower()
    if should_continue == 'no':
        continue_bidding=False
        highest_bidder(bids)
    elif should_continue=="yes":
        print("\n" * 20)






