import random
import numpy as np

class AIPlayer:
    """
    AI player that uses the Minimax algorithm to make decisions.
    """
    def __init__(self, player_num=2, difficulty='medium'):
        self.player_num = player_num  # AI player number (usually 2)
        self.opponent_num = 1 if player_num == 2 else 2
        self.set_difficulty(difficulty)
    
    def set_difficulty(self, difficulty):
        """Set the AI difficulty level by adjusting minimax depth."""
        difficulty_levels = {
            'easy': 1,     # Reduced from 2 to 1
            'medium': 3,   # Reduced from 4 to 3
            'hard': 4,     # Reduced from 5 to 4
            'expert': 6
        }
        self.depth = difficulty_levels.get(difficulty.lower(), 3)
        self.difficulty = difficulty.lower()
        return self.depth
    
    def get_move(self, board):
        """
        Uses the minimax algorithm to choose the best move.
        Returns the column to drop the piece.
        """
        valid_moves = board.get_valid_moves()
        if not valid_moves:
            return None
        
        # For easy difficulty, sometimes make a completely random move
        if self.difficulty == 'easy' and random.random() < 0.4:
            return random.choice(valid_moves)
            
        # For first few moves, add randomness to improve variety
        if np.count_nonzero(board.board) <= 3:
            random_factor = {
                'easy': 0.8,
                'medium': 0.4,
                'hard': 0.2,
                'expert': 0.0
            }.get(self.difficulty, 0.4)
            
            if random.random() < random_factor:
                return random.choice(valid_moves)
        
        best_score = float('-inf')
        best_col = random.choice(valid_moves)  # Default to random valid move
        
        # Try each valid column and pick the one with the best score
        for col in valid_moves:
            # Make a copy of the board
            temp_board = board.copy()
            temp_board.drop_piece(col, self.player_num)
            
            # Get score for this move
            score = self.minimax(temp_board, self.depth - 1, False, float('-inf'), float('inf'))
            
            # Add a large random factor for lower difficulties to make the AI less perfect
            if self.difficulty == 'easy':
                score += random.uniform(-8.0, 8.0)
            elif self.difficulty == 'medium':
                score += random.uniform(-3.0, 3.0)
            elif self.difficulty == 'hard':
                score += random.uniform(-1.0, 1.0)
            
            # Update best move if this score is better
            if score > best_score:
                best_score = score
                best_col = col
        
        # For easy mode, occasionally avoid winning moves to give the player a chance
        if self.difficulty == 'easy':
            temp_board = board.copy()
            temp_board.drop_piece(best_col, self.player_num)
            if temp_board.check_win(self.player_num) and random.random() < 0.7:
                # Try to find a non-winning move instead
                other_moves = [m for m in valid_moves if m != best_col]
                if other_moves:
                    return random.choice(other_moves)
        
        return best_col
    
    def minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Minimax algorithm with alpha-beta pruning.
        Returns the best score for the current board position.
        """
        # Check terminal conditions
        winner = board.get_winner()
        if winner is not None:
            if winner == self.player_num:
                return 10000  # AI wins
            elif winner == 0:
                return 0  # Draw
            else:
                return -10000  # Human wins
        
        if depth == 0:
            return self.evaluate_board(board)
        
        valid_moves = board.get_valid_moves()
        
        if is_maximizing:  # AI's turn (maximizing)
            value = float('-inf')
            for col in valid_moves:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.player_num)
                score = self.minimax(temp_board, depth - 1, False, alpha, beta)
                value = max(value, score)
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cutoff
            return value
        else:  # Human's turn (minimizing)
            value = float('inf')
            for col in valid_moves:
                temp_board = board.copy()
                temp_board.drop_piece(col, self.opponent_num)
                score = self.minimax(temp_board, depth - 1, True, alpha, beta)
                value = min(value, score)
                beta = min(beta, value)
                if alpha >= beta:
                    break  # Alpha cutoff
            return value
    
    def evaluate_board(self, board):
        """
        Evaluates the board position for the AI player.
        Returns a score based on the current board state.
        """
        score = 0
        
        # Apply difficulty factor - easier levels evaluate the board less accurately
        difficulty_factor = {
            'easy': 0.1,
            'medium': 0.3,
            'hard': 0.6,
            'expert': 1.0
        }.get(self.difficulty, 1.0)
        
        # Score center column higher (control of center is advantageous)
        center_col = board.cols // 2
        center_array = [int(i) for i in list(board.board[:, center_col])]
        center_count = center_array.count(self.player_num)
        score += center_count * 3 * difficulty_factor
        
        # Score horizontal windows
        for row in range(board.rows):
            row_array = [int(i) for i in list(board.board[row, :])]
            for col in range(board.cols - 3):
                window = row_array[col:col+4]
                score += self.evaluate_window(window, difficulty_factor)
        
        # Score vertical windows
        for col in range(board.cols):
            col_array = [int(i) for i in list(board.board[:, col])]
            for row in range(board.rows - 3):
                window = col_array[row:row+4]
                score += self.evaluate_window(window, difficulty_factor)
        
        # Score positive diagonal windows
        for row in range(board.rows - 3):
            for col in range(board.cols - 3):
                window = [board.board[row+i][col+i] for i in range(4)]
                score += self.evaluate_window(window, difficulty_factor)
        
        # Score negative diagonal windows
        for row in range(3, board.rows):
            for col in range(board.cols - 3):
                window = [board.board[row-i][col+i] for i in range(4)]
                score += self.evaluate_window(window, difficulty_factor)
        
        return score
    
    def evaluate_window(self, window, difficulty_factor=1.0):
        """
        Evaluates a window of 4 positions and returns a score.
        This function implements the evaluation function described in requirements.
        """
        score = 0
        ai_count = window.count(self.player_num)
        opponent_count = window.count(self.opponent_num)
        empty_count = window.count(0)
        
        # Score AI pieces
        if ai_count == 4:
            score += 100  # Winning position
        elif ai_count == 3 and empty_count == 1:
            score += 5 * difficulty_factor    # Potential win (3 in a row)
        elif ai_count == 2 and empty_count == 2:
            score += 2 * difficulty_factor    # Build-up (2 in a row)
        
        # Penalize opponent's potential wins more severely
        # Lower difficulties are less likely to block winning moves
        if opponent_count == 3 and empty_count == 1:
            score -= 8 * difficulty_factor    # Block opponent's potential win
        elif opponent_count == 2 and empty_count == 2:
            score -= 2 * difficulty_factor    # Block opponent's build-up
        
        return score