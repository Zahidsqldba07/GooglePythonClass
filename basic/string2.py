#!/usr/bin/env python3
"""
created: 2022-04-20 21:32:57
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Basic String Exercises
license: None
"""

import unittest


# D. verbing
# Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case
# add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.
def verbing(s):
    if len(s) >= 3 and not s.endswith('ing'):
        s += 'ing'
    elif len(s) >= 3 and s.endswith('ing'):
        s += 'ly'
    elif len(s) >= 3 and s.endswith('ly'):
        s = s.replace('ly', 'ing')
    return s


# E. not_bad
# Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string.
# So 'This dinner is not that bad!' yields: This dinner is good!
def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if (n == -1 or b == -1) or n > b:
        return s
    else:
        not_bad_sub = s[n: b + 3]
        s = s.replace(not_bad_sub, 'good')

    return s


# F. front_back
# Consider dividing a string into two halves. If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half. e.g. 'abcde', the front half is 'abc',
# the back half 'de'. Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back
def front_back(a, b):
    def split_me(s):
        if len(s) % 2 == 0:
            i = len(s) // 2
        else:
            i = len(s) // 2 + 1
        front, back = s[:i], s[i:]
        return front, back

    a_front, a_back = split_me(a)[0], split_me(a)[1]
    b_front, b_back = split_me(b)[0], split_me(b)[1]

    return f'{a_front}{b_front}{a_back}{b_back}'


class TestSolution(unittest.TestCase):
    """ Unittests to check if each solution result is correct or not."""

    def test_verbing(self):
        """Test verbing solution."""
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swiming'), 'swimingly')
        self.assertEqual(verbing('do'), 'do')

    def test_not_bad(self):
        """Test not_bad solution"""
        self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
        self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
        self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

    def test_front_back(self):
        """Test front_back solution"""
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    unittest.main()
