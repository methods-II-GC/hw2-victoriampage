#!/usr/bin/env python3
"""Read in data from a file and split into training, dev, and test sets."""


import argparse
import random

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


# writes section of the data to a path
def write_tag(path: str, set):
    with open(path, "w") as file:
        for line in set:
            #print(line)
            #print(words)
            for word in line: #found some weirdness at the end of each run, not sure what it is
                if type(word) == list:
                    file.writelines(word)
                    file.writelines("\n")


def main(args: argparse.Namespace) -> None:
    # TODO: do the work here.
    corpus = list(read_tags(args.input))

    #Add seed and randomize
    seed = args.seed
    random.seed(seed)
    random.shuffle(corpus)

    eighty = int(len(corpus) * 0.8)
    ninety = int(len(corpus) * 0.9)

    train_data = corpus[:eighty]
    dev_data = corpus[eighty:ninety]
    test_data = corpus[ninety:]

    write_tag(args.train, train_data)
    write_tag(args.dev, dev_data)
    write_tag(args.test, test_data)
    ...


if __name__ == "__main__":
    # TODO: declare arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str)

    parser.add_argument("train", type=str)

    parser.add_argument("dev", type=str)

    parser.add_argument("test", type=str)

    parser.add_argument(
        "--seed", type=int, required=True, help="Seed is required.")

    # TODO: parse arguments and pass them to `main`.
    main(parser.parse_args())
