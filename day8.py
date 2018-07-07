#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


filename = "day8.input"

with open(filename, "r") as f:
    orig_lines = filter(lambda s: len(s) > 0, map(lambda s: s.strip(), f.read().split("\n")))
    lines = map(lambda s: s.strip()[1:-1].decode("string-escape"), orig_lines)
    new_lines = map(lambda s: "\"" + s.replace("\\","\\\\") + "\"", orig_lines)

    print sum([len(line) for line in orig_lines])
    print sum([len(line) for line in lines])
    print sum([len(line) for line in new_lines])


