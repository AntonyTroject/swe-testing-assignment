import pytest

from quick_calc.calculator import (
    DivisionByZeroError,
    add,
    sub,
    mul,
    div,
    CalculatorState,
)


def test_addition_basic():
    assert add(5, 3) == 8


def test_subtraction_basic():
    assert sub(10, 4) == 6


def test_multiplication_basic():
    assert mul(6, 7) == 42


def test_division_basic():
    assert div(8, 2) == 4


def test_division_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        div(1, 0)


def test_negative_numbers():
    assert add(-5, -3) == -8
    assert sub(-10, 4) == -14


def test_decimal_numbers():
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert div(1.5, 0.5) == 3


def test_very_large_numbers():
    big = 10**18
    assert mul(big, 2) == 2 * big


def test_clear_resets_state():
    s = CalculatorState()
    s.current_input = "123"
    s.stored_value = 999
    s.pending_op = "+"
    s.result = 777
    s.clear()
    assert s.current_input == ""
    assert s.stored_value == 0.0
    assert s.pending_op is None
    assert s.result == 0.0