############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

# 카드를 컴퓨터와 내가 2장씩 받는다
# 카드를 추가로 받을지 말지 결정한다
## if no = 비교 후 승자 선언
## if yes = 카드 받고 21넘어가는지 확인
### 21 넘어가면 패배, 안넘어가면 추가로 카드를 받을것인지 다시 확인
#### no 선택시 비교 후 승자 선언

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer = []
user = []

computer.append(random.choice(cards))
computer.append(random.choice(cards))
user.append(random.choice(cards))
user.append(random.choice(cards))

print(f"Computer's cards are : {computer[0]} and X")

your_card = 0
for i in user:
	your_card += i
print(f"Your cards are: {user[0]} and {user[1]}")


go_stop = True

while go_stop:
	h_or_s = input(f"Your total is {your_card}, Do you want to hit or stand? 'h' or 's' >> ")
	if h_or_s == 'h':
		your_card += random.choice(cards)
		if your_card > 21:
			card_comp = 0
			for i in computer:
				card_comp += int(i)
			while card_comp <= 16:
				card_comp += random.choice(cards)
				if card_comp > 21:
					go_stop = False
					print(f"You win, you:{your_card}   computer: {card_comp}")
				elif your_card == card_comp:
					go_stop = False
					print(f"Draw, you:{your_card}   computer: {card_comp}")
			go_stop = False

		else:
			print(f"Your card is {your_card}")
	else:
		print(f"Your card is {your_card}")
		go_stop = False


card_comp = 0
for i in computer:
	card_comp += int(i)
while card_comp <=16:
	card_comp += random.choice(cards)


if card_comp > your_card:
	if card_comp > 21:
		print(f"You win, you:{your_card}   computer: {card_comp}")
	elif card_comp == your_card:
		print(f"Draw, you:{your_card}   computer: {card_comp}")
	else:
		print(f"You lose, computer: {card_comp}  you: {your_card}")
else:
	if your_card > 21:
		print(f"You lose, computer: {card_comp}  you: {your_card}")
	else:
		print(f"You win, you:{your_card}   computer: {card_comp}")

# if card_comp < 17:
# 	computer.append(random.choice(cards))

