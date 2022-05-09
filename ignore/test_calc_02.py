import unittest
from calc.calc import *

class CalculatorTest(TestCase):
    # testing add()
    def test_add_1(self):
        self.assertEqual(add(1,2),3)

    def test_add_2(self):
        self.assertEqual(add(2,-2), 0)

    def test_add_3(self):
        self.assertEqual(add(-2,2), 0)


    # testing subtract()
    def test_subtract_1(self):
        self.assertEqual(subtract(1,2), -1)

    def test_subtract_2(self):
        self.assertEqual(subtract(2,-2), 4)

    def test_subtract_3(self):
        self.assertEqual(subtract(-2,2), -4)

    def test_subtract_4(self):
        self.assertEqual(subtract(0,0), 0)


    # testing multiply()
    def test_multiply_1(self):
        self.assertEqual(multiply(1,2), 2)

    def test_multiply_2(self):
        self.assertEqual(multiply(2,-2), -4)

    def test_multiply_3(self):
        self.assertEqual(multiply(-2,2), -4)

    def test_multiply_4(self):
        self.assertEqual(multiply(0,0), 0)

    def test_multiply_5(self):
        self.assertEqual(multiply(0,1), 0)

    def test_multiply_6(self):
        self.assertEqual(multiply(1,0), 0)

    def test_multiply_7(self):
        self.assertEqual(multiply(1,1), 1)

    def test_multiply_8(self):
        self.assertEqual(multiply(2,2), 4)

    def test_multiply_9(self):
        self.assertEqual(multiply(2,3), 6)

    def test_multiply_10(self):
        self.assertEqual(multiply(3,2), 6)

    def test_multiply_11(self):
        self.assertEqual(multiply(3,3), 9)


    # testing divide()
    def test_divide_1(self):
        self.assertEqual(divide(1,2), 0.5)

    def test_divide_2(self):
        self.assertEqual(divide(2,-2), -1)

    def test_divide_3(self):
        self.assertEqual(divide(-2,2), -1)

    def test_divide_4(self):
        self.assertRaises(ZeroDivisionError,divide,0,0)

    def test_divide_5(self):
        self.assertEqual(divide(0,1), 0)

    def test_divide_6(self):
        self.assertEqual(divide(1,0), 0)

    def test_divide_7(self):
        self.assertEqual(divide(1,1), 1)

    def test_divide_8(self):
        self.assertEqual(divide(2,2), 1)

    def test_divide_9(self):
        self.assertEqual(divide(2,3), 0.6666666666666666)

    def test_divide_10(self):
        self.assertEqual(divide(3,2), 1.5)

    def test_divide_11(self):
        self.assertEqual(divide(3,3), 1)


    # testing abs()
    def test_abs_1(self):
        self.assertEqual(abs(-1), 1)

    def test_abs_2(self):
        self.assertEqual(abs(1), 1)

    def test_abs_3(self):
        self.assertEqual(abs(0), 0)

    def test_abs_4(self):
        self.assertEqual(abs(-0), 0)

    def test_abs_5(self):
        self.assertEqual(abs(1.1), 1.1)

    def test_abs_6(self):
        self.assertEqual(abs(-1.1), 1.1)

    def test_abs_7(self):
        self.assertEqual(abs(0.0), 0.0)

    def test_abs_8(self):
        self.assertEqual(abs(-0.0), 0.0)

    def test_abs_9(self):
        self.assertEqual(abs(1.1e10), 1.1e10)

    def test_abs_10(self):
        self.assertEqual(abs(-1.1e10), 1.1e10)


    # testing mod()
    def test_mod_1(self):
        self.assertEqual(mod(1,2), 1)

    def test_mod_2(self):
        self.assertEqual(mod(2,-2), 0)

    def test_mod_3(self):
        self.assertEqual(mod(-2,2), 0)

    def test_mod_4(self):
        self.assertEqual(mod(0,0), 0)

    def test_mod_5(self):
        self.assertEqual(mod(0,1), 0)

    def test_mod_6(self):
        self.assertEqual(mod(1,0), 0)

    def test_mod_7(self):
        self.assertEqual(mod(1,1), 0)

    def test_mod_8(self):
        self.assertEqual(mod(2,2), 0)

    def test_mod_9(self):
        self.assertEqual(mod(2,3), 1)

    def test_mod_10(self):
        self.assertEqual(mod(3,2), 1)


    # testing sqrt()
    def test_sqrt_1(self):
        self.assertEqual(sqrt(1), 1)

    def test_sqrt_2(self):
        self.assertEqual(sqrt(2), 1.4142135623730951)

    def test_sqrt_3(self):
        self.assertEqual(sqrt(3), 1.7320508075688772)

    def test_sqrt_4(self):
        self.assertEqual(sqrt(4), 2)

    def test_sqrt_5(self):
        self.assertEqual(sqrt(5), 2.23606797749979)

    def test_sqrt_6(self):
        self.assertEqual(sqrt(6), 2.449489742783178)

    def test_sqrt_7(self):
        self.assertEqual(sqrt(7), 2.6457513110645907)

    def test_sqrt_8(self):
        self.assertEqual(sqrt(8), 2.8284271247461903)

    def test_sqrt_9(self):
        self.assertEqual(sqrt(9), 3)

    def test_sqrt_10(self):
        self.assertEqual(sqrt(100), 10)


    # testing factorial()
    def test_factorial_1(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_2(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_3(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_4(self):
        self.assertEqual(factorial(3), 6)

    def test_factorial_5(self):
        self.assertEqual(factorial(4), 24)

    def test_factorial_6(self):
        self.assertEqual(factorial(5), 120)


    # testing floor()
    def test_floor_1(self):
        self.assertEqual(floor(1.1), 1)

    def test_floor_2(self):
        self.assertEqual(floor(1.9), 1)

    def test_floor_3(self):
        self.assertEqual(floor(2.1), 2)

    def test_floor_4(self):
        self.assertEqual(floor(2.9), 2)

    def test_floor_5(self):
        self.assertEqual(floor(0.1), 0)

    def test_floor_6(self):
        self.assertEqual(floor(0.9), 0)

    def test_floor_7(self):
        self.assertEqual(floor(1), 1)


    # testing ceiling()
    def test_ceiling_1(self):
        self.assertEqual(ceiling(1.1), 2)

    def test_ceiling_2(self):
        self.assertEqual(ceiling(1.9), 2)

    def test_ceiling_3(self):
        self.assertEqual(ceiling(2.1), 3)

    def test_ceiling_4(self):
        self.assertEqual(ceiling(2.9), 3)

    def test_ceiling_5(self):
        self.assertEqual(ceiling(0.1), 1)

    def test_ceiling_6(self):
        self.assertEqual(ceiling(0.9), 1)

    def test_ceiling_7(self):
        self.assertEqual(ceiling(1), 1)
