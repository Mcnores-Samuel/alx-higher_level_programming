#!/usr/bin/python3


def process_tuple(tuple_a=()):
    """Checks if a tuple has no value or only one and one value.

    args:
        tuple_a: a tuple to process or add a value(s).
    Returns: a new tuple of two values.
    """
    if not tuple_a or len(tuple_a) == 1:
        tuple_a = list(tuple_a)
        for n in range(2):
            if tuple_a and tuple_a[0] and len(tuple_a) == 1:
                tuple_a.insert(1, 0)
            else:
                if len(tuple_a) < 2:
                    tuple_a.append(0)
            n += 1
        tuple_a = tuple(tuple_a)
    else:
        if len(tuple_a) > 2:
            tuple_a = list(tuple_a)
            tuple_a = [tuple_a[n] for n in range(2)]
            tuple_a = tuple(tuple_a)
    return tuple_a


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples.

    args:
        tuple_a: first tuple to add.
        tuple_b: second tuple.
    Returns: new tuple of total values fro
    """
    new_tuple_a = process_tuple(tuple_a)
    new_tuple_b = process_tuple(tuple_b)

    result = []
    for n in range(len(new_tuple_a)):
        result.append(new_tuple_a[n] + new_tuple_b[n])

    result = tuple(result)

    return result
