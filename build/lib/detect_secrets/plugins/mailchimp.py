"""
This plugin searches for Mailchimp keys
"""
import re
from base64 import b64encode

import requests

from ..constants import VerifiedResult
from .base import RegexBasedDetector


class MailchimpDetector(RegexBasedDetector):
    """Scans for Mailchimp keys."""
    secret_type = 'Mailchimp Access Key'

    denylist = (
        re.compile(r'[0-9a-z]{32}-us[0-9]{1,2}'),
    )

    def verify(self, secret: str) -> VerifiedResult:  # pragma: no cover
        _, datacenter_number = secret.split('-us')

        response = requests.get(
            'https://us{}.api.mailchimp.com/3.0/'.format(
                datacenter_number,
            ),
            headers={
                'Authorization': b'Basic ' + b64encode(
                    'any_user:{}'.format(secret).encode('utf-8'),
                ),
            },
        )
        return (
            VerifiedResult.VERIFIED_TRUE
            if response.status_code == 200
            else VerifiedResult.VERIFIED_FALSE
        )
