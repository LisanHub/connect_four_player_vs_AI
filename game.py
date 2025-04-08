from board import Board
from ai import AIPlayer
from player import HumanPlayer

class Game:
    """
    Main game controller class that coordinates the game flow.
    """
    def __init__(self, ui, ai_difficulty='medium'):
        """Initialize the game with the given UI and difficulty."""
        self.board = Board()
        self.ui = ui
        self.ui.board = self.board  # Connect the UI to the board
        self.human = HumanPlayer(player_num=1)
        self.ai = AIPlayer(player_num=2, difficulty=ai_difficulty)
        self.current_player = 1  # Human starts
    
    def start(self):
        """Start the game and return whether to play again."""
        # Reset game state
        self.board.reset()
        self.current_player = 1
        
        # Show initial board
        self.ui.draw_board()
        
        # Main game loop
        game_over = False
        while not game_over:
            # Get the current player's move
            if self.current_player == 1:  # Human's turn
                col = self.human.get_move(self.board, self.ui)
            else:  # AI's turn
                col = self.ai.get_move(self.board)
            
            # Make the move
            if self.board.drop_piece(col, self.current_player):
                row = self.board.last_move[0]
                
                # Animate the piece drop and update the display
                self.ui.animate_piece_drop(col, row, self.current_player)
                self.ui.draw_board()
                
                # Check for win or draw
                if self.board.check_win(self.current_player):
                    game_over = True
                    self.ui.display_winner(self.current_player)
                elif self.board.is_full():
                    game_over = True
                    self.ui.display_winner(0)  # Draw
                else:
                    # Switch turns
                    self.current_player = 3 - self.current_player  # Switch between 1 and 2
        
        # Game is over, let the UI handle restart logic
        return self.ui.handle_game_end()