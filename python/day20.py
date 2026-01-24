#!/usr/bin/env python3

import sys


def part1(lines):
    target = int(lines[0],10)
    arr = [0] * (target//10)
    n = len(arr)
    for i in range(1, n):
        j = i
        k = i * 10
        while j < n:
            arr[j] += k
            j += i
        if arr[i] >= target:
            return i


def part2(lines):
    target = int(lines[0],10)
    arr = [0] * (target//10)
    n = len(arr)
    for i in range(1, n):
        j = i
        k = i * 11
        m = 0
        while j < n and m < 50:
            arr[j] += k
            j += i
            m += 1
        if arr[i] >= target:
            return i


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

