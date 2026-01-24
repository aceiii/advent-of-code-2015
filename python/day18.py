#!/usr/bin/env python3

import sys


def parse(lines):
    state = {}
    height = len(lines)
    width = len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            pos = (x, y)
            state[pos] = c == '#'
    return state, (width, height)


def all_tiles(dims):
    width, height = dims
    for y in range(height):
        for x in range(width):
            yield (x, y)


def neighbours(dims, pos):
    width, height = dims
    x, y = pos
    tiles = [
        (-1,-1), (0,-1), (1,-1),
        (-1, 0),         (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]

    for (dx, dy) in tiles:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= width or ny < 0 or ny >= height:
            continue
        yield (nx, ny)


def count_neighbours(state, dims, pos):
    n = {npos:1 if state[npos] else 0 for npos in neighbours(dims, pos)}
    return sum(n.values())


def count_on(state, dims):
    return sum(1 if state[pos] else 0 for pos in all_tiles(dims))


def update(state, dims):
    new_state = {}
    for pos in all_tiles(dims):
        on = state[pos]
        count = count_neighbours(state, dims, pos)
        new_state[pos]= (on and (count == 2 or count == 3)) or (not on and count == 3)
    return new_state


def print_grid(state, dims, title=None):
    width, height = dims
    if title:
        print(title)
    print('╔' + ''.join(['═'] * width) + '╗')
    for y in range(height):
        row = ['#' if state[(x,y)] else '.' for x in range(width)]
        print('║' + ''.join(row) + '║')
    print('╚' + ''.join(['═'] * width) + '╝')
    print()


def part1(lines):
    N = 100
    state, dims = parse(lines)
    #print_grid(state, dims, 'Initial state')

    for i in range(N):
        state = update(state, dims)
        #print_grid(state, dims, f'After {i+1} Steps')

    return count_on(state, dims)


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

