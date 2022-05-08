from calc.calc import *

# testing add()
def test_add_1():
    assert add(1,2) == 3

def test_add_2():
    assert add(2,-2) == 0

def test_add_3():
    assert add(-2,2) == 0


# testing subtract()
def test_subtract_1():
    assert subtract(1,2) == -1

def test_subtract_2():
    assert subtract(2,-2) == 4

def test_subtract_3():
    assert subtract(-2,2) == -4

def test_subtract_4():
    assert subtract(0,0) == 0


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


# testing divide()
def test_divide_1():
    assert divide(1,2) == 0.5

def test_divide_2():
    assert divide(2,-2) == -0.5

def test_divide_3():
    assert divide(-2,2) == -0.5

def test_divide_4():
    assert divide(0,0) == 0

def test_divide_5():
    assert divide(0,1) == 0

def test_divide_6():
    assert divide(1,0) == 0

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


# testing mod()
def test_mod_1():
    assert mod(1,2) == 1

def test_mod_2():
    assert mod(2,-2) == 0

def test_mod_3():
    assert mod(-2,2) == 0

def test_mod_4():
    assert mod(0,0) == 0

def test_mod_5():
    assert mod(0,1) == 0

def test_mod_6():
    assert mod(1,0) == 0

def test_mod_7():
    assert mod(1,1) == 0

def test_mod_8():
    assert mod(2,2) == 0

def test_mod_9():
    assert mod(2,3) == 1

def test_mod_10():
    assert mod(3,2) == 1