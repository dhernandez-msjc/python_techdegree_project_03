# Create your Game class logic in here.
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
        return selected_phrases
