from calc.calc import *
import pytest


# testing mod()
def test_mod_1():
    assert mod(1,2) == 1

def test_mod_2():
    assert mod(2,-2) == 0

def test_mod_3():
    assert mod(-2,2) == 0

def test_mod_4():
    with pytest.raises(ZeroDivisionError):
        mod(0,0)
    #assert mod(0,0) == 0

def test_mod_5():
    assert mod(0,1) == 0

def test_mod_6():
    with pytest.raises(ZeroDivisionError):
        mod(1,0)
    #assert mod(1,0) == 0

def test_mod_7():
    assert mod(1,1) == 0

def test_mod_8():
    assert mod(2,2) == 0

def test_mod_9():
    assert mod(2,3) == 2

def test_mod_10():
    assert mod(3,2) == 1

