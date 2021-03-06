import argparse

from .. import baseline
from ...exceptions import UnableToReadBaselineError
from .common import initialize_plugin_settings
from .common import valid_path


def add_baseline_option(parser: argparse.ArgumentParser, help: str) -> None:
    parser.add_argument(
        '--baseline',
        nargs=1,
        metavar='FILENAME',
        type=valid_path,
        help=help,
    )


def parse_args(args: argparse.Namespace) -> None:
    if not hasattr(args, 'baseline') or not args.baseline:
        return initialize_plugin_settings(args)

    try:
        loaded_baseline = baseline.load_from_file(args.baseline[0])
    except UnableToReadBaselineError:
        raise argparse.ArgumentTypeError('Unable to read baseline.')

    try:
        args.baseline_filename = args.baseline[0]
        args.baseline_version = loaded_baseline['version']
        args.baseline = baseline.load(loaded_baseline, filename=args.baseline_filename)
    except KeyError:
        raise argparse.ArgumentTypeError('Invalid baseline.')
