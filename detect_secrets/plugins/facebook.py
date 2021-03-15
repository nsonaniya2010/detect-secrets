import re

from .base import RegexBasedDetector


class FacebookKeyDetector(RegexBasedDetector):
    """
    Scans for Facebook Auth Token.

    This checks for Facebook Auth Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Facebook Oauth Token'

    denylist = [
        re.compile(r'EAACEdEose0cBA[0-9A-Za-z]+'),
    ]
