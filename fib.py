from typing import Dict
from typing import Generator
from functools import lru_cache


def fib2(n: int):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


memo: Dict[int, int] = {0: 1, 1: 1}
def fib3(n: int):
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)

    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


def fib5(n: int):
    if n == 0:
        return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next

    return next


def fib6(n):

    yield 0
    yield 1

    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next
