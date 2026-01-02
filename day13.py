#!/usr/bin/env python3

import sys
from collections import defaultdict
from operator import itemgetter
from itertools import permutations


def parse_seat(lines):
    names = set()
    prefs = defaultdict(lambda: 0)

    for line in lines:
        line = line.strip()
        name1, rest = line.split(' ', 1)
        mid, name2 = rest.rsplit(' ', 1)
        num, *rest = mid[11:].split(' ')
        name2 = name2[:-1]
        val = int(num, 10)

        if mid.startswith('would lose'):
            val = -val

        prefs[(name1, name2)] = val

        names.add(name1)
        names.add(name2)

    return names, prefs

def calc_happiness(prefs, seating):
    n = len(seating)
    if n < 2:
        return 0

    happiness = 0
    if n == 2:
        name1 = seating[0]
        name2 = seating[1]
        happiness += prefs[(name1, name2)]
        happiness += prefs[(name2, name1)]
        return happiness

    for idx, name in enumerate(seating):
        prev_name = seating[(idx - 1) % n]
        next_name = seating[(idx + 1) % n]
        happiness += prefs[(name, prev_name)]
        happiness += prefs[(name, next_name)]

    return happiness


def part1(lines):
    names, prefs = parse_seat(lines)
    answer = -float('inf')
    for seating in permutations(names):
        answer = max(answer, calc_happiness(prefs, seating))
    return answer


def part2(lines):
    names, prefs = parse_seat(lines)
    names.add('Me')
    answer = -float('inf')
    for seating in permutations(names):
        answer = max(answer, calc_happiness(prefs, seating))
    return answer


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

