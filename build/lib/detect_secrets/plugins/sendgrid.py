import re

from .base import RegexBasedDetector


class SendgridKeyDetector(RegexBasedDetector):
    """
    Scans for Sendgrid API Token.

    This checks for Sendgrid API Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Sendgrid API Token'

    denylist = [
        re.compile(r'SG\\.[a-zA-Z0-9]{22}\\.[a-zA-Z0-9]{43}')
    ]
