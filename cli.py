import os
import time

class CliUI:
    """
    Command-line interface for the Connect Four game.
    """
    def __init__(self, board):
        self.board = board
    
    def clear_screen(self):
        """Clears the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw_board(self):
        """Draws the current state of the board in the terminal."""
        self.clear_screen()
        print("\nConnect Four\n")
        
        # Print column numbers
        header = "  "
        for col in range(self.board.cols):
            header += str(col + 1) + " "
        print(header)
        
        # Print board
        for row in range(self.board.rows):
            row_str = "| "
            for col in range(self.board.cols):
                if self.board.board[row][col] == 0:
                    row_str += ". "
                elif self.board.board[row][col] == 1:
                    row_str += "X "  # Human player (red in GUI)
                else:
                    row_str += "O "  # AI player (yellow in GUI)
            row_str += "|"
            print(row_str)
        
        # Print bottom border
        footer = "  "
        for col in range(self.board.cols):
            footer += "= "
        print(footer + "\n")
    
    def get_human_move(self):
        """Gets a move from the human player via command line."""
        while True:
            try:
                col = input("Your move (1-7): ")
                col = int(col) - 1  # Convert to 0-based indexing
                
                if 0 <= col < self.board.cols and self.board.is_valid_move(col):
                    return col
                else:
                    print("Invalid move. Column must be between 1-7 and not full.")
            except ValueError:
                print("Please enter a number between 1 and 7.")
    
    def animate_piece_drop(self, col, row, player):
        """Simple animation effect for CLI."""
        # No complex animation in CLI mode
        pass
    
    def display_winner(self, winner):
        """Displays who won the game."""
        print("\n" + "=" * 30)
        if winner == 1:
            print("You win! Congratulations!")
        elif winner == 2:
            print("AI wins! Better luck next time!")
        else:
            print("It's a draw!")
        print("=" * 30 + "\n")
    
    def show_difficulty_selection(self):
        """Shows a difficulty selection prompt."""
        print("\nSelect AI difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Expert")
        
        while True:
            try:
                choice = int(input("Enter your choice (1-4): "))
                if 1 <= choice <= 4:
                    difficulties = ["easy", "medium", "hard", "expert"]
                    return difficulties[choice - 1]
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")
    
    def handle_game_end(self):
        """Handles the end-of-game state and returns whether to restart."""
        restart = input("Play again? (y/n): ").lower().startswith('y')
        return restart