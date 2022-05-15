#!/usr/bin/env python3
"""
created: 2022-04-20 20:07:29
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Basic String Exercises
license: None
"""

import unittest


# Basic string exercises
# Fill in the code for the functions below. main() is already set up to call the functions with a few different inputs,
# printing 'OK' when each function is correct. The starter code for each function includes a 'return' which is just a
# placeholder for your code. It's ok if you do not complete all the functions, and there are some additional functions
# to try in string2.py.


# A. donuts
# Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count>
# is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'
def donuts(n):
    return f"Number of donuts: {(n, 'many')[n >= 10]}"


# B. both_ends
# Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring'
# yields 'spng'. However, if the string length is less than 2, return instead the empty string.
def both_ends(s):
    return f'{s[:2]}{s[-2:]}' if len(s) >= 2 else ''


# C. fix_start
# Given a string s, return a string where all occurences of its first char have been changed to '*', except do not
# change the first char itself. e.g. 'babble' yields 'ba**le'. Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.
def fix_start(s):
    s = list(s)
    for i, letter in enumerate(s[1:]):
        if letter == s[0]:
            s[i + 1] = '*'

    return ''.join(s)


# D. MixUp
# Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap
# the first 2 chars of each string. e.g. ('mix', pod' -> 'pox mid'), ('dog', 'dinner' -> 'dig donner')
# Assume a and b are length 2 or more.
def mix_up(a, b):
    return f'{b[:2]}{a[2:]} {a[:2]}{b[2:]}'


class TestSolution(unittest.TestCase):
    """ Unittests to check if each solution result is correct or not."""

    def test_donuts(self):
        """Tests donuts solution."""
        self.assertEqual(donuts(4), 'Number of donuts: 4')
        self.assertEqual(donuts(9), 'Number of donuts: 9')
        self.assertEqual(donuts(10), 'Number of donuts: many')
        self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
        """Tests both_ends solution."""
        self.assertEqual(both_ends('spring'), 'spng')
        self.assertEqual(both_ends('Hello'), 'Helo')
        self.assertEqual(both_ends('a'), '')
        self.assertEqual(both_ends('xyz'), 'xyyz')

    def test_fix_start(self):
        """Test fix_start solution."""
        self.assertEqual(fix_start('babble'), 'ba**le')
        self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
        self.assertEqual(fix_start('google'), 'goo*le')
        self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
        """Tests mix_up solution."""
        self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
        self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
        self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
        self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
    unittest.main()
