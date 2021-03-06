from collections.abc import Iterator
from typing import Any
from typing import Sequence

from . import io
from ..core.secrets_collection import SecretsCollection


def get_secret_iterator(baseline: SecretsCollection) -> 'BidirectionalIterator':
    """
    :returns: (index, filename, secret)
    """
    unlabelled_secrets = [
        secret
        for _, secret in baseline
        if secret.is_secret is None
    ]

    if not unlabelled_secrets:
        io.print_message('Nothing to audit!')
        return BidirectionalIterator([])

    return BidirectionalIterator(unlabelled_secrets)


class BidirectionalIterator(Iterator):
    def __init__(self, collection: Sequence):
        self.collection = collection
        self.index = -1  # Starts on -1, as index is increased _before_ getting result
        self.step_back_once = False

    def __next__(self) -> Any:
        if self.step_back_once:
            self.index -= 1
            self.step_back_once = False
        else:
            self.index += 1

        if self.index < 0:
            raise StopIteration

        try:
            result = self.collection[self.index]
        except IndexError:
            raise StopIteration

        return result

    def next(self) -> Any:  # pragma: no cover
        return self.__next__()

    def step_back_on_next_iteration(self) -> None:
        self.step_back_once = True

    def can_step_back(self) -> bool:
        return self.index > 0

    def __iter__(self) -> 'BidirectionalIterator':  # pragma: no cover
        return self
