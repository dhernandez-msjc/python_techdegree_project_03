from phrasehunter.phrase import Phrase
from phrasehunter.phrases import PHRASES
from random import choice
from string import ascii_lowercase

NUMBER_OF_PHRASES = 5


class Game:

    def __init__(self) -> None:
        self.missed = 0
        self.phrases = None
        self.active_phrase = None
        self.guesses = [' ']

    def get_random_phrase(self) -> Phrase:
        random_phrase = choice(self.phrases)
        self.phrases.remove(random_phrase)
        return Phrase(random_phrase)

    def welcome(self) -> None:
        MAIN_MESSAGE = "Welcome to Phrase Hunter"
        HIDDEN_MESSAGE = "t_ee_ou_e"
        BORDER = '=' * (len(MAIN_MESSAGE) + 10)

        print(BORDER)
        print(f'{MAIN_MESSAGE:^{len(BORDER)}}')
        print(f'{HIDDEN_MESSAGE:^{len(BORDER)}}')
        print(BORDER)

    def get_guess(self):
        return self._validate_user_guess()

    def start(self) -> None:
        self.phrases = self._create_phrases()
        self.active_phrase = self.get_random_phrase()

        self.welcome()
        print(f'Number missed: {self.missed}')
        self.active_phrase.display(self.guesses)

        user_guess = self.get_guess()
        self.guesses.append(user_guess)

    def game_over(self):
        pass

    @staticmethod
    def _create_phrases() -> []:
        selected_phrases = []

        for _ in range(NUMBER_OF_PHRASES):
            available_phrases = (set(PHRASES) - set(selected_phrases))
            random_phrase = choice(list(available_phrases))
            selected_phrases.append(random_phrase)
        return selected_phrases

    @staticmethod
    def _validate_user_guess() -> str:
        user_input = input('Enter a letter: ')

        while user_input not in ascii_lowercase or len(user_input) != 1:
            print('Invalid entry. ')
            print('Please enter a lower-case letter between a - z.\n')
            user_input = input('Enter a letter: ')
        return user_input
