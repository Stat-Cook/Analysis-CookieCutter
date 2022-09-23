"""
Implementation of the csv_2_tsv CLI interface.
"""

import argparse

from analysis_cli.cutter import cutter


def analysis_dir():
    """
    CLI to the csv_2_tsv.spider function.
    Returns:
        int
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-wp", "--work_package", help='Relevant Work Package to add analysis folders to',
                        default="1", nargs="?", type=int)

    parser.add_argument("-a", "--analysis", help='Relevant Analysis to add',
                        default="1", nargs="?", type=int)

    parser.add_argument("-r", "--root", help='Root to write folders from',
                        default=".", nargs="?")

    parser.add_argument("-v", "--verbose",
                        action = "store_true",
                        help='Turn on verbose logging [optional]')

    args = parser.parse_args()

    val = cutter(args.work_package, args.analysis, args.root)

    return val
