from typing import List
from urllib.parse import urlparse
import os
import re


class ProfanityCheck:
    def __init__(self, censored_list: List[str] = None) -> None:
        self.censored_list = list(censored_list or [])
        self.load_words()

    '''
    Load profanity into censored words list
    '''
    def load_words(self) -> None:
        base_dir = os.path.dirname(__file__)
        profanity_list = os.path.join(base_dir, 'data', 'profanity_list.txt')

        with open(profanity_list, 'r') as words:
            self.censored_list = [line.strip() for line in words]

    '''
    Add a new word to the file
    '''
    def add_word(self, word: str) -> None:
        if word not in self.censored_list:
            self.censored_list.append(word)

            base_dir = os.path.dirname(__file__)
            profanity_list = os.path.join(base_dir, 'data', 'profanity_list.txt')
            with open(profanity_list, 'a') as file:
                file.write('\n' + word)
                file.close()

    '''
    Check if player's history is dirty
    '''
    def is_dirty(self, input_urls: dict) -> dict:
        occurrences = dict()

        # any(word in input_url for word in self.censored_list)
        for key, value in input_urls.items():
            to_parse = urlparse(value).geturl()
            word = re.search(r'\.(.*)\.', to_parse, re.IGNORECASE).group(1)
            for censored_word in self.censored_list:
                if word.find(censored_word) != -1:
                    if to_parse in occurrences:
                        occurrences[to_parse] += 1
                    else:
                        occurrences[to_parse] = 1

        return occurrences
