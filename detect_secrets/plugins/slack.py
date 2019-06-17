"""
This plugin searches for Slack tokens
"""
from __future__ import absolute_import

import re

from .base import RegexBasedDetector


class SlackDetector(RegexBasedDetector):

    secret_type = 'Slack Token'

    denylist = (
        # Slack Token
        re.compile(r'xox(?:a|b|p|o|s|r)-(?:\d+-)+[a-z0-9]+', flags=re.IGNORECASE),
        # Slack Webhooks
        re.compile(
            r"""
            https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}
            """,
            flags=re.IGNORECASE | re.VERBOSE,
        ),
    )
