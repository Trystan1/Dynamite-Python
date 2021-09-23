from bot import Bot

class StrawmanBot(Bot):
    def __init__(self):
        pass

    def make_move(self, gamestate):

        length = len(gamestate["rounds"])
        if length >= 500 and length <= 1000:
            Move = 'R'
        elif length >= 1000 and length <= 1500:
            Move = 'S'
        elif length >= 1500 and length <= 2000:
            Move = 'P'
        elif length >= 2000 and length <= 2100:
            Move = 'D'
        else:
            Move = 'W'
        return Move
