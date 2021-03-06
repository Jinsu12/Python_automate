############### Blackjack Project #####################

#Difficulty Normal π: Use all Hints below to complete the project.
#Difficulty Hard π€: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard π­: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert π€―: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## if computer < 17 1μ₯ λ λ°κΈ°
## μ»΄ν¨ν° ν¨λ 1κ°λ§ λ³΄μ΄κ² λ§λ€κΈ°
## 2μ₯μ΄ μμ λ 21μ΄ λλ©΄ κ²μ λλ΄κΈ°
## λ§μ½ 21μ΄ λμ΄κ° κ²½μ° κ²μ λλ΄κΈ°

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
deal_card()


def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

if len(user_cards) == 2 and calculate_score(user_cards) == 21:
    print("You win!")
print(calculate_score(user_cards))