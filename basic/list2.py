#!/usr/bin/env python3
"""
created: 2022-04-21 16:00:16
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Basic List Exercises
license: None
"""

import unittest


# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
def remove_adjacent(nums):
    output = []
    for num in nums:
        if len(output) == 0 or num != output[-1]:
            output.append(num)
    return output


# E. linear_merge
# Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order.
# You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    return sorted(list1 + list2)


class TestsSolutions(unittest.TestCase):
    """ Unittests to check if each solution result is correct or not."""

    def test_remove_adjacent(self):
        """Tests remove adjacent solution"""
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        """Tests linear_merge solution"""
        self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    unittest.main()
