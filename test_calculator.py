"""
Unit tests for the calculator library
"""

import app


class TestCalculator:

    def test_addition(self):
        assert 4 == app.add(2, 2)

    def test_subtraction(self):
        assert 2 == app.subtract(4, 2)
