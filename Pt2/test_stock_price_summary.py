import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_prices_all_types(self):
        """Test stock prices with positive, negative and zero values."""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

    def test_stock_prices_all_positive(self):
        """Test stock prices with all positive values."""

        actual = a1.stock_price_summary([0.01, 0.02, 0.03, 0.04, 0.05])
        expected = (0.15, 0.0)
        self.assertEqual(expected, actual)

    def test_stock_prices_all_negative(self):
        """Test stock prices with all negative values."""

        actual = a1.stock_price_summary([-0.01, -0.02, -0.03, -0.04, -0.05])
        expected = (0.0, -0.15)
        self.assertEqual(expected, actual)

    def test_stock_prices_all_zero(self):
        """Test stock prices with all zero values."""

        actual = a1.stock_price_summary([0, 0, 0, 0, 0])
        expected = (0.0, 0.0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
