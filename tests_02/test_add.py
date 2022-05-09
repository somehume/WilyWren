from calc.calc import *
import pytest

# testing add()
def test_add_1():
    assert add(1,2) == 3

def test_add_2():
    assert add(2,-2) == 0

def test_add_3():
    assert add(-2,2) == 0

