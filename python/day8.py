#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


filename = "./input/day08"

def decode_str(line):
    new_line = []
    i = 1
    n = len(line) - 1
    while i < n:
        c = line[i]
        if c == '\\':
            d = line[i+1]
            if d == 'x':
                e = chr(int(line[i+2:i+4], 16))
                new_line.append(e)
                i += 4
            else:
                new_line.append(d)
                i += 2
        else:
            new_line.append(c)
            i += 1

    return ''.join(new_line)


def encode_str(line):
    new_line = []
    for c in line:
        if c == '"':
            new_line.append('\\"')
        elif c == '\\':
            new_line.append('\\\\')
        else:
            new_line.append(c)
    return '"' + ''.join(new_line) + '"'

with open(filename, "r") as f:
    lines = [s.strip() for s in f.readlines() if s.strip()]
    part1 = 0
    part2 = 0
    for line in lines:
        decoded_line = decode_str(line)
        encoded_line = encode_str(line)
        part1 += len(line) - len(decoded_line)
        part2 += len(encoded_line) - len(line)

    print("Part1: ", part1)
    print("Part2: ", part2)


