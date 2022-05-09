from calc.calc import *
import pytest


# testing subtract()
def test_subtract_1():
    assert subtract(1,2) == -1

def test_subtract_2():
    assert subtract(2,-2) == 4

def test_subtract_3():
    assert subtract(-2,2) == -4

def test_subtract_4():
    assert subtract(0,0) == 0

