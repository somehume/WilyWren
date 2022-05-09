from calc.calc import *
import pytest


# testing ceiling()
def test_ceiling_1():
    assert ceiling(1.1) == 2

def test_ceiling_2():
    assert ceiling(1.9) == 2

def test_ceiling_3():
    assert ceiling(2.1) == 3

def test_ceiling_4():
    assert ceiling(2.9) == 3

def test_ceiling_5():
    assert ceiling(0.1) == 1

def test_ceiling_6():
    assert ceiling(0.9) == 1

def test_ceiling_7():
    assert ceiling(1) == 1
