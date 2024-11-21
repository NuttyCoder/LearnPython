import pygame
import random
import sys

# Game logic classes
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

# Pygame UI integration
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pirate Gin Rummy')

def draw_hand(screen, hand, x, y):
    font = pygame.font.Font(None, 36)
    for idx, card in enumerate(hand.cards):
        card_text = font.render(str(card), True, (255, 255, 255))
        screen.blit(card_text, (x, y + idx * 30))

def game_loop():
    deck = Deck()
    player1_hand = Hand()
    player2_hand = Hand()

    # Draw initial hands
    for _ in range(10):
        player1_hand.add
