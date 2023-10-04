#Ioannis Apomachos
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
print("Welcome to the secret auction program.")

def find_winner(auction_dictionary):
    highest_bid=0
    highest_bidder=""

    for bidder in auction_dictionary:
        bid_amount= auction_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            highest_bidder=bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

keep_running=True
keep_running_answer=""
name=""
auction_dictionary={}
bid_price=0

while keep_running:
    name=input("What is your name?: ")
    bid_price=int(input("What's your bid?: $"))
    auction_dictionary[name]= bid_price

    keep_running_answer=input("Are there any other bidders? Type 'yes' or 'no'. ")
    if keep_running_answer=="no":
        keep_running=False
     
find_winner(auction_dictionary)