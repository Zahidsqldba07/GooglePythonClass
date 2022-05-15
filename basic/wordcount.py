#!/usr/bin/env python3
"""
created: 2022-04-21 16:26:12
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Wordcount

metadoc: For the --count flag, implement a print_words(filename) function that counts
         how often each word appears in the text and prints:
         word1 count1
         word2 count2

         For the --top_count flag, implement a print_top(filename) which is similar
         to print_words() but which prints just the top 20 most common words sorted
         so the most common word is first, then the next most common, and so on.
         Use str.split() (no arguments) to split on all whitespace.

license: None
"""

import sys
from collections import Counter
from string import punctuation


def get_file(filename):
    with open(filename) as fo:
        content = [i.strip().lower() for i in fo]
    return ' '.join(content)


def process_file(file_content):
    # str_output = ''
    file_content = file_content.replace('--', '  ')
    file_content = file_content.replace('.', '. ')
    file_content = file_content.replace('  ', '')
    for word in file_content:
        for letter in word:
            if letter in punctuation:
                file_content = file_content.replace(letter, '')
    return file_content


def print_words(filename, option):
    tt = (None, 20)[option == 2]
    alice_file = get_file(filename)
    processed_alice_file = process_file(alice_file)
    print(f"-- {('Total words', 'Top 20 words')[option == 2]} in Alice in Wonderland! --\n")
    d = Counter(processed_alice_file.split())
    for word, count in sorted(d.items(), key=lambda i: i[1], reverse=True)[:tt]:
        print(f'\t{word:<18}: {count:<5}')
    print(f'\nTotal unique words:\t{len(d)}')
    print()


print(print_words('alice.txt', 1))


def main():
    while user_input := int(input('Select (1) total word count or (2) for Top 20 most frequent words:\n> ')):
        print_words('alice.txt', user_input)


if __name__ == '__main__':
    main()
