#!/usr/bin/env python3

import sys


def look_and_say(line):
    if not line:
        return []

    res = []
    count = 1
    prev = line[0]
    for i in range(1, len(line)):
        n = line[i]
        if n != prev:
            res.append(count)
            res.append(prev)
            count = 1
        else:
            count += 1
        prev = n
    res.append(count)
    res.append(prev)
    return res


def part1(lines):
    res = [int(c,10) for c in lines[0]]
    print(res)
    for _ in range(40):
        res = look_and_say(res)
        #print("".join(map(str,res)))
    return len(res)


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

