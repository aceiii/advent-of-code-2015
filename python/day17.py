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


def count2(vals, target, idx, n = 0):
    if target == 0:
        return [n]

    res = []
    for j in range(idx, len(vals)):
        val = vals[j]
        if val <= target:
            ans = count2(vals, target-val, j+1, n + 1)
            res += ans
    return res


def part2(lines):
    N = 150
    vals = list(sorted((int(line.strip(),10) for line in lines), reverse=True))
    res = count2(vals, N, 0)
    return res.count(min(res))


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

