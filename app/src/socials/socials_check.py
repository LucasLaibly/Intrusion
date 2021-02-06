from typing import List
from urllib.parse import urlparse
import os
import re

class SocialCheck:
    def __init__(self, socials_list: List[str] = None) -> None:
        self.socials_list = list(socials_list or [])
        self.load_socials()

    def load_socials(self) -> None:
        base_dir = os.path.dirname(__file__)
        socials_list = os.path.join(base_dir, 'data', 'social_media_list.txt')

        with open(socials_list, 'r') as sites:
            self.socials_list = [line.strip() for line in sites]