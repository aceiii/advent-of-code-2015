#!/usr/bin/env python3

import sys
from math import prod


def count(vals, target, idx, arr=[]):
    if target == 0:
        return 1

    n = 0
    for j in range(idx, len(vals)):
        val = vals[j]
        if val <= target:
            n += count(vals, target-val, j+1, arr + [val])
    return n


def part1(lines):
    N = 150
    vals = list(sorted((int(line.strip(),10) for line in lines), reverse=True))
    return count(vals, N, 0)


def part2(lines):
    vals = list(sorted((int(line.strip(),10) for line in lines), reverse=True))
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

