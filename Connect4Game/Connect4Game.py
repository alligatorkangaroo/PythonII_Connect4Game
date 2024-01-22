from abc import (ABC, abstractmethod)

"""creates a class for the strategy of the game"""
class Connect4GameStrategy(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def strategy(self, game_safety_copy):
        ...

"""this is the class for the moves of the game"""
class Connect4Game:
    def __init__(self):
        """in the init we create the logic for the board which is 7 wide and 6 tall"""
        self.board = [[0] * 7 for _ in range(6)]
        """the current player variable, which changes each turn to keep track of whos turn it is"""
        self.current_player = 1
         """the self.winner will remain none until someone has won the game"""
        self.winner = None

    def is_valid_move(self, column):
         """checks if the move made is valid and returns false if not"""
        if not (0 <= column < 7):
            return False
        return self.board[0][column] == 0

    def make_move(self, column):
         """first checks that the move is valid and that the game is still going on"""
        if not self.is_valid_move(column) or self.winner is not None:
            return
 """loops through the rows from top to bottom until it finds the highest empty 
 spot and sets that to the current player"""
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                 """calls check_winner to see if the move is a winning move and if not, 
                 sets current_player to next players turn"""
                if self.check_winner(row, column):
                    self.winner = self.current_player
                else:
                    self.current_player = 3 - self.current_player
                return

    def check_winner(self, row, col):
         """calls check_line to check if there is four in a row in any direction from the piece and returns 
         if there is a winner. the directions are up, down, right and left of the current piece, each is run through
         the check_line method."""
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        results = [self.check_line(row, col, dr, dc) for dr, dc in directions]
        return any(results)

    def check_line(self, row, col, dr, dc):
         """this is the function which contains the logic for checking if there is a win"""
        count = 0
        row = row - dr * 3
        col = col - dc * 3
    """this for loop goes along whichever direction it is iterating on and adds 1 for every piece that is the 
    same color as the current piece and if there are four in a row it returns true, otherwise not"""
        for _ in range(7):
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
            row += dr
            col += dc

        return False
