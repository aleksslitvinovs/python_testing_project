import pytest

from src.calculator import Calculator


@pytest.fixture
def calculator() -> Calculator:
    return Calculator()


def test_add(calculator: Calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(2, 1) == 3


def test_subtract(calculator: Calculator):
    assert calculator.subtract(2, 1) == 1


def test_multiply(calculator: Calculator):
    assert calculator.multiply(2, 3) == 6


@pytest.mark.divide
def test_divide(calculator: Calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(6, 2) == 3


@pytest.mark.divide
def test_divide_by_zero(calculator: Calculator):
    with pytest.raises(ValueError) as err:
        calculator.divide(6, 0)

    assert str(err.value) == "Cannot divide by zero"


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 2),
        (3, -1, 3),
        (2, 2, 2),
    ],
)
def test_maximum(calculator: Calculator, a: float, b: float, expected: float):
    assert calculator.maximum(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (-3, 0, -3),
        (0, 100, 0),
        (1, 1, 1),
    ],
)
def test_minimum(calculator: Calculator, a: float, b: float, expected: float):
    assert calculator.minimum(a, b) == expected
