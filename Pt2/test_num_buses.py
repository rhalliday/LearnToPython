import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_75(self):
        """Test num_buses with 75."""

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_least_amount(self):
        """Test num_buses with least amount of people."""

        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_1_less_max(self):
        """Test num_buses with 1 below the max number of people for a bus."""

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_max(self):
        """Test num_buses with max amount of people."""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_max_plus_1(self):
        """Test num_buses with max plus 1 amount of people."""

        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected, actual)

    def test_num_buses_more_than_2(self):
        """Test num_buses with more than 2 buses."""

        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
