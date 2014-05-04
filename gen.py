#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

import argparse
import collections
import json
import os


def main(args):
    generate_model(args._in, args.out, args.n)


def generate_model(_in, out, n):
    "Generates model for the specified set file."

    print("Set: %s" % _in.name)

    print("Counting ngrams…")
    mgram_counter, ngram_counter = collections.Counter(), collections.Counter()
    for word in _in:
        word = word.strip().lower()
        if not word:
            continue
        for chars in ngrams(word, n):
            mgram_counter[chars[:-1]] += 1
            ngram_counter[chars] += 1

    print("Generating model…")
    model, breakable, p_counter = collections.defaultdict(list), set(), collections.Counter()
    for chars, count in ngram_counter.items():
        if chars[-1] != "$":
            p = count / mgram_counter[chars[:-1]]
            p_counter[chars[:-1]] += p
            model[chars[:-1]].append((chars[-1], round(p_counter[chars[:-1]], 3)))
        else:
            breakable.add(chars[:-1])

    model_name = os.path.splitext(os.path.basename(_in.name))[0]

    print("Writing %s…" % out.name)
    print("models = models or {}", file=out)
    print("""models["%s"] = {}""" % model_name, file=out)
    print("""models["%s"].p = %s""" % (model_name, json.dumps(model, indent=2)), file=out)
    print("""models["%s"].breakable = %s""" % (model_name, json.dumps(list(breakable), indent=2)), file=out)

    print("Done.")


def ngrams(word, n):
    "Generates n-grams for the specified word."

    current = "$" * n
    for char in word:
        current = current[1:] + char
        yield current
    for i in range(1, n):
        yield current[i:] + "$" * i


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--in", dest="_in", metavar="FILE", required=True, type=argparse.FileType("rt"))
    parser.add_argument("-o", "--out", dest="out", metavar="FILE", required=True, type=argparse.FileType("wt"))
    parser.add_argument("-n", dest="n", metavar="N", default=3, type=int)
    args = parser.parse_args()
    main(args)
