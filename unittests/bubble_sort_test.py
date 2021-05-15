import random
import unittest
from src import bubble_sort as bs


class TestValue(unittest.TestCase):
    def test_simple(self):
        test_list = [4, 3, 2, 1]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = bs.bubble_sort(test_list)
        self.assertEqual(actual_list, expected_list)

    def test_empty(self):
        test_list = []
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = bs.bubble_sort(test_list)
        self.assertEqual(actual_list, expected_list)

    def test_presorted(self):
        test_list = [1, 2, 3, 4]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = bs.bubble_sort(test_list)
        self.assertEqual(actual_list, expected_list)

    def test_negative(self):
        test_list = [-4, -3, -2, -1]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = bs.bubble_sort(test_list)
        self.assertEqual(actual_list, expected_list)

    def test_random(self):
        test_list = [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
        expected_list = test_list.copy()
        expected_list.sort()
        actual_list = bs.bubble_sort(test_list)
        self.assertEqual(actual_list, expected_list)
