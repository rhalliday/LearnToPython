import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_long_list(self):
        """Test swap_k with long list of even values."""

        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected, nums)

    def test_swap_k_short_list(self):
        """Test swap_k with short list."""
        
        nums = [1,2,3]
        a1.swap_k(nums,1)
        expected = [3, 2, 1]
        self.assertEqual(expected, nums)

    def test_swap_k_zero_k(self):
        """Test swap_k where k is 0."""

        nums = [1, 2, 3]
        a1.swap_k(nums,0)
        expected = [1, 2, 3]
        self.assertEqual(expected, nums)

    def test_swap_k_long_odd(self):
        """Test swap k with a long odd length list."""

        nums = [1,2,3,4,5,6,7]
        a1.swap_k(nums,3)
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(expected, nums)

    def test_swap_k_even_list_all(self):
        """Test swap_k with an even list where all values
        are swapped."""

        nums = [1, 2, 3, 4]
        a1.swap_k(nums, 2)
        expected = [3, 4, 1, 2]
        self.assertEqual(expected, nums)

        
if __name__ == '__main__':
    unittest.main(exit=False)
