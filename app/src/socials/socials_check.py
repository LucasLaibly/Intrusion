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
    def find_social_media(self, social_media: dict) -> dict:
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
                socials["facebook"].append(to_parse)
            elif word == "twitter":
                socials["twitter"].append(to_parse)
            elif word == "parler":
                socials["parler"].append(to_parse)
            elif word == "onlyfans":
                socials["onlyfans"].append(to_parse)

        return socials

    '''
    After searching for each of the designated social media sites, look to sort
    and condense findings -- specifically, look to determine frequency of site
    visited per sort
    '''
    def check_frequencies(self, social_media: dict) -> dict:
        frequency = dict()

        if not social_media:
            frequency["empty"] = True
        else:
            for item in social_media:
                for index in social_media[item]:
                    print(index)
                    if index in frequency:
                        frequency[index] += 1
                    else:
                        frequency[index] = 1
        return frequency
