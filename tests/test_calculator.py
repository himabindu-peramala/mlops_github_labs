import pytest
from src.calculator import add, subtract, multiply, divide, power, add_three

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(5, 0) == 5
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3
    assert power(2, -1) == 0.5

def test_add_three():
    assert add_three(1, 2, 3) == 6
    assert add_three(-1, 0, 1) == 0

def test_type_errors():
    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        add("a", 1)
    with pytest.raises(ValueError, match="All inputs must be numbers."):
        add_three(1, "b", 3)
