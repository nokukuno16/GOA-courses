def is_flush(cards):
    first_suit = cards[0][-1]  # Get the suit of the first card
    for card in cards:
        if card[-1] != first_suit:  # Check if any card has a different suit
            return False
    return True