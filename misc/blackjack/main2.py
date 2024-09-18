import random

# print("welcome to blackjack / 24")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    pick_a_card = random.choice(cards)
    return pick_a_card


user_deck = []
cpu_deck = []


for _ in range(2):
    user_deck.append(deal_card())
    cpu_deck.append(deal_card())


print(user_deck, cpu_deck)

# print(deal_card())

# cards = {
#     "A": 1 
# }

# while (1):
#     ques = input("do you wanna play blackjack? ")
#     if (ques != 'y'):
#         break

#     break