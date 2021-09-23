from bot import Bot
import random
from constants import *


class TJBotOld(Bot):
    def __init__(self):
        self.Dynamite = 0
        self.repeat_flag = False
        self.repeat_value = ''
        self.buffer = ['', '', '']

    def make_move(self, gamestate):

        self.check_4_repeat(gamestate)
        if self.repeat_flag:
            Move = TJBotOld.beat_const_bot(self)
        else:
            Move = TJBotOld.make_random_move(self)

        return Move

    def check_4_repeat(self, gamestate):
        length = len(gamestate["rounds"])
        if length >= 1:
            # shift and fill in the the 3 item long list 'buffer'
            self.buffer[0] = self.buffer[1]
            self.buffer[1] = self.buffer[2]
            self.buffer[2] = gamestate["rounds"][length - 1]["p2"]
            if self.buffer[0] == self.buffer[1] and self.buffer[0] == self.buffer[2]:
                self.repeat_flag = True
                self.repeat_value = self.buffer[2]
            else:
                self.repeat_flag = False

    def beat_const_bot(self):
        if self.repeat_value == 'R':
            Move = 'P'
        elif self.repeat_value == 'P':
            Move = 'S'
        elif self.repeat_value == 'S':
            Move = 'R'
        elif self.repeat_value == 'D':
            Move = 'W'
        else:
            Move = 'R'

        return Move

    def make_random_move(self):
        moveIndex = random.choice([0, 1, 2, 3, 4])
        if moveIndex == 4:
            self.Dynamite += 1

        if self.Dynamite >= NUM_DYNAMITE:
            moveIndex = random.choice([0, 1, 2, 3])

        Move = VALID_MOVES[moveIndex]
        return Move
