deck_of_cards= input().split()
count_shiffles = int(input())

for shuffle in range(count_shiffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)): #len(right_part) - няма значение, тъй като и двете са с еднаква дължина
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling # за да разбъркваме вече новото разбъркано тесте
print(deck_after_shuffling)