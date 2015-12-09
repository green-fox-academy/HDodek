import unittest
import func1

class TestFunc(unittest.TestCase):
    def test_apply_function(self):
        array = [1, 2, 3,]
        self.assertEqual(func1.adder(array), [2, 3, 4])

    def test_filter_array(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(func1.filterArray(array), [0,3,6,9])

unittest.main()
