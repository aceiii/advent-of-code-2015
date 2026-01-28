#!/usr/bin/env python3

import sys


def parse(lines):
    instrs = []
    for line in lines:
        instr, rest = line.strip().split(' ', 1)
        if instr == 'jmp':
            instrs.append((instr, None, int(rest, 10)))
        elif instr == 'jie' or instr == 'jio':
            reg, offset = rest.split(',')
            instrs.append((instr, reg, int(offset, 10)))
        else:
            instrs.append((instr, rest, None))
    return instrs


def step(regs, instr):
    op, r, off = instr
    if op == 'hlf':
        regs[r] //= 2
    elif op == 'tpl':
        regs[r] *= 3
    elif op == 'inc':
        regs[r] += 1
    elif op == 'jmp':
        return off
    elif op == 'jie':
        if regs[r] % 2 == 0:
            return off
    elif op == 'jio':
        if regs[r] == 1:
            return off
    return 1


def run(instrs):
    regs = {'a': 0, 'b': 0}
    ip = 0
    while ip >= 0 and ip < len(instrs):
        ip += step(regs, instrs[ip])
    return regs


def part1(lines):
    instrs = parse(lines)
    regs = run(instrs)
    return regs['b']


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

