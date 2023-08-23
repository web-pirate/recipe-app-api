"""
Sample Tst case
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calculator class."""
    def test_add_numbers(self):
        res = calc.add(5,6)
        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        res = calc.substract(-2,-30)
        self.assertEqual(res , 28 )