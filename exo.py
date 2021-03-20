#!/usr/bin/env python
# -*- coding: utf-8 -*-

# %% [markdown]
# # Compter le nombre de mot dans un fichier
#
# ## Comment faire ? Quelles sont les différentes étapes ?
import argparse
import sys
import os
from collections import Counter


def get_script_path(for_file = None):
    path = os.path.dirname(os.path.realpath(sys.argv[0] or 'something'))
    return path if not for_file else os.path.join(path, for_file)


def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", help="choose file in same directory that script file")
    args = parser.parse_args()
    
    return args
    

def count_most_frequent_word(file_path):
    freq = {}
    for part in open(file_path).read().lower().split():
        word = "".join(c for c in part if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0)

    cx = 0
    wd = ""
    for w, c in freq.items():
        if c > cx:
            cx = c
            wd = w
    print(wd, cx)

def count(file_path):
    test = Counter(open(file_path).read().lower().split()) 
    
    most_occur = test.most_common(1) 
    print(most_occur)
    

def main():
    args = command_line()
    filename = args.filename if args.filename else "cgu.txt"
    file_path = get_script_path(filename)
    count(file_path)
    count_most_frequent_word(file_path)


if __name__ == "__main__":
    main()
