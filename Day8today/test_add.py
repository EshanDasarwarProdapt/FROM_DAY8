import unittest
from Demo import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    # ---------- ADD TEST CASES ----------

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(5, -3), 2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(0, 0), 0)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)

    def test_add_floats(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_add_invalid_type(self):
        with self.assertRaises(TypeError):
            add("2", 3)

    def test_add_none(self):
        with self.assertRaises(TypeError):
            add(None, 3)


    # ---------- SUBTRACT TEST CASES ----------

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(-5, 3), -8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 0), 0)

    def test_subtract_large_numbers(self):
        self.assertEqual(subtract(2000000, 1000000), 1000000)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)

    def test_subtract_invalid_type(self):
        with self.assertRaises(TypeError):
            subtract("5", 2)

    def test_subtract_none(self):
        with self.assertRaises(TypeError):
            subtract(None, 2)


    # ---------- MULTIPLY TEST CASES ----------

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1000000, 2000), 2000000000)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 3.2), 8.0)

    def test_multiply_invalid_type(self):
        with self.assertRaises(TypeError):
            multiply("2", 3)

    def test_multiply_none(self):
        with self.assertRaises(TypeError):
            multiply(None, 3)


    # ---------- DIVIDE TEST CASES ----------

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(-10, -2), 5)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_large_numbers(self):
        self.assertEqual(divide(1000000, 1000), 1000)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_invalid_type(self):
        with self.assertRaises(TypeError):
            divide("10", 2)

    def test_divide_none(self):
        with self.assertRaises(TypeError):
            divide(None, 2)


if __name__ == "__main__":
    unittest.main()
