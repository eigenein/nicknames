#!/usr/bin/env python3
# coding: utf-8

from __future__ import print_function

import argparse
import collections
import json
import os


def main(args):
    for set_file in args.set_files:
        generate_model(set_file)


def generate_model(set_file):
    "Generates model for the specified set file."

    print("Set: %s" % set_file.name)
    
    print("Counting ngrams…")
    bigram_counter, trigram_counter = collections.Counter(), collections.Counter()
    for word in set_file:
        word = word.strip().lower()
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

    model_name = os.path.splitext(os.path.basename(set_file.name))[0]
    coffee_name = os.path.join("coffee", "models%s%s%scoffee" % (os.extsep, model_name, os.extsep))

    print("Writing %s…" % coffee_name)
    with open(coffee_name, "wt", encoding="utf-8") as coffee:
        print("models = models or {}", file=coffee)
        print("""models["%s"] = {}""" % model_name, file=coffee)
        print("""models["%s"].p = %s""" % (model_name, json.dumps(model, indent=2)), file=coffee)
        print("""models["%s"].breakable = %s""" % (model_name, json.dumps(list(breakable), indent=2)), file=coffee)

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
    parser.add_argument(dest="set_files", nargs=argparse.REMAINDER, type=argparse.FileType("rt"))
    args = parser.parse_args()
    main(args)
