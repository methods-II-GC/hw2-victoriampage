#!/usr/bin/env python
"""Read in data from a file and split the data into training, dev, and test sets."""


import argparse

from typing import Iterator, List


def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines

def main(args: argparse.Namespace) -> None:
    # TODO: do the work here.

    ...


if __name__ == "__main__":
    # TODO: declare arguments.
    # TODO: parse arguments and pass them to `main`.
    ...
