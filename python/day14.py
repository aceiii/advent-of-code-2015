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


class Deer:
    def __init__(self, speed, time, rest):
        self.speed = speed
        self.time = time
        self.rest = rest
        self.state = 0
        self.counter = time
        self.distance = 0
        self.points = 0

    def update(self):
        self.counter -= 1
        if self.state == 0:
            self.distance += self.speed

        if self.counter == 0:
            if self.state == 0:
                self.counter = self.rest
                self.state = 1
            else:
                self.counter = self.time
                self.state = 0

    def add_point(self):
        self.points += 1


def update_deers(deers):
    for deer in deers:
        deer.update()
    return sorted(deers, key=lambda d: d.distance, reverse=True)


def part2(lines):
    target = 2503
    deers = [Deer(*deer) for deer in parse_reindeer(lines).values()]
    while target:
        target -= 1
        deers = update_deers(deers)
        prev = deers[0].distance
        for deer in deers:
            if deer.distance < prev:
                break
            deer.add_point()

    deers = sorted(deers, key=lambda d: d.points, reverse=True)
    return deers[0].points


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

