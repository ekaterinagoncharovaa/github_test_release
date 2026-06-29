"""Simple arithmetic operations.

Every function works with ints and floats and raises clear errors on
invalid input (e.g. division by zero, empty sequences).
"""

from __future__ import annotations

from typing import Sequence

Number = int | float


def add(a: Number, b: Number) -> Number:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return ``a`` minus ``b``."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: if ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """Return ``base`` raised to ``exponent``."""
    return base ** exponent


def modulo(a: Number, b: Number) -> Number:
    """Return the remainder of ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: if ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b


def floor_divide(a: Number, b: Number) -> Number:
    """Return the floor of ``a`` divided by ``b``.

    Raises:
        ZeroDivisionError: if ``b`` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("floor division by zero")
    return a // b


def absolute(a: Number) -> Number:
    """Return the absolute value of ``a``."""
    return abs(a)


def negate(a: Number) -> Number:
    """Return ``a`` with its sign flipped."""
    return -a


def average(values: Sequence[Number]) -> float:
    """Return the arithmetic mean of ``values``.

    Raises:
        ValueError: if ``values`` is empty.
    """
    if not values:
        raise ValueError("cannot compute the average of an empty sequence")
    return sum(values) / len(values)
