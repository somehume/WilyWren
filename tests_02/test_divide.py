from calc.calc import *
import pytest


# testing divide()
def test_divide_1():
    assert divide(1,2) == 0.5

def test_divide_2():
    assert divide(2,-2) == -1

def test_divide_3():
    assert divide(-2,2) == -1

def test_divide_4():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)
    #assert divide(0,0) == 0

def test_divide_5():
    assert divide(0,1) == 0

def test_divide_6():
        with pytest.raises(ZeroDivisionError):
            divide(1,0)
    #assert divide(1,0) == 0

def test_divide_7():
    assert divide(1,1) == 1

def test_divide_8():
    assert divide(2,2) == 1

def test_divide_9():
    assert divide(2,3) == 0.6666666666666666

def test_divide_10():
    assert divide(3,2) == 1.5

def test_divide_11():
    assert divide(3,3) == 1

