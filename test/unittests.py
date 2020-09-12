import unittest

class BubbleSortTest(unittest.TestCase):

    def test_unsorted_list(self):
        list = [4, 2, 1, 6, 3, 5]
        self.assertEqual(list.bubbleSort(), [1, 2, 3, 4, 5, 6])
        
    def test_sorted_list(self):
        list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(list.bubbleSort(), list)
        
    def test_single_list(self):
        list = [1]
        self.assertEqual(list.bubbleSort(), list)
