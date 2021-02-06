from typing import List
from urllib.parse import urlparse
import os
import re


class SocialCheck:
    def __init__(self, socials_list: List[str] = None) -> None:
        self.socials_list = list(socials_list or [])
        self.load_socials()
    '''
    Load socials
    '''
    def load_socials(self) -> None:
        base_dir = os.path.dirname(__file__)
        socials_list = os.path.join(base_dir, 'data', 'social_media_list.txt')

        with open(socials_list, 'r') as sites:
            self.socials_list = [line.strip() for line in sites]

    '''
    Build dictionary of available social media sites to look for,
    Once found, operate on each url per it's base platform,
    We will be weighting ea. site based on the content provided
    '''
    def find_origin(self, social_media: dict) -> dict:
        socials = dict()

        # ea. social media site gets it's own index
        for item in self.socials_list:
            socials[item] = []

        # based on history, fill in ea. unique index
        for key, value in social_media.items():
            to_parse = urlparse(value).geturl()
            word = re.search(r'\.(.*)\.', to_parse, re.IGNORECASE).group(1)
            if word == "instagram":
                socials["instagram"].append(to_parse)
            elif word == "facebook":
                socials["facebook"] = [to_parse]
            elif word == "twitter":
                socials["twitter"] = [to_parse]
            elif word == "parler":
                socials["parler"] = [to_parse]

        return socials

    # def is_instagram(self):
    # def is_facebook(self):
    # def is_twitter(self):
    # def is_parler(self):
