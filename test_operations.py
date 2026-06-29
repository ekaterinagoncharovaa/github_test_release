"""Tests for mathops.operations — one test (class) per public method."""

import pytest

from mathops import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    floor_divide,
    absolute,
    negate,
    average,
)


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_with_zero(self):
        assert add(7, 0) == 7

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    def test_positive_result(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_with_zero(self):
        assert subtract(4, 0) == 4

    def test_floats(self):
        assert subtract(5.5, 2.2) == pytest.approx(3.3)


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(4, 5) == 20

    def test_by_zero(self):
        assert multiply(99, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-3, 6) == -18

    def test_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5

    def test_fractional_result(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_negative(self):
        assert divide(-9, 3) == -3

    def test_division_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            divide(1, 0)


class TestPower:
    def test_square(self):
        assert power(3, 2) == 9

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)

    def test_fractional_exponent(self):
        assert power(9, 0.5) == pytest.approx(3.0)


class TestModulo:
    def test_basic(self):
        assert modulo(10, 3) == 1

    def test_no_remainder(self):
        assert modulo(10, 5) == 0

    def test_modulo_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            modulo(5, 0)


class TestFloorDivide:
    def test_basic(self):
        assert floor_divide(7, 2) == 3

    def test_exact(self):
        assert floor_divide(8, 4) == 2

    def test_floor_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError):
            floor_divide(5, 0)


class TestAbsolute:
    def test_negative(self):
        assert absolute(-7) == 7

    def test_positive(self):
        assert absolute(7) == 7

    def test_zero(self):
        assert absolute(0) == 0


class TestNegate:
    def test_positive(self):
        assert negate(5) == -5

    def test_negative(self):
        assert negate(-5) == 5

    def test_zero(self):
        assert negate(0) == 0


class TestAverage:
    def test_basic(self):
        assert average([2, 4, 6]) == pytest.approx(4.0)

    def test_single_value(self):
        assert average([42]) == 42

    def test_floats(self):
        assert average([1.5, 2.5]) == pytest.approx(2.0)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            average([])
