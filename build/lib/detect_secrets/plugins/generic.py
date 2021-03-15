import re

from .base import RegexBasedDetector


class GenericKeyDetector(RegexBasedDetector):
    """
    Scans for Generic Keys/Token.

    This checks for Generic Keys/Token by determining whether the denylisted
    lines are present in the analyzed string.
    """

    secret_type = 'Generic Secret Key'

    denylist = [
        re.compile(r"(?:[s|S][e|E][c|C][r|R][e|E][t|T].*)(['|\"][0-9a-zA-Z]{32,45}['|\"])"),
        re.compile(r"(?:[a|A][p|P][i|I][_]?[k|K][e|E][y|Y].*)(['|\"][0-9a-zA-Z]{32,45}['|\"])"),
    ]
