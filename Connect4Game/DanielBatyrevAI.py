"""imports the Connect4Game file"""
import Connect4Game as Game
"""imports python random library"""
import random

"""class RandomStrategy takes in the Connect4GameStrategy() class"""
class RandomStrategy(Game.Connect4GameStrategy):
    def __init__(self, name="Daniel Batyrev"):
        """sets name to Daniel Batyrev"""
        self.name = name

    @classmethod
    def strategy(cls, game_safety_copy):
        """this method accepts a deepcopy of the current game and makes a list of valid moves"""
        valid_moves = list()
        """looping through all the columns, it calls is_valid_move() to check the validity 
        of the move and then if it is valid adds it to the list of possible moves"""
        for col in range(7):
            if game_safety_copy.is_valid_move(col):
                valid_moves.append(col)
                """picks a random move from the list of possible moves"""
        return random.choice(valid_moves)
