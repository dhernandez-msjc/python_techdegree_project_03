from phrasehunter.phrases import PHRASES
from random import choice

NUMBER_OF_PHRASES = 5


class Game:

    def __init__(self) -> None:
        self.missed = 0
        self.phrases = self._create_phrases()
        self.active_phrases = None
        self.guesses = [" "]

    def get_random_phrase(self) -> str:
        random_phrase = choice(self.phrases)
        self.phrases.remove(random_phrase)
        return random_phrase

    def welcome(self) -> None:
        pass

    def get_guess(self):
        pass

    def game_over(self):
        pass

    def start(self) -> None:
        pass

    @staticmethod
    def _create_phrases() -> []:
        selected_phrases = []

        for _ in range(NUMBER_OF_PHRASES):
            available_phrases = (set(PHRASES) - set(selected_phrases))
            random_phrase = choice(list(available_phrases))
            selected_phrases.append(random_phrase)
        return [phrase.lower() for phrase in selected_phrases]
