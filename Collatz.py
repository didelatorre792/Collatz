#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]


# ------------
# collatz_eval
# -----------

# creating cache
cache = {}


def cycle_length(n):
    """
    calculate the number of cycle length for Collatz
    """
    # making sure collatz input is non-negative
    assert n > 0

    cycle = 1
    # while loop keeps cycling until number equals desired 1
    while n > 1:
        # if n is even
        if (n % 2) == 0:
            n = (n // 2)
            cycle += 1
        else:
            # if n is odd
            n = (n + (n // 2) + 1)
            cycle += 2

    # cycle will never be under 0 or above 999999
    assert cycle > 0
    assert cycle < 999999
    return cycle


def collatz_eval(i, j):

    max_cycle = 0
    #making sure that the left integer in range is always the smallest
    if j < i:
        (i, j) = (j, i)
    if ((j // 2) + 1) > i:
        i = (j // 2) + 1

    assert j > i
    # creating cache values
    for n in range(i, j + 1):
        #getting cache value with index if already in cache
        if n in cache:
            cycle = cache[n]
        #otherwise, store value
        else:
            cycle = cycle_length(n)
            cache[n] = cycle

        if (cycle > max_cycle):
            max_cycle = cycle

    # max_cycle will never be under 0 or above 999999
    assert max_cycle > 0
    assert max_cycle < 999999
    return max_cycle


# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
