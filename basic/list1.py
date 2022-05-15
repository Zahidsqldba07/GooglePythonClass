#!/usr/bin/env python3
"""
created: 2022-04-21 16:00:16
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Basic List Exercises
license: None
"""


# A. match_ends
# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first
# and last chars of the string are the same. Note: python does not have a ++ operator, but += works.
import unittest


def match_ends(words):
    return sum([1 for i in words if len(i) >= 2 and i[0] == i[-1]])


# B. front_x
# Given a list of strings, return a list with the strings in sorted order, except group all the strings that
# begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
def front_x(words):
    x_list = sorted([i for i in words if i.startswith('x')])
    a_list = sorted([i for i in words if i not in x_list])
    return x_list + a_list


#
# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    return sorted(tuples, key=lambda i: i[1])


class TestSolution(unittest.TestCase):
    """ Unittests to check if each solution result is correct or not."""

    def test_match_ends(self):
        """Tests match_end solution"""
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        """Tests front_x solution"""
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
                         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        """Tests sort_last solution"""
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    unittest.main()
