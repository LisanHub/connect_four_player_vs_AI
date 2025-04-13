# Connect Four Game with Minimax AI

![Connect Four Icon](connect_four_icon.png)

A Python implementation of the classic Connect Four game featuring an intelligent AI opponent powered by the Minimax algorithm with alpha-beta pruning.

## Features

- **Interactive Gameplay**: Classic 7x6 Connect Four grid with intuitive controls
- **Customizable Interface**: Choose between a polished graphical interface (Pygame) or a terminal-based interface
- **Intelligent AI Opponent**: Four difficulty levels (Easy, Medium, Hard, Expert) to match your skill level
- **Advanced Algorithm**: Minimax with alpha-beta pruning and strategic evaluation functions
- **Game Physics**: Animated piece dropping with realistic behavior
- **Custom Game Icon**: Distinctive app icon for desktop environments
- **Win/Draw Detection**: Automatic detection of winning combinations and board-full draws
- **Restart Functionality**: Easily restart the game after completion

## Running the Game

### Using the Executable (Windows)

1. Navigate to the `dist` folder
2. Double-click on `main.exe` to launch the game
3. No installation required - the game runs immediately!

### From Source Code (All Platforms)

#### Requirements
- Python 3.6+
- NumPy
- Pygame (for graphical interface)

#### Installation

1. Clone the repository or download the files
2. Install the required packages:

```bash
pip install numpy pygame
```

3. Ensure the `connect_four_icon.png` file is in the same directory as the game files

#### How to Run

**Graphical User Interface (Default)**
```bash
python main.py
```

**Command Line Interface**
```bash
python main.py --cli
```

## How to Play

### GUI Mode
- **Select Column**: Use mouse movement or left/right arrow keys to select a column
- **Drop Piece**: Click the mouse or press Enter/Space/Down key to drop your piece
- **Restart Game**: Press 'R' when prompted after a game ends
- **Exit Game**: Press 'ESC' or close the window

### CLI Mode
- Enter column numbers (1-7) when prompted to drop your piece
- Follow the on-screen instructions for navigating the game

## Game Rules

1. Players take turns dropping colored discs into a 7-column, 6-row grid
2. The discs fall to the lowest available space in the selected column
3. The first player to form a horizontal, vertical, or diagonal line of four discs wins
4. If the grid fills up without a winner, the game is a draw

## AI Difficulty Levels

- **Easy**: Makes occasional random moves and may overlook winning opportunities, searches 1 move ahead
- **Medium**: Makes some strategic moves but can be beaten with planning, searches 3 moves ahead
- **Hard**: Makes strong strategic moves and rarely misses winning opportunities, searches 4 moves ahead
- **Expert**: Plays optimally using full algorithm capabilities, searches 6 moves ahead

## Technical Implementation

### Board Representation
The game uses a 2D NumPy array to represent the board, with:
- `0` representing empty cells
- `1` representing player pieces (red)
- `2` representing AI pieces (green)

### AI Algorithm Details
The AI implementation uses several advanced techniques:

#### Minimax Algorithm
- Recursively evaluates all possible future board states
- Creates a game tree where each node is a potential board state
- Assigns scores to terminal states (wins, losses, draws)
- Propagates scores up the tree, assuming optimal play by both players
- Time complexity is reduced through alpha-beta pruning

#### Alpha-Beta Pruning
- Optimization technique that significantly reduces the number of nodes evaluated
- Maintains two values (alpha and beta) to represent the minimum score the maximizing player is assured and the maximum score the minimizing player is assured
- Skips evaluating branches that cannot possibly influence the final decision
- Allows for deeper search depths in the same amount of time

#### Evaluation Function
The AI evaluates non-terminal board positions through a sophisticated heuristic:
- Prioritizes center column control (strategically stronger positions)
- Scores potential winning sequences (connected 2 and 3 pieces with open spaces)
- Assigns higher penalties to opponent's potential winning moves based on urgency
- Applies difficulty-based scoring adjustments to simulate different skill levels

### Game Interface
- Built using Pygame for the graphical version
- Clean, responsive UI with visual feedback
- Custom window icon for better desktop integration
- Animated piece dropping for a more engaging experience

## File Structure

- `main.py` - Main game logic and entry point
- `board.py` - Board representation and game state
- `ai.py` - AI player using Minimax algorithm
- `player.py` - Human player representation
- `gui.py` - Pygame-based graphical user interface
- `cli.py` - Command-line interface
- `connect_four_icon.png` - Custom game icon
- `main.exe` - Executable version (in `dist` folder)
- `README.md` - Project documentation

## Creating the Executable

The executable was created using PyInstaller with the following command:

```bash
pyinstaller --onefile --windowed --icon=connect_four_icon.ico main.py
```

## Troubleshooting the Executable

If you encounter issues with the executable:

1. Ensure your antivirus isn't blocking the execution
2. Try running as administrator
3. Make sure the `dist` folder contains all necessary game assets
4. If all else fails, run from source code as described above

## Extensibility

The modular design makes it easy to:
- Customize board dimensions
- Implement new AI algorithms
- Add multiplayer support
- Create custom themes or visual styles

## Credits

- AI strategy based on research papers on adversarial search and game theory
- Game rules following the classic Milton Bradley/Hasbro Connect Four game