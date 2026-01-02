#!/usr/bin/env python3

import sys


def clamp(n, min_, max_):
    if n < min_:
        return min_
    elif n > max_:
        return max_
    return n


def parse_reindeer(lines):
    deer = {}
    for line in lines:
        parts = line.strip().split()
        name = parts[0],
        speed = parts[3]
        time = parts[6]
        rest = parts[-2]
        deer[name] = (int(speed,10), int(time,10), int(rest,10))
    return deer


def travel_for(deer, target):
    speed, time, rest = deer
    n = target / (rest + time)
    seconds = int(n) * time
    seconds += clamp((n - int(n)) * (rest + time), 0, time)
    return speed * seconds


def part1(lines):
    target = 2503
    deers = parse_reindeer(lines)
    distances = sorted([travel_for(deer, target) for deer in deers.values()], reverse=True)
    return distances[0]


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

