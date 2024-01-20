import pytest

from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.Calculator = Calculator
    def test_successfull_addition(self):
        assert self.Calculator.adding(self, 9, 3) == 12
    def test_successfull_subtraction(self):
        assert self.Calculator.subtraction(self, 15, 1) == 14
    def test_successfull_multiplication(self):
        assert self.Calculator.multiply(self, 15, 5) == 75
    def test_successfull_division(self):
        assert self.Calculator.division(self, 50, 10) == 5

    def teardown(self):
        print('Выполнение метода Teardown')