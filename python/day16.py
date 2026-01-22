#!/usr/bin/env python3

import sys

attribs = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

def parse(line):
    _, rest = line.strip().split(": ", 1)
    sue = {}
    for part in rest.split(", "):
        key, val = part.split(": ")
        sue[key] = int(val, 10)
    return sue


def part1(lines):
    sues = [parse(line) for line in lines]
    for idx, sue in enumerate(sues):
        if all(attribs[key] == val for key,val in sue.items()):
            return idx + 1


def match(key, val):
    check_val = attribs[key]
    if key in ['cats','trees']:
        return val > check_val
    elif key in ['pomeranians','goldfish']:
        return val < check_val
    return check_val == val


def part2(lines):
    sues = [parse(line) for line in lines]
    for idx, sue in enumerate(sues):
        if all(match(key, val) for key,val in sue.items()):
            return idx + 1



def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

