#Ioannis Apomachos 
import random

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




cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand=[]
pc_hand=[]
user_score=0
pc_score=0

def deal_card():
    return random.choice(cards)

def calculate_score(hand):

    if sum(hand)==21 and len(hand)==2:
        return 0

    if 11 in hand and sum(hand)>21:
        hand.remove(11)
        hand.append(1)
   
    return sum(hand)

def compare(user_score,pc_score):
    if user_score==pc_score:
        return"It's a draw"
    elif pc_score==0:
        return"Computer has Blackjack, you loose"
    elif user_score==0:
        return"You have a Blackjack, you win!"
    elif user_score>21:
        return"You have more than 21, you loose"
    elif pc_score>21:
        return"Computer has more than 21, you win"
    elif user_score>pc_score:
        return"You have higher score, you win"
    else:
        return"You loose"

start_playing=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
continue_playing=True

if start_playing=='y':

    print(logo)

    user_hand.append(deal_card())
    user_hand.append(deal_card())

    pc_hand.append(deal_card())
    pc_hand.append(deal_card())

    while continue_playing:
        user_score=calculate_score(user_hand)
        pc_score=calculate_score(pc_hand)

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {pc_hand[0]}")

        if user_score==0 or pc_score==0 or user_score>21:
            continue_playing=False
        else:
            user_should_deal=input("Type 'y' to get another cards, type 'n' to pass: ")
            if user_should_deal=='y':
                user_hand.append(deal_card())
            else:
                continue_playing=False
        
    while pc_score!=0 and pc_score<17:
        pc_hand.append(deal_card())
        pc_score=calculate_score(pc_hand)


    if {user_score}==0:
        user_score=21

    if {pc_score}==0:
        pc_score=21

    print(f"Your cards are: {user_hand}, with a score: {user_score}")
    print(f"Computer cards are: {pc_hand}, with a score: {pc_score}")
    print(compare(user_score,pc_score))
