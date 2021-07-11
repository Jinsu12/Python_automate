# 빈 딕셔너리에 참가자이름을 키로, 입찰금을 밸류로 넣는다.
# 참가자 이름 input
# 입찰금 input
# 추가 참가자가 있는지 yes or no
# no일경우 멈추고 입찰급이 가장 큰 참가자가 우승한 것으로 print
# no를 제외한 다른 키를 입력하는 경우 계속 참가자를 입력할 수 있게 진행



def winner():
    high_score = 0
    win = ""
    for bidder in bids:
        if bids[bidder] > high_score:
            high_score = bids[bidder]
            win = bidder
    print(f"The winner is {win} with {high_score}")


bids = {}
go_stop = False
while not go_stop:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    participants = input("Are there more participants? 'yes' or 'no' \n")
    if participants == 'no':
        go_stop = True
        print(bids)
        winner(bids)
