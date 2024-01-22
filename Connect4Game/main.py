import Connect4Game
import DanielBatyrevAI as DanielAI
import copy
import func_timeout
"""this creates a list of the two "players" in this game, two instances of the DanielAI.RandomStrategy() """
competitor_list = [DanielAI.RandomStrategy(), DanielAI.RandomStrategy("alter ego")]

MAX_WAIT_TIME = 1
winners = list()
"""another instance of the RandomStrategy class"""
random_choice = DanielAI.RandomStrategy()
"""prints the numbers 1 through 1000"""
for game_nr in range(1000):
    print(game_nr + 1)
    """tie variable will chanhge to true if there is a tie"""
    tie = False
    """create an instance of the Connect4Game class"""
    game = Connect4Game.Connect4Game()
    """the whole time the game is going on this while loop creates a deepcopy of the game
    which will be fed into the Strategy() method of RandomStrategy class"""
    while game.winner is None:
        game_safety_copy = copy.deepcopy(game)
        try:
            """the func_timeout function runs the strategy function for as long as MAX_WAIT_TIME, 
            which is 1 and then performs a random move"""
            move = func_timeout.func_timeout(
                MAX_WAIT_TIME, competitor_list[game.current_player - 1].strategy, [game_safety_copy])
        except func_timeout.FunctionTimedOut:
            print(f'time out limit exceeded: {competitor_list[game.current_player - 1].name} performs random move')
            move = random_choice.strategy(game_safety_copy)
        game.make_move(move)
        """checks if there are any valid moves left and declares a tie if not"""
        if 0 == sum(map(game.is_valid_move, range(7))):
            tie = True
            break
            """adds a tie to the list of winners if there is a tie""""
    if tie:
        winners.append("tie")
    else:
         """adds the current winner to list of winners"""
        winners.append(competitor_list[game.current_player - 1].name)
"""reverses the competitor list so now "alter ego" would be first"""
    competitor_list.reverse()
"""adds the winners to a dictionary and then prints them"""
dictionary = {}
for item in winners:
    dictionary[item] = dictionary.get(item, 0) + 1

print(dictionary)
