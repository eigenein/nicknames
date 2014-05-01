#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import argparse
import json
import os


def main(args):
    for set_file in args.set_files:
        generate_model(set_file)


def generate_model(set_file):
    "Generates model for the specified set file."

    print("Set: %s" % set_file.name)
    basename = os.path.basename(set_file.name)
    coffee_name = os.path.join("coffee", "%s%scoffee" % (os.path.splitext(basename)[0], os.extsep))
    
    print("Generating %s…" % coffee_name)
    model = {}
    for word in set_file:
        word = word.strip()


def trigrams(word):
    "Generates trigrams for the specified word."

    current = "$" * 3
    for char in word:
        current = current[1:] + char
        yield current
    yield current[1:] + "$"
    yield current[2:] + "$$"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="set_files", nargs=argparse.REMAINDER, type=argparse.FileType("rt"))
    args = parser.parse_args()
    main(args)
