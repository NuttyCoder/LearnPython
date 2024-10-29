# table.py
from deck import Deck

class Table:
    def __init__(self):
        self.deck = Deck()
        self.tableau = [[] for _ in range(7)]
        self.foundation = [[] for _ in range(4)]
        self.stock = []
        self.waste = []

    def setup(self):
        for i in range(7):
            for j in range(i, 7):
                self.tableau[j].append(self.deck.draw_card())
