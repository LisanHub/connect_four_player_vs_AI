import numpy as np

class Board:
    """
    Represents the Connect Four game board with game logic.
    """
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = np.zeros((rows, cols), dtype=int)
        self.last_move = None
        
    def drop_piece(self, col, player):
        """
        Drops a piece in the specified column for the player.
        Returns True if move was successful, False if invalid.
        """
        # Check if column is valid and not full
        if col < 0 or col >= self.cols or self.board[0][col] != 0:
            return False
        
        # Find the lowest empty row
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                self.last_move = (row, col)
                return True
        
        return False
    
    def is_valid_move(self, col):
        """Check if a move to the specified column is valid."""
        return 0 <= col < self.cols and self.board[0][col] == 0
    
    def get_valid_moves(self):
        """Returns a list of columns where a piece can be dropped."""
        return [col for col in range(self.cols) if self.is_valid_move(col)]
    
    def check_win(self, player):
        """Checks if the specified player has won."""
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == player for i in range(4)):
                    return True
                    
        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if all(self.board[row + i][col] == player for i in range(4)):
                    return True
                    
        # Check diagonal (positive slope)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True
                    
        # Check diagonal (negative slope)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True
                    
        return False
    
    def is_full(self):
        """Checks if the board is full."""
        return all(self.board[0][col] != 0 for col in range(self.cols))
    
    def is_game_over(self):
        """Checks if the game is over."""
        return self.check_win(1) or self.check_win(2) or self.is_full()
    
    def get_winner(self):
        """Returns the winner (1 or 2), 0 for draw, None if game not over."""
        if self.check_win(1):
            return 1
        elif self.check_win(2):
            return 2
        elif self.is_full():
            return 0
        return None
    
    def reset(self):
        """Resets the board to its initial state."""
        self.board = np.zeros((self.rows, self.cols), dtype=int)
        self.last_move = None
    
    def copy(self):
        """Returns a copy of the board."""
        new_board = Board(self.rows, self.cols)
        new_board.board = self.board.copy()
        new_board.last_move = self.last_move
        return new_board
    
    def print_board(self):
        """Prints the board to the console (for debugging or CLI mode)."""
        print("\n")
        for row in range(self.rows):
            row_str = "|"
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    row_str += " "
                elif self.board[row][col] == 1:
                    row_str += "X"
                else:
                    row_str += "O"
                row_str += "|"
            print(row_str)
        
        # Print column numbers at the bottom
        footer = " "
        for col in range(self.cols):
            footer += str(col + 1) + " "
        print(footer + "\n")