import re

from .base import RegexBasedDetector


class MailgunKeyDetector(RegexBasedDetector):
    """
    Scans for Mailgun Auth Token.

    This checks for Mailgun Auth Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Mailgun Auth Token'

    denylist = [
        re.compile(r'key-[0-9a-zA-Z]{32}')
    ]
