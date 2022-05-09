from calc.calc import *
import pytest


# testing abs()
def test_abs_1():
    assert abs(-1) == 1

def test_abs_2():
    assert abs(1) == 1

def test_abs_3():
    assert abs(0) == 0

def test_abs_4():
    assert abs(-0) == 0

def test_abs_5():
    assert abs(1.1) == 1.1

def test_abs_6():
    assert abs(-1.1) == 1.1

def test_abs_7():
    assert abs(0.0) == 0.0

def test_abs_8():
    assert abs(-0.0) == 0.0

def test_abs_9():
    assert abs(1.1e10) == 1.1e10

def test_abs_10():
    assert abs(-1.1e10) == 1.1e10

