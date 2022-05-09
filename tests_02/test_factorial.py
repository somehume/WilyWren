from calc.calc import *
import pytest


# testing factorial()
def test_factorial_1():
    assert factorial(0) == 0

def test_factorial_2():
    assert factorial(1) == 1

def test_factorial_3():
    assert factorial(2) == 2

def test_factorial_4():
    assert factorial(3) == 6

def test_factorial_5():
    assert factorial(4) == 24

def test_factorial_6():
    assert factorial(5) == 120

def test_factorial_7():
    with pytest.raises(Exception):
        factorial(-1)

