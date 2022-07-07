class Phrase:

    def __init__(self, phrase: str) -> None:
        self.phrase = phrase.lower()

    def display(self, guesses) -> None:
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end='')
            else:
                print('_', end='')
        print()

    def check_letter(self) -> bool:
        pass

    def check_complete(self) -> bool:
        pass
