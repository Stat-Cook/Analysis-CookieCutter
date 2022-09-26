import os

from .cutter import cutter


def main():
    wp = int(input("WP [1]:") or 1)
    analysis = int(input("Analysis [1]:") or 1)

    return cutter(wp, analysis)
