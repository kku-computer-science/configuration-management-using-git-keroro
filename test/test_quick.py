import unittest
from Project.main import quick_sort

class TestQuickSort(unittest.TestCase):

    def test_basic_sort(self):
        self.assertEqual(quick_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])

    def test_already_sorted(self):
        self.assertEqual(quick_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_order(self):
        self.assertEqual(quick_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(quick_sort([3, 1, 2, 3]), [1, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(quick_sort([10]), [10])

    def test_empty(self):
        self.assertEqual(quick_sort([]), [])

if __name__ == "__main__":
    unittest.main()
