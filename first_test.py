import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 4) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 30, 10) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 15, 5) == 10

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 100, 400) == 500
