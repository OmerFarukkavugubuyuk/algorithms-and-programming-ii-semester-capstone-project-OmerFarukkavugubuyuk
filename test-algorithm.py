import unittest
from algorithm import merge_sort, heap_sort

class TestSortingAlgorithms(unittest.TestCase):
    def test_merge_sort(self):
        test_array = [5, 3, 8, 4, 2]
        sorted_arr, _ = merge_sort(test_array.copy())
        self.assertEqual(sorted_arr, [2, 3, 4, 5, 8])

    def test_heap_sort(self):
        test_array = [10, 7, 8, 9, 1, 5]
        sorted_arr, _ = heap_sort(test_array.copy())
        self.assertEqual(sorted_arr, [1, 5, 7, 8, 9, 10])

if __name__ == "__main__":
    unittest.main()
