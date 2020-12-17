from typing import List, Sequence
import os


class ProfanityCheck:
    def __init__(self, censored_list: Sequence[str] = None) -> None:
        self.censored_list = list(censored_list or [])
        self.load_words()

    def load_words(self) -> None:
        base_dir = os.path.dirname(__file__)
        profanity_list = os.path.join(base_dir, 'data', 'profanity_list.txt')

        with open(profanity_list, 'r') as words:
            self.censored_list = [line.strip() for line in words]

    def is_dirty(self, input_url: str) -> bool:
        # any(word in input_url for word in self.censored_list)
        if input_url in self.censored_list:
            return True
        else:
            return False
