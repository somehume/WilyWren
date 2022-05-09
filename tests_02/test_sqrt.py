from calc.calc import *
import pytest

# testing sqrt()
def test_sqrt_1():
    assert sqrt(1) == 1

def test_sqrt_2():
    assert sqrt(2) == 1.414213562373095

def test_sqrt_3():
    assert sqrt(3) == 1.7320508075688772

def test_sqrt_4():
    assert sqrt(4) == 2

def test_sqrt_5():
    assert sqrt(5) == 2.23606797749979

def test_sqrt_6():
    assert sqrt(6) == 2.449489742783178

def test_sqrt_7():
    assert sqrt(7) == 2.6457513110645907

def test_sqrt_8():
    assert sqrt(8) == 2.82842712474619

def test_sqrt_9():
    assert sqrt(9) == 3

def test_sqrt_10():
    assert sqrt(100) == 10

