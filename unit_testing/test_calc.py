import unittest
import calc

class TestCalc(unittest.TestCase):

  def test_add(self):
    result = calc.add(1, 2)
    self.assertEqual(result, 3)

  def test_subtract(self):
    result = calc.subtract(5, 3)
    self.assertEqual(result, 2)

  def test_multiply(self):
    result = calc.multiply(4, 3)
    self.assertEqual(result, 12)

  def test_divide(self):
    self.assertEqual(calc.divide(12, 2), 6)
    
    with self.assertRaises(ValueError) as cm:
      calc.divide(12, 0)

