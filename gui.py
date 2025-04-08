import pygame
import sys
import time
import numpy as np

class GameUI:
    """
    Graphical user interface for the Connect Four game using pygame.
    """
    # Colors
    BLUE = (0, 155, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    PLAYER_COLOR = (255, 0, 0)
    AI_COLOR = (37, 187, 44)
    YELLOW = (37, 187, 44)
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    DARK_GRAY = (100, 100, 100)
    GREEN = (0, 255, 31)
    PURPLE = (75, 0, 130)
    
    def __init__(self, board, square_size=100):
        self.board = board
        self.square_size = square_size
        self.radius = square_size // 2 - 5
        self.width = board.cols * square_size
        self.height = (board.rows + 1) * square_size  # Extra row for piece dropping
        
        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Connect Four')

        self.font = pygame.font.SysFont('monospace', 30)
        self.big_bold_font = pygame.font.SysFont('monospace', 30, bold= True)
        self.small_font = pygame.font.SysFont('monospace', 20)
        self.bold_font = pygame.font.SysFont('monospace', 20, bold=True)  # Add this line
        
        # Initial UI drawing
        self.draw_board()
        pygame.display.update()
    
    def draw_board(self):
        """Draws the current state of the board."""
        self.screen.fill(self.BLACK)
        
        # Draw drop area (top row)
        for col in range(self.board.cols):
            pygame.draw.rect(self.screen, self.GRAY, 
                            (col * self.square_size, 0, self.square_size, self.square_size))
        
        # Draw board background
        pygame.draw.rect(self.screen, self.BLUE, 
                         (0, self.square_size, self.width, self.height - self.square_size))
        
        # Draw empty slots and pieces
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                # Draw circle slots
                pygame.draw.circle(self.screen, self.BLACK, 
                                  (col * self.square_size + self.square_size // 2, 
                                   (row + 1) * self.square_size + self.square_size // 2), 
                                  self.radius)
                
                # Draw pieces
                if self.board.board[row][col] == 1:
                    pygame.draw.circle(self.screen, self.PLAYER_COLOR, 
                                      (col * self.square_size + self.square_size // 2, 
                                       (row + 1) * self.square_size + self.square_size // 2), 
                                      self.radius)
                elif self.board.board[row][col] == 2:
                    pygame.draw.circle(self.screen, self.AI_COLOR, 
                                      (col * self.square_size + self.square_size // 2, 
                                       (row + 1) * self.square_size + self.square_size // 2), 
                                      self.radius)
        
        # Draw column numbers at the bottom
        # for col in range(self.board.cols):
        #     text = self.small_font.render(str(col + 1), True, self.WHITE)
        #     self.screen.blit(text, (col * self.square_size + self.square_size // 2 - 5, 
        #                            (self.board.rows + 0.7) * self.square_size))
        # Draw column numbers at the bottom
        for col in range(self.board.cols):
            text = self.bold_font.render(str(col + 1), True, self.WHITE)                # bold_font
            self.screen.blit(text, (col * self.square_size + self.square_size // 2 - 5, 
                                    (self.board.rows + 0.7) * self.square_size))
        
        pygame.display.update()
    
    def draw_hovering_piece(self, col, player):
        """Draws a hovering piece above the specified column."""
        # Clear top row first
        for c in range(self.board.cols):
            pygame.draw.rect(self.screen, self.GRAY, 
                           (c * self.square_size, 0, self.square_size, self.square_size))
            
        if 0 <= col < self.board.cols:
            color = self.PLAYER_COLOR if player == 1 else self.AI_COLOR
            pygame.draw.circle(self.screen, color, 
                              (col * self.square_size + self.square_size // 2, 
                               self.square_size // 2), 
                              self.radius)
        
        pygame.display.update()
    
    def animate_piece_drop(self, col, row, player):
        """Animates a piece dropping into position."""
        color = self.PLAYER_COLOR if player == 1 else self.AI_COLOR
        
        # Clear the top position first
        pygame.draw.rect(self.screen, self.GRAY, 
                       (col * self.square_size, 0, self.square_size, self.square_size))
        
        # Animate the drop
        for r in range(row + 1):
            # Draw piece at current position
            pygame.draw.rect(self.screen, self.BLUE, 
                           (col * self.square_size, self.square_size, 
                            self.square_size, (r) * self.square_size))
            
            pygame.draw.circle(self.screen, self.BLACK, 
                              (col * self.square_size + self.square_size // 2, 
                               (r) * self.square_size + self.square_size // 2 + self.square_size), 
                              self.radius)
            
            pygame.draw.circle(self.screen, color, 
                              (col * self.square_size + self.square_size // 2, 
                               r * self.square_size + self.square_size // 2 + self.square_size), 
                              self.radius)
            
            pygame.display.update()
            
            # Erase the piece if not at final position
            if r < row:
                pygame.draw.circle(self.screen, self.BLACK, 
                                  (col * self.square_size + self.square_size // 2, 
                                   r * self.square_size + self.square_size // 2 + self.square_size), 
                                  self.radius)
            
            pygame.time.wait(50)  # Animation speed
    
    def display_winner(self, winner):
        """Displays who won the game."""
        if winner == 1:
            message = "PLAYER WINS!"
        elif winner == 2:
            message = "AI WINS!"
        else:
            message = "DRAW!"
            
        text = self.font.render(message, True, self.WHITE)
        text_rect = text.get_rect(center=(self.width//2, self.square_size//2))
        
        restart_text = self.small_font.render("Press R to restart, ESC to quit", True, self.WHITE)
        restart_rect = restart_text.get_rect(center=(self.width//2, self.square_size//2 + 30))
        
        overlay = pygame.Surface((self.width, self.square_size))
        overlay.set_alpha(200)
        overlay.fill(self.BLACK)
        self.screen.blit(overlay, (0, 0))
        self.screen.blit(text, text_rect)
        self.screen.blit(restart_text, restart_rect)
        pygame.display.update()
    
    def get_human_move(self):
        """Gets a move from the human player."""
        current_col = 3  # Start hovering over middle column
        self.draw_hovering_piece(current_col, 1)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    # Move left
                    if event.key == pygame.K_LEFT and current_col > 0:
                        current_col -= 1
                        self.draw_hovering_piece(current_col, 1)
                    
                    # Move right
                    elif event.key == pygame.K_RIGHT and current_col < self.board.cols - 1:
                        current_col += 1
                        self.draw_hovering_piece(current_col, 1)
                    
                    # Drop piece
                    elif event.key in [pygame.K_RETURN, pygame.K_SPACE, pygame.K_DOWN]:
                        if self.board.is_valid_move(current_col):
                            return current_col
                
                # Mouse movement for hovering
                elif event.type == pygame.MOUSEMOTION:
                    col = event.pos[0] // self.square_size
                    if 0 <= col < self.board.cols:
                        current_col = col
                        self.draw_hovering_piece(current_col, 1)
                
                # Mouse click to drop piece
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col = event.pos[0] // self.square_size
                    if 0 <= col < self.board.cols and self.board.is_valid_move(col):
                        return col
    
    def show_difficulty_selection(self):
        """Shows a difficulty selection screen."""
        self.screen.fill(self.BLACK)
        
        title = self.big_bold_font.render("SELECT DIFFICULTY", True, self.WHITE)
        title_rect = title.get_rect(center=(self.width//2, self.height//6))
        self.screen.blit(title, title_rect)
        
        difficulties = ["Easy", "Medium", "Hard", "Expert"]
        button_height = 60
        button_width = 200
        button_spacing = 40
        
        buttons = []
        for i, diff in enumerate(difficulties):
            y_pos = self.height//3 + i * (button_height + button_spacing)
            button_rect = pygame.Rect(self.width//2 - button_width//2, y_pos, button_width, button_height)
            buttons.append((button_rect, diff.lower()))
            
            # Draw button
            color = self.GRAY
            pygame.draw.rect(self.screen, color, button_rect)
            pygame.draw.rect(self.screen, self.WHITE, button_rect, 2)  # Border
            
            # Button text
            text = self.font.render(diff, True, self.BLACK)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)
        
        pygame.display.update()
        
        # Wait for selection
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button_rect, difficulty in buttons:
                        if button_rect.collidepoint(mouse_pos):
                            return difficulty
    
    def handle_game_end(self):
        """Handles the end-of-game state and returns whether to restart."""
        waiting_for_restart = True
        while waiting_for_restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart
                        return True
                    elif event.key == pygame.K_ESCAPE:  # Quit
                        pygame.quit()
                        return False