#Ioannis Apomachos


import random
import art
import game_data


def compare_candidates(users_candidate, other_candidate):
    """Takes user's choice (as the first parameter) and compares it to the other candidate."""
    if users_candidate['follower_count']>other_candidate['follower_count']:
        return False
    else:
        return True
    


game_over=False
current_correct_answers=0


candidate_b=random.choice(game_data.data)

while not game_over:
    print(art.logo)

    if current_correct_answers!=0:
        print(f"Your current correct answers are {current_correct_answers}")
    
    candidate_a=candidate_b
    candidate_b=random.choice(game_data.data)

    while candidate_a==candidate_b:
        candidate_b=random.choice(game_data.data)

    print(f"Compare A: {candidate_a['name']}, a {candidate_a['description']}, from {candidate_a['country']}")
    print(art.vs)
    print(f"Against B: {candidate_b['name']}, a {candidate_b['description']}, from {candidate_b['country']}")


    choice=input("Who has more followers? Type 'A' or 'B': ") .lower()   
    if choice=='A':
        game_over=compare_candidates(candidate_a, candidate_b)
    else:
        game_over=compare_candidates(candidate_b, candidate_a)

    if not game_over:
        current_correct_answers+=1
    else:
        print(f"You lose with {current_correct_answers} correct answers")


