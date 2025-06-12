## Operation Tests
## Evan Garvey
## IS 601, Module 3

import pytest # type: ignore
from app.operations import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(1, 2) == -1

def test_multiply():
    assert multiply(2, 4) == 8

def test_divide():
    assert divide(4, 2) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)