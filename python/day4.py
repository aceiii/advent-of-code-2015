#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import hashlib


s = "iwrupvqb"

i = 1

part1 = None
part2 = None
prefix = s.encode('ascii')
while part1 is None or part2 is None:
    m = hashlib.md5(prefix + str(i).encode('ascii'))
    h = m.digest()

    a = int.from_bytes(h[:3])

    if a <= 15 and part1 is None:
        part1 = i
        print("Part1: ", i)
    if a == 0 and part2 is None:
        part2 = i
        print("Part2: ", i)

    i += 1
    #print(h, i)


