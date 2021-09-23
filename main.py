from pprint import pprint

from game import Game
from paperbot import PaperBot
from rockbot import RockBot
from tjbot import TJBot
from tjbotold import TJBotOld
from strawmanbot import StrawmanBot
from randombot import RandomBot

def main():
  # bot1 = StrawmanBot()
  # bot1 = TJBotOld()
  bot1 = RandomBot()
  # bot1 = PaperBot()
  # bot2 = StrawmanBot()
  bot2 = TJBot()
  game = Game(bot1, bot2)
  result = game.play()
  pprint(result)


if __name__ == '__main__':
  main()