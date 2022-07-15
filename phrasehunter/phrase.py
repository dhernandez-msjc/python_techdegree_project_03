class Phrase:

    def __init__(self, phrase: str) -> None:
        self.phrase = phrase.lower()

    def display(self, guesses: [str]) -> None:
        """
        Displays which of the letters of the phrase the user
        has guessed correctly, as well as the shape of the phrase.
        :param guesses: The user guesses
        :return: None, prints message
        """
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end='')
            else:
                print('_', end='')
        print()

    def check_guess(self, guess: str) -> bool:
        """
        Checks the user guess against the phrase to see if
        the guessed letter is in the phrase.
        :param guess: The letter the user is guessing.
        :return: bool representing True if the letter is in the
                 phrase, False otherwise.
        """
        return guess in self.phrase

    def check_complete(self, guesses: [str]) -> bool:
        """
        Checks if the phrase has been completely guessed.
        :param guesses: The list of letters the player has guessed.
        :return: True if all letters are in the guesses list,
                 False otherwise.
        """
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
