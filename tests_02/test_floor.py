from calc.calc import *
import pytest


# testing floor()
def test_floor_1():
    assert floor(1.1) == 1

def test_floor_2():
    assert floor(1.9) == 1

def test_floor_3():
    assert floor(2.1) == 2

def test_floor_4():
    assert floor(2.9) == 2

def test_floor_5():
    assert floor(0.1) == 0

def test_floor_6():
    assert floor(0.9) == 0

def test_floor_7():
    assert floor(1) == 1
