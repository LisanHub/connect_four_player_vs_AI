# Connect Four Game with Minimax AI

This is a Python implementation of the classic Connect Four game where a human player competes against an AI using the Minimax algorithm.

## Features

- 7x6 Connect Four grid
- Choose between graphical (Pygame) or terminal-based interface
- Four AI difficulty levels (Easy, Medium, Hard, Expert)
- Minimax algorithm with alpha-beta pruning
- Win detection in all directions (horizontal, vertical, diagonal)
- Draw detection when board is full
- Restart option after game completion

## Requirements

- Python 3.6+
- NumPy
- Pygame (for graphical interface)

## Installation

1. Clone the repository or download the files
2. Install the required packages:

```bash
pip install numpy pygame
```

## How to Run

### Graphical User Interface (Default)

```bash
python main.py
```

### Command Line Interface

```bash
python main.py --cli
```

## How to Play

- GUI Mode: 
  - Use the mouse or arrow keys to select a column
  - Click or press Enter/Space to drop your piece
  - Press 'R' to restart after a game ends

- CLI Mode:
  - Enter column numbers (1-7) to drop your piece
  - Follow the on-screen prompts

## Game Rules

1. Players take turns dropping colored discs into a 7-column, 6-row grid
2. The discs fall to the lowest available space in the selected column
3. The first player to form a horizontal, vertical, or diagonal line of four discs wins
4. If the grid fills up without a winner, the game is a draw

## File Structure

- `main.py` - Main game logic and entry point
- `board.py` - Board representation and game state
- `ai.py` - AI player using Minimax algorithm
- `player.py` - Human player representation
- `gui.py` - Pygame-based graphical user interface
- `cli.py` - Command-line interface
- `README.md` - Project documentation

## How It Works

### Board Representation
The game uses a 2D NumPy array to represent the board, with:
- `0` representing empty cells
- `1` representing player pieces
- `2` representing AI pieces

### AI Algorithm
The AI uses the Minimax algorithm with alpha-beta pruning to find the optimal move:
1. It simulates all possible moves and their outcomes
2. Each board position is evaluated using a heuristic function
3. The AI chooses the move that maximizes its chances of winning
4. The difficulty level determines how many moves ahead the AI will look

### Evaluation Function
The AI evaluates board positions by:
- Counting sequences of 2, 3, and 4 pieces
- Favoring center column positions (strategically stronger)
- Blocking opponent's potential winning moves