#!/usr/bin/env python3

import sys
from operator import itemgetter
from itertools import permutations


def parse_routes(lines):
    routes = []
    for line in lines:
        first, second = line.strip().split(" = ")
        dist = int(second, 10)
        start, end = first.strip().split(" to ")
        routes.append((start, end, dist))
    return routes


def shortest_route(route_map):
    places = set()
    for start, end in route_map:
        places.add(start)
        places.add(end)

    (start, end), dist = list(sorted(route_map.items(), key=itemgetter(1))[0])
    total_dist = dist
    places.remove(start)
    places.remove(end)
    route = [start, end]

    while places:
        fronts = []
        backs = []

        for place in places:
            front = (place, start)
            back = (end, place)

            front_dist = route_map[front]
            back_dist = route_map[back]

            fronts.append((front_dist, place))
            backs.append((back_dist, place))

        fronts.sort(key=itemgetter(0))
        backs.sort(key=itemgetter(0))

        front_dist, front = fronts[0]
        back_dist, back = backs[0]

        if front_dist < back_dist:
            route.insert(0, front)
            places.remove(front)
            total_dist += front_dist
            start = front
        else:
            route.append(back)
            places.remove(back)
            total_dist += back_dist
            end = back

    return route, total_dist


def longest_route(route_map):
    places = set()
    for start, end in route_map:
        places.add(start)
        places.add(end)


    found = None
    max_dist = 0
    for route in permutations(places):
        dist = 0
        for i in range(len(route) - 1):
            start, end = route[i:i+2]
            dist += route_map[(start, end)]

        if dist > max_dist:
            max_dist = dist
            found = route
            
            print(max_dist, found)

    return found, max_dist


def route_dist(route, route_map):
    dist = 0
    for i in range(len(route) - 1):
        start, end = route[i:i+2]
        dist += route_map[(start, end)]
    return dist


def part1(lines):
    routes = parse_routes(lines)

    route_map = {}
    for start, end, dist in routes:
        route_map[(start, end)] = dist
        route_map[(end, start)] = dist


    route, dist = shortest_route(route_map)
    return dist


def part2(lines):
    routes = parse_routes(lines)

    route_map = {}
    for start, end, dist in routes:
        route_map[(start, end)] = dist
        route_map[(end, start)] = dist


    route, dist = longest_route(route_map)
    print(route)
    return dist


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

