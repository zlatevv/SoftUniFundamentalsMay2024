cards = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    middle = len(cards) // 2
    left_side = cards[:middle]
    right_side = cards[middle:]
    deck_after_shuffling = []
    for card_index in range(len(left_side)):
        deck_after_shuffling.append(left_side[card_index])
        deck_after_shuffling.append(right_side[card_index])
    cards = deck_after_shuffling
print(cards)