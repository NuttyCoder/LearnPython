import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __repr__(self):
        return ', '.join(map(str, self.cards))

def main():
    deck = Deck()
    player1_hand = Hand()
    player2_hand = Hand()

    # Draw initial hands
    for _ in range(10):
        player1_hand.add_card(deck.draw_card())
        player2_hand.add_card(deck.draw_card())

    print("Player 1 Hand:", player1_hand)
    print("Player 2 Hand:", player2_hand)

if __name__ == "__main__":
    main()
