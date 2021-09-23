from bot import Bot
import random
from constants import *


class TJBot(Bot):
    def __init__(self):
        self.__Dynamite = NUM_DYNAMITE
        self.__repeat_flag = False
        self.__repeat_value = ''
        self.__buffer = ['', '', '']
        self.__cheeky_flag = False
        self.__cheeky_counter = 0
        self.__p2_Dynamite = NUM_DYNAMITE
        self.__D_weight = NUM_DYNAMITE
        self.__W_weight = NUM_DYNAMITE

    def make_move(self, gamestate):

        self.__length = len(gamestate["rounds"])

        self.check_4_repeat(gamestate)

        self.check_4_dynamite(gamestate)

        if self.__repeat_flag:
            Move = TJBot.beat_const_bot(self)
        elif self.__cheeky_flag:
            Move = TJBot.cheeky_method(self)
        else:
            cheeky = random.randint(0, 5)
            if cheeky == 0 and self.__Dynamite >= 2:
                # method to make a run of 3 P's, followed by 2 Dynamites
                self.__cheeky_flag = True
                Move = 'P'
                self.__cheeky_counter += 1
            else:
                Move = TJBot.make_random_move(self)
        # print(f'I have {self.__Dynamite} left')


        return Move

    def check_4_repeat(self, gamestate):

        if self.__length >= 1:
            # shift and fill in the the 3 item long list 'buffer'
            self.__buffer[0] = self.__buffer[1]
            self.__buffer[1] = self.__buffer[2]
            self.__buffer[2] = gamestate["rounds"][self.__length - 1]["p2"]
            if self.__buffer[0] == self.__buffer[1] and self.__buffer[0] == self.__buffer[2]:
                self.__repeat_flag = True
                self.__repeat_value = self.__buffer[2]
            else:
                self.__repeat_flag = False

    def beat_const_bot(self):
        if self.__repeat_value == 'R':
            Move = 'P'
        elif self.__repeat_value == 'P':
            Move = 'S'
        elif self.__repeat_value == 'S':
            Move = 'R'
        elif self.__repeat_value == 'D':
            Move = 'W'
        else:
            Move = 'R'

        return Move

    def make_random_move(self):

        Move = random.choices(VALID_MOVES, weights=(NUM_DYNAMITE, NUM_DYNAMITE, NUM_DYNAMITE, self.__W_weight, self.__D_weight), k=1)
        print(Move[0])
        if Move[0] == 'D': self.__Dynamite -= 1

        return Move[0]

    def cheeky_method(self):
        if self.__cheeky_flag and self.__cheeky_counter < 3:
            Move = 'P'
            self.__cheeky_counter += 1
        elif self.__cheeky_flag and self.__cheeky_counter < 5:
            Move = 'D'
            self.__Dynamite -= 1
            self.__cheeky_counter += 1
        elif self.__cheeky_counter >= 5:
            self.__cheeky_flag = False
            self.__cheeky_counter = 0
            Move = TJBot.make_random_move(self)
        return Move

    def check_4_dynamite(self, gamestate):

        self.__D_weight = self.__Dynamite

        # nameList = ["R", "P", "S", "W", "D"]
        # outputlist = random.choices(nameList, weights=(NUM_DYNAMITE, NUM_DYNAMITE, NUM_DYNAMITE, self.__W_weight, self.__D_weight), k=10)
        # R = 0
        # P = 0
        # S = 0
        # W = 0
        # D = 0
        # for i in range(0, len(outputlist)):
        #     if outputlist[i] == 'R': R += 1
        #     if outputlist[i] == 'P': P += 1
        #     if outputlist[i] == 'S': S += 1
        #     if outputlist[i] == 'W': W += 1
        #     if outputlist[i] == 'D': D += 1

        # print(f'Outputs are: R:{R}, P:{P}, S:{S}, W:{W}, D:{D}')
        # print(f'Weights are: R:{NUM_DYNAMITE}, P:{NUM_DYNAMITE}, S:{NUM_DYNAMITE}, W:{self.__W_weight}, D:{self.__D_weight}')
        # print(f'I have {self.__Dynamite} left')
        # print(f'the enemy has {self.__p2_Dynamite} Dynamite remaining')

        if self.__length >= 1 and gamestate["rounds"][self.__length - 1]["p2"] == 'D':
            self.__p2_Dynamite -= 1
            if self.__p2_Dynamite <= 1:
                self.__W_weight = 0
            else:
                self.__W_weight -= 1