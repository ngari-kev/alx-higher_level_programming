#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tup_1 = tuple(tuple_a[i] if i < len_a else 0 for i in range(0, 2))
    tup_2 = tuple(tuple_b[i] if i < len_b else 0 for i in range(0, 2))
    result = tuple(tup_1[i] + tup_2[i] for i in range(max_len))
    return result
