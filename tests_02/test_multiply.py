from calc.calc import *
import pytest


# testing multiply()
def test_multiply_1():
    assert multiply(1,2) == 2

def test_multiply_2():
    assert multiply(2,-2) == -4

def test_multiply_3():
    assert multiply(-2,2) == -4

def test_multiply_4():
    assert multiply(0,0) == 0

def test_multiply_5():
    assert multiply(0,1) == 0

def test_multiply_6():
    assert multiply(1,0) == 0

def test_multiply_7():
    assert multiply(1,1) == 1

def test_multiply_8():
    assert multiply(2,2) == 4

def test_multiply_9():
    assert multiply(2,3) == 6

def test_multiply_10():
    assert multiply(3,2) == 6

def test_multiply_11():
    assert multiply(3,3) == 9

