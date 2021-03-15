import re

from .base import RegexBasedDetector


class GoogleKeyDetector(RegexBasedDetector):
    """
    Scans for Google Auth/API Token.

    This checks for Google Auth/API Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Google Auth/API Token'

    denylist = [
        re.compile(regexp)
        for regexp in (
            r'AIza[0-9A-Za-z\\-_]{35}',
            r'\"type\": \"service_account\"',
            r'ya29\\.[0-9A-Za-z\\-_]+',
        )
    ]
