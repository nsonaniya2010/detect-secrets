import re

from .base import RegexBasedDetector


class GoogleFCMKeyDetector(RegexBasedDetector):
    """
    Scans for Google FCM Token.

    This checks for Google FCM Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Google FCM Token'

    denylist = [
        re.compile(r'AAAA[a-zA-Z0-9_-]{7}:[a-zA-Z0-9_-]{140}'),
    ]
