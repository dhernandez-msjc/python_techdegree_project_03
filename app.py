from phrasehunter.game import Game

if __name__ == '__main__':
    game = Game()
    game.start()
    print(game.active_phrase.phrase)
    game.active_phrase.display(game.guesses)
