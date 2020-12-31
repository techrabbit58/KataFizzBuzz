"""
Speed test: compare selected methods by execution time.
"""
import time
from typing import Callable

from fizzbuzz import FizzBuzz


def speed_test(method: Callable[[int], str]) -> str:
    start = time.perf_counter()
    for n in range(0, 101):
        method(n)
    return f'{method.__name__:>25s} - {(time.perf_counter() - start) * 1000:6.4f} ms'


if __name__ == '__main__':

    fb = FizzBuzz()

    methods = [fb.by_cheating, fb.by_expression, fb.by_boolean_multiplication,
               fb.by_accumulator, fb.by_decode, fb.by_tables, fb.by_mapping,
               fb.by_lambda_decode, fb.by_framework, fb.by_functions]

    for m in methods:
        print(speed_test(m))
