#!/usr/bin/env python
# -*- coding: utf-8 -*-


s = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""


ids = {}


class BinaryOp(object):
    def __init__(self, op, left, right):
        self._op = op
        self._left = left
        self._right = right
    def val(self):
        return self._op(self._left(), self._right())

class UnaryOp(object):
    def __init__(self, op, val):
        self._op = op
        self._val = val
    def val(self):
        return self._op(self._val())



def tokenize(item):
    try:
        n = int(item, 10)
        return Signal(n)
    except:
        if item == '->':
            return 


for line in s.split("\n"):
    tokens = map(tokenize, line.split(" "))


