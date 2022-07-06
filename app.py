from phrasehunter.phrase import Phrase
from phrasehunter.game import Game


if __name__ == '__main__':
    game = Game()
    game.run()

    for phrase in game.phrases:
        print(phrase)
