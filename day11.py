#!/usr/bin/env python3

import sys
from more_itertools import windowed


INVALID_LETTERS = set(ord(c) for c in 'iol')


def has_straight(password):
    for a, b, c in windowed(reversed(password), 3):
        if b == a + 1 and c == a + 2:
            return True
    return False


def has_invalid_letters(password):
    for c in password:
        if c in INVALID_LETTERS:
            return True
    return False


def has_overlapping_pairs(password):
    first_pair = None
    first_pair_idx = -1

    for i, (a, b) in enumerate(windowed(reversed(password), 2)):
        if a != b:
            continue

        if first_pair is None:
            first_pair = a
            first_pair_idx = i
            continue

        if a != first_pair and i > first_pair_idx + 1:
            return True

    return False


def is_valid(password):
    return has_straight(password) \
        and not has_invalid_letters(password) \
        and has_overlapping_pairs(password)


def parse_password(line):
    password = [ord(c) - ord('a') for c in line]
    password.reverse()
    return password


def next_password(password):
    idx = 0
    while True:
        if idx > len(password) - 1:
            password.append(1)
            break

        password[idx] += 1
        carry = password[idx] > 25
        if not carry:
            break

        password[idx] = 0
        idx += 1

    return password


def password_to_str(password):
    res = [chr(c + ord('a')) for c in password]
    res.reverse()
    return "".join(res)


def part1(lines):
    password = parse_password(lines[0].strip())
    while True:
        password = next_password(password)
        if is_valid(password):
            break
    return password_to_str(password)


def part2(lines):
    password = parse_password(lines[0].strip())
    count = 0
    while True:
        password = next_password(password)
        if is_valid(password):
            count += 1
            if count == 2:
                break
    return password_to_str(password)


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

