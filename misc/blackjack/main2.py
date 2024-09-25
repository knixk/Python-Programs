import random

print("welcome to blackjack / 24")

# BLACKJACK = 21
# ACE_SMALLER = 1
# ACE_BIGGER = 2
not_game_over = True

user_deck = []
cpu_deck = []

def deal_card():
    """Returns a random cards from a deck of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    pick_a_card = random.choice(cards)
    return pick_a_card

def optimize(deck):
    total = sum(deck)
    pass

def calculate_score(cards):
    '''Returns the score takes in an arr as input'''
    total = sum(cards)

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if total == 21 and len(cards) == 2:
        return 0

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and total > 21:
        cards.remove(11).append(1)

    return total

def check_game_over():
    user_score = calculate_score(user_deck)
    cpu_score = calculate_score(cpu_deck)

    if (user_score == 0 or cpu_score == 0 or user_score > 21):
        return True

    return False

def user_deals():
    """function for user to deal a card or not"""
    ans = input("Would you like to take another card or pass? ")

    if (ans == "y"):
        # deal another card..
        user_deck.append(deal_card())
        pass
    elif (ans == "n"):
        # show the final show and check if win or lose..
        pass

    print(f"user_deck: {user_deck}, cpu_deck: {cpu_deck}")
    user_score = calculate_score(user_deck)
    print(user_score, " : Your score")

def cpu_deals():
    """simple algo for cpu to teach until less than 17"""
    cpu_score = calculate_score(cpu_deck)

    if (cpu_score < 17):
        cpu_deck.append(deal_card())
        print("cpu decided to deal")

    print("cpu decided to pass..")

# deals two cards at first
for _ in range(2):
    user_deck.append(deal_card())
    cpu_deck.append(deal_card())

print(f"user_deck: {user_deck}, cpu_deck: {cpu_deck}")

def play():
    # prmpt = input("would you like to draw another card?")
    user_score = calculate_score(user_deck)
    cpu_score = calculate_score(cpu_deck)

    print(user_score, " : Your score")
    print(cpu_score, " : CPU's score")

    user_deals()
    cpu_deals()

while (not_game_over):
    ans = check_game_over()
    if (ans):
        not_game_over = False
        break
    play()

























# print(deal_card())

# cards = {
#     "A": 1 
# }

# while (1):
#     ques = input("do you wanna play blackjack? ")
#     if (ques != 'y'):
#         break

#     break