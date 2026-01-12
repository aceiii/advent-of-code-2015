#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ctypes
import string


s = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""



def and_func(a, b):
    return ctypes.c_uint16(a & b).value


def or_func(a, b):
    return ctypes.c_uint16(a | b).value


def lshift_func(a, b):
    return ctypes.c_uint16(a << b).value


def rshift_func(a, b):
    return ctypes.c_uint16(a >> b).value


def not_func(a):
    return ctypes.c_uint16(~a).value


def is_var(a):
    return all(c in string.ascii_lowercase for c in a)


def is_op(a):
    return all(c in string.ascii_uppercase for c in a)


ops = {
    "AND": and_func,
    "OR": or_func,
    "LSHIFT": lshift_func,
    "RSHIFT": rshift_func,
    "NOT": not_func,
}


def parse_arg(arg):
    if is_var(arg):
        return ("var", arg)
    elif is_op(arg):
        return ("op", ops[arg])
    else:
        return ("int", int(arg, 10))


def eval_int_or_var(arg, vars):
    type_, val = arg

    if type_ == "int":
        return val

    if val in vars["__cache__"]:
        return vars["__cache__"][val]

    res = vars[val]()
    vars["__cache__"][val] = res

    return res


def make_func(ops, vars):
    args = [parse_arg(arg) for arg in ops.strip().split(" ")]

    def func():
        if len(args) == 1:
            arg, = args
            return eval_int_or_var(arg, vars)

        elif len(args) == 2:
            (_, op_func), arg = args
            return op_func(eval_int_or_var(arg, vars))

        elif len(args) == 3:
            a, (_, op_func), b = args
            a_val = eval_int_or_var(a, vars)
            b_val = eval_int_or_var(b, vars)
            return op_func(a_val, b_val)

        else:
            raise NotImplementedError(f"Invalid args: {args}")
    return func


def parse(lines):
    vars = { "__cache__": {} }

    for line in lines:
        ops, target = line.strip().split(" -> ")
        vars[target] = make_func(ops, vars)

    return vars


print(parse(s.strip().split("\n"))["i"]())

with open("day7.input") as f:
    lines = f.read().strip().split("\n")
    vars =  parse(lines)
    part1 = vars["a"]()
    print("part1: ", part1)

    vars["__cache__"] = { "b": part1 }
    part2 = vars["a"]()
    print("part2: ", part2)

