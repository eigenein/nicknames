#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import argparse


def main(args):
    for set_file in args.set_files:
        generate_model(set_file)


def generate_model(set_file):
    print(set_file.name)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="set_files", nargs=argparse.REMAINDER, type=argparse.FileType("rt"))
    args = parser.parse_args()
    main(args)
