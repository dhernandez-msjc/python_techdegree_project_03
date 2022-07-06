from phrases import PHRASES
from random import choice

NUMBER_OF_PHRASES = 5


class Game:

    def __init__(self) -> None:
        self.missed = 0
        self.phrases = self._create_phrases()
        self.active_phrases = None
        self.guesses = [" "]

    def run(self) -> None:
        pass

    def _create_phrases(self) -> []:
        selected_phrases = []

        for _ in range(NUMBER_OF_PHRASES):
            pass
        return selected_phrases
