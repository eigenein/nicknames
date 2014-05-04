#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

import argparse
import collections
import json
import os


def main(args):
    generate_model(args._in, args.out)


def generate_model(_in, out):
    "Generates model for the specified set file."

    print("Set: %s" % _in.name)

    print("Counting ngrams…")
    bigram_counter, trigram_counter = collections.Counter(), collections.Counter()
    for word in _in:
        word = word.strip().lower()
        if not word:
            continue
        for chars in trigrams(word):
            bigram_counter[chars[:2]] += 1
            trigram_counter[chars] += 1

    print("Generating model…")
    model, breakable, p_counter = collections.defaultdict(list), set(), collections.Counter()
    for chars, count in trigram_counter.items():
        if chars[2] != "$":
            p = count / bigram_counter[chars[:2]]
            p_counter[chars[:2]] += p
            model[chars[:2]].append((chars[2], round(p_counter[chars[:2]], 3)))
        else:
            breakable.add(chars[:2])

    model_name = os.path.splitext(os.path.basename(_in.name))[0]

    print("Writing %s…" % out.name)
    print("models = models or {}", file=out)
    print("""models["%s"] = {}""" % model_name, file=out)
    print("""models["%s"].p = %s""" % (model_name, json.dumps(model, indent=2)), file=out)
    print("""models["%s"].breakable = %s""" % (model_name, json.dumps(list(breakable), indent=2)), file=out)

    print("Done.")


def trigrams(word):
    "Generates trigrams for the specified word."

    current = "$$$"
    for char in word:
        current = current[1:] + char
        yield current
    yield current[1:] + "$"
    yield current[2:] + "$$"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in", dest="_in", metavar="FILE", required=True, type=argparse.FileType("rt"))
    parser.add_argument("-o", "--out", dest="out", metavar="FILE", required=True, type=argparse.FileType("wt"))
    args = parser.parse_args()
    main(args)
