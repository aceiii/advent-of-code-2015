#!/usr/bin/env python3

import sys
from json import loads


def is_number(val):
    t = type(val)
    return t == float or t == int

def is_obj(val):
    return type(val) == dict


def is_array(val):
    return type(val) == list


def count_numbers(obj):
    if is_number(obj):
        return obj

    if is_obj(obj):
        return sum(count_numbers(val) for val in obj.values())

    if is_array(obj):
        return sum(count_numbers(val) for val in obj)

    return 0


def part1(lines):
    obj = loads(lines[0])
    return count_numbers(obj)


def count_numbers_without_red(obj):
    if is_number(obj):
        return obj

    if is_array(obj):
        return sum(count_numbers_without_red(val) for val in obj)

    if is_obj(obj):
        count = 0
        for key, val in obj.items():
            if val == 'red':
                return 0
            count += count_numbers_without_red(val)
        return count

    return 0


def part2(lines):
    obj = loads(lines[0])
    return count_numbers_without_red(obj)


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

