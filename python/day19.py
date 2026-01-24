#!/usr/bin/env python3

import sys
from collections import defaultdict


def parse(lines):
    mode = 1
    replacements = defaultdict(list)
    molecules = None
    for line in lines:
        line = line.strip()
        if mode == 2:
            molecules = line
            break

        if not line:
            mode += 1
            continue

        key, val = line.split(' => ')
        replacements[key].append(val)
    return molecules, replacements


def part1(lines):
    molecules, replacements = parse(lines)
    replaced = set()
    for idx, m in enumerate(molecules):
        head = molecules[:idx]
        tail = molecules[idx+1:]
        for r in replacements[m]:
            replaced.add(head + r + tail)

        m2 = molecules[idx:idx+2]
        tail = molecules[idx+2:]
        for r in replacements[m2]:
            replaced.add(head + r + tail)
    return len(replaced)


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

