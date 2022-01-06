import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 3) == 9

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 15, 5) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 19, 5) == 14

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 14, 35) == 49