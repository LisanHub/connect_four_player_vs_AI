import sys
import argparse
from board import Board
from ai import AIPlayer
from player import HumanPlayer
from gui import GameUI
from cli import CliUI
from game import Game

def parse_arguments():
    """Parse command line arguments to determine game mode."""
    parser = argparse.ArgumentParser(description='Connect Four Game')
    parser.add_argument('--cli', action='store_true', help='Run in command-line interface mode')
    return parser.parse_args()

def main():
    """Entry point for the game."""
    args = parse_arguments()
    
    # Import pygame only if using GUI mode
    if not args.cli:
        global pygame
        import pygame
    
    # Create the board
    board = Board()
    
    # Create the appropriate UI
    if args.cli:
        ui = CliUI(board)
    else:
        ui = GameUI(board) 
    
    # Main game loop with restart option
    play_again = True
    while play_again:
        # Get difficulty from UI
        difficulty = ui.show_difficulty_selection()
        
        # Create and start a new game
        game = Game(ui, ai_difficulty=difficulty)
        play_again = game.start()

if __name__ == "__main__":
    main()