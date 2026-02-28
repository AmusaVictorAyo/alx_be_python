import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """
        Create a new calculator instance before each test.
        Ensures test isolation and avoids shared state.
        """
        self.calc = SimpleCalculator()

    # --------------------
    # Addition Tests
    # --------------------

    def test_add_positive_numbers(self):
        """Test addition with positive integers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Test addition with negative values."""
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_add_mixed_sign_numbers(self):
        """Test addition with mixed positive and negative values."""
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_add_floats(self):
        """Test addition with floating-point numbers."""
        self.assertEqual(self.calc.add(2.5, 0.5), 3.0)

    # --------------------
    # Subtraction Tests
    # --------------------

    def test_subtract_positive_numbers(self):
        """Test subtraction with positive integers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_result_negative(self):
        """Ensure subtraction can return negative results."""
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_subtract_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    # --------------------
    # Multiplication Tests
    # --------------------

    def test_multiply_positive_numbers(self):
        """Test multiplication with positive integers."""
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        """Ensure multiplication by zero returns zero."""
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative values."""
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

    def test_multiply_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)

    # --------------------
    # Division Tests
    # --------------------

    def test_divide_positive_numbers(self):
        """Test normal division with positive integers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_negative_numbers(self):
        """Test division with negative values."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_floats(self):
        """Test division with floating-point numbers."""
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        """
        Division by zero should return None
        as defined in the implementation contract.
        """
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()