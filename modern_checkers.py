import tkinter as tk
from tkinter import messagebox
import random

class CheckersGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checkers")
        self.root.configure(bg='#f5f5f7')  # Apple-style background
        
        # Game state
        self.board = self.create_board()
        self.selected_piece = None
        self.player_turn = True  # True for player (black), False for computer (red)
        self.valid_moves = []
        
        # Colors and styles
        self.DARK_SQUARE = '#8a8a8a'
        self.LIGHT_SQUARE = '#ffffff'
        self.PLAYER_COLOR = '#333333'
        self.COMPUTER_COLOR = '#ff3b30'
        self.HIGHLIGHT_COLOR = '#007aff'
        
        # Create the game board GUI
        self.create_gui()
        
    def create_board(self):
        # Initialize 8x8 board
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Set up initial pieces
        for row in range(8):
            for col in range(8):
                if row < 3 and (row + col) % 2 == 1:
                    board[row][col] = {'color': 'red', 'king': False}
                elif row > 4 and (row + col) % 2 == 1:
                    board[row][col] = {'color': 'black', 'king': False}
        
        return board
    
    def create_gui(self):
        # Main frame
        self.frame = tk.Frame(
            self.root,
            padx=20,
            pady=20,
            bg='#f5f5f7'
        )
        self.frame.pack(expand=True)
        
        # Status label
        self.status_label = tk.Label(
            self.frame,
            text="Your turn",
            font=('SF Pro Text', 16),
            bg='#f5f5f7',
            fg='#1d1d1f'
        )
        self.status_label.pack(pady=(0, 20))
        
        # Game board frame
        self.board_frame = tk.Frame(
            self.frame,
            bg='#ffffff',
            padx=2,
            pady=2,
        )
        self.board_frame.pack()
        
        # Create squares and bind clicks
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                color = self.LIGHT_SQUARE if (row + col) % 2 == 0 else self.DARK_SQUARE
                square = tk.Canvas(
                    self.board_frame,
                    width=60,
                    height=60,
                    bg=color,
                    highlightthickness=0
                )
                square.grid(row=row, column=col)
                square.bind('<Button-1>', lambda e, r=row, c=col: self.square_clicked(r, c))
                self.squares[row][col] = square
        
        self.draw_board()
        
    def draw_board(self):
        # Clear all squares
        for row in range(8):
            for col in range(8):
                self.squares[row][col].delete('piece')
                self.squares[row][col].delete('highlight')
        
        # Draw pieces
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    color = self.PLAYER_COLOR if piece['color'] == 'black' else self.COMPUTER_COLOR
                    self.draw_piece(row, col, color, piece['king'])
        
        # Highlight valid moves
        for move in self.valid_moves:
            row, col = move[1]  # Destination coordinates
            self.squares[row][col].create_oval(
                5, 5, 55, 55,
                outline=self.HIGHLIGHT_COLOR,
                width=2,
                tags='highlight'
            )
    
    def draw_piece(self, row, col, color, king=False):
        canvas = self.squares[row][col]
        canvas.create_oval(10, 10, 50, 50, fill=color, tags='piece')
        if king:
            canvas.create_text(30, 30, text='★', fill='#ffffff', font=('SF Pro Text', 20), tags='piece')
    
    def square_clicked(self, row, col):
        if not self.player_turn:
            return
            
        piece = self.board[row][col]
        
        # If selecting a piece
        if piece and piece['color'] == 'black':
            self.selected_piece = (row, col)
            self.valid_moves = self.get_valid_moves(row, col)
            self.draw_board()
            
        # If selecting a destination
        elif self.selected_piece:
            start_row, start_col = self.selected_piece
            move = ((start_row, start_col), (row, col))
            
            if move in self.valid_moves:
                self.make_move(move)
                self.selected_piece = None
                self.valid_moves = []
                self.draw_board()
                
                if not self.game_over():
                    self.player_turn = False
                    self.status_label.config(text="Computer's turn")
                    self.root.after(1000, self.computer_move)
    
    def get_valid_moves(self, row, col):
        moves = []
        piece = self.board[row][col]
        
        if not piece:
            return moves
            
        directions = []
        if piece['color'] == 'black' or piece['king']:
            directions.extend([(-1, -1), (-1, 1)])  # Up-left and up-right
        if piece['color'] == 'red' or piece['king']:
            directions.extend([(1, -1), (1, 1)])    # Down-left and down-right
            
        # Check regular moves
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col) and not self.board[new_row][new_col]:
                moves.append(((row, col), (new_row, new_col)))
                
        # Check jumps
        for dr, dc in directions:
            jump_row, jump_col = row + 2*dr, col + 2*dc
            between_row, between_col = row + dr, col + dc
            
            if self.is_valid_position(jump_row, jump_col) and \
               self.board[between_row][between_col] and \
               self.board[between_row][between_col]['color'] != piece['color'] and \
               not self.board[jump_row][jump_col]:
                moves.append(((row, col), (jump_row, jump_col)))
                
        return moves
    
    def is_valid_position(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
    def make_move(self, move):
        start, end = move
        start_row, start_col = start
        end_row, end_col = end
        
        # Move the piece
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None
        
        # Check if piece becomes king
        if end_row == 0 and self.board[end_row][end_col]['color'] == 'black':
            self.board[end_row][end_col]['king'] = True
        elif end_row == 7 and self.board[end_row][end_col]['color'] == 'red':
            self.board[end_row][end_col]['king'] = True
            
        # Remove jumped piece if it was a jump move
        if abs(end_row - start_row) == 2:
            jumped_row = (start_row + end_row) // 2
            jumped_col = (start_col + end_col) // 2
            self.board[jumped_row][jumped_col] = None
    
    def computer_move(self):
        # Get all possible moves for computer pieces
        all_moves = []
        for row in range(8):
            for col in range(8):
                if self.board[row][col] and self.board[row][col]['color'] == 'red':
                    moves = self.get_valid_moves(row, col)
                    all_moves.extend(moves)
        
        if all_moves:
            # Prioritize jumps over regular moves
            jump_moves = [move for move in all_moves if abs(move[0][0] - move[1][0]) == 2]
            chosen_move = random.choice(jump_moves) if jump_moves else random.choice(all_moves)
            
            self.make_move(chosen_move)
            self.draw_board()
            
            if not self.game_over():
                self.player_turn = True
                self.status_label.config(text="Your turn")
        
    def game_over(self):
        # Check if either player has any pieces left
        black_pieces = False
        red_pieces = False
        
        for row in range(8):
            for col in range(8):
                if self.board[row][col]:
                    if self.board[row][col]['color'] == 'black':
                        black_pieces = True
                    else:
                        red_pieces = True
                        
        if not black_pieces:
            messagebox.showinfo("Game Over", "Computer wins!")
            return True
        elif not red_pieces:
            messagebox.showinfo("Game Over", "You win!")
            return True
            
        return False
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = CheckersGame()
    game.run()
