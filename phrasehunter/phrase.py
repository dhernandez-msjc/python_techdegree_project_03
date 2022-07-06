# Create your Phrase class logic here.
class Phrase:

    def __init__(self, phrase: str) -> None:
        self.phrase = phrase.lower()

    def display(self) -> None:
        pass

    def check_letter(self) -> bool:
        pass

    def check_complete(self) -> bool:
        pass

    def _create_phrases(self) -> None:
        phrases = [
            'hello world',
            'to infinity and beyond',
            'hang on lady we going for a ride',
            'i feel invincible',

        ]