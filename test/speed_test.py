"""
Speed test: compare selected methods by execution time.
"""
import time
from typing import Callable, Tuple, List

from fizzbuzz import FizzBuzz


def speed_test(method: Callable[[int], str]) -> str:
    start = time.perf_counter()
    for n in range(0, 101):
        method(n)
    return f'{method.__name__:>25s} - {(time.perf_counter() - start) * 1000:6.4f} ms'


def extra_method(n: int, modules: Tuple[Tuple[int, str]] = ((3, 'Fizz'), (5, 'Buzz'))) -> str:
    res = ''
    for mod, s in modules:
        if n % mod == 0:
            res += s
    return res if res else str(n)


if __name__ == '__main__':

    fb = FizzBuzz()

    methods: List[Callable[[int], str]] = [fb.by_cheating, fb.by_expression, fb.by_boolean_multiplication,
                                           fb.by_accumulator, fb.by_decode, fb.by_tables, fb.by_mapping,
                                           fb.by_lambda_decode, fb.by_framework, fb.by_functions,
                                           extra_method]

    for m in methods:
        print(speed_test(m))
