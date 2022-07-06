from phrasehunter.phrase import Phrase
from phrasehunter.game import Game


if __name__ == '__main__':
    phrase = Phrase('Life is like a box of chocolates')
    print(phrase.phrase)
    game = Game()
    game.run()
