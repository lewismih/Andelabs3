from Missing_Number import num_finder
import unittest

        
class MissingNumberTest(unittest.TestCase):
   
    def test_empty_list(self):
        self.assertEqual(0, num_finder([], []),
                         msg='should return 0 for empty list')

    def test_same_entries(self):
        list1 = num_finder([9], [9])
        list2 = num_finder([17], [17])
        list3 = num_finder([5], [5])
        self.assertListEqual([0, 0, 0],
                             [list1, list2, list3],
                             msg='should return 0 for lists with the same entries')

    def test_missing_entries(self):
        list1 = num_finder([4, 9], [4, 9, 5])
        list2 = num_finder([5, 13, 7, 31, 11, 42], [5, 13, 22, 7, 31, 11, 42])
        list3 = num_finder([16, 8, 3 ], [8, 3, 16,  10])
        self.assertListEqual([5, 22, 10, ],
                             [list1, list2, list3],
                             msg='should return the missing number for lists with similar entries and a missing number')

if __name__ == '__main__':
unittest.main()