# game.py
from table import Table

class Solitaire:
    def __init__(self):
        self.table = Table()
        self.table.setup()

    def play(self):
        # Implement game loop and rules here
        pass

if __name__ == "__main__":
    game = Solitaire()
    game.play()
