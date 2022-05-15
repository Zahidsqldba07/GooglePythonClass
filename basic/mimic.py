#!/usr/bin/env python3
"""
created: 2022-04-21 18:58:14
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Mimic Exercises
license: None

metadoc: Build a "mimic" dict that maps each word that appears in the file to a list of all the words that
         immediately follow that word in the file. The list of words can be in any order and should include
         duplicates. So for example the key "and" might have the list ["then", "best", "then", "after", ...]
         listing all the words which came after "and" in the text. We'll say that the empty string is what
         comes before the first word in the file.

         With the mimic dict, it's fairly easy to emit random text that mimics the original. Print a word,
         then look up what words might come next and pick one at random as the next work.
"""
from textwrap import fill
from random import choice
from string import punctuation


def get_file(filename: str) -> str:
    """Opens the text file"""
    with open(filename) as alice_file:
        content = alice_file.read()
    return content


def build_dict(datafile: str) -> dict:
    """Strips punctuation from datafile and builds mimic dictionary"""
    str_output = ''
    for i in datafile:
        if i not in punctuation:
            str_output += i

    str_output = str_output.lower().split()

    # Start with all words as keys and empty list as value
    d = {word: [] for word in str_output}
    for i in range(len(str_output) - 1):
        # if the word is in d then append next value
        if str_output[i] in d:
            d[str_output[i]].append(str_output[i + 1])
    return d


def mimic_dict(filename, word):
    """Given mimic dict and start word, prints 200 random words."""
    # get alice in wonderland file
    data = get_file(filename)
    # Build mimic dictionary
    data_dict = build_dict(data)
    output = []
    for _ in range(200):
        next_values = data_dict.get(word, ' ')
        next_value = choice(next_values)
        output.append(next_value)
    output = ' '.join(output).capitalize()
    return ''.join(fill(output, width=80)) + '\n'


if __name__ == '__main__':
    while user_input := input('Enter a word:\n>> '):
        print(mimic_dict('alice.txt', user_input))
