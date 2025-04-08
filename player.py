class HumanPlayer:
    """
    Represents a human player in the Connect Four game.
    """
    def __init__(self, player_num=1):
        self.player_num = player_num
        
    def get_move(self, board, ui):
        """
        Gets a move from the human player using the UI.
        Returns the column to drop the piece.
        """
        return ui.get_human_move()