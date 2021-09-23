from bot import Bot
from constants import *
import random

class RandomBot(Bot):
  def __init__(self):
    self.Dynamite = 0


  def make_move(self, gamestate):
      moveIndex = random.choice([0, 1, 2, 3, 4])
      if moveIndex == 4:
          self.Dynamite += 1

      if self.Dynamite >= NUM_DYNAMITE:
          moveIndex = random.choice([0, 1, 2, 3])

      Move = VALID_MOVES[moveIndex]
      return Move