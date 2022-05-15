# Basic Python Exercises

This directory contains my authentic solutions to the Basic Python Exercises. Nick Parlante's sample solutions can be found [here](https://github.com/seraph776/GooglePythonClass/tree/main/solutions/basics).



## Directory File Content

- **alice.txt** - This text file contains _Alice in Wonderland_ by Lewis Carroll, and is used for `wordcount.py`
- **list1.py** -  Contains several `lists` challenges with `unittests`. 
- **list2.py** - Contains several `list` challenges with `unittests`. 
- **mimic.py** - This program that maps each word that appears in the file to a list of all the words that immediately follow that word in the file.
- **small.txt** - This file is not used. It came with the original sourcecode with no instructions for its use.   
- **string1.py** - Contains several `string` challenges with `unittests`. 
- **string2.py** - Contains several `string` challenges with `unittests`. 
- **wordcount.py** - This program counts the total number of words, as well as the top 20 most frequent words in a given file.

  
### List1.py
> **match_ends**
> 
> Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first
and last chars of the string are the same. Note: python does not have a ++ operator, but += works.

```python
def match_ends(words):
    return sum([1 for i in words if len(i) >= 2 and i[0] == i[-1]])
```

> **front_x**
> 
> Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  
> e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']   

```python
def front_x(words):
    x_list = sorted([i for i in words if i.startswith('x')])
    a_list = sorted([i for i in words if i not in x_list])
    return x_list + a_list
```

>  **sort_last**
>
> Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.   
> e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


```python
def sort_last(tuples):
    return sorted(tuples, key=lambda i: i[1])
```

### List2.py

> **remove_adjacent**
> 
> Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element,
> so [1, 2, 2, 3] returns [1, 2, 3]. 

```python
def remove_adjacent(nums):
    output = []
    for num in nums:
        if len(output) == 0 or num != output[-1]:
            output.append(num)
    return output
```

> **linear_merge**
> 
> Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order.
You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single
pass of both lists.

```python
def linear_merge(list1, list2):
    return sorted(list1 + list2)
```

### Mimic.py

```python

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

```

### String1.py

> **donuts**
> 
> Given an int count of a number of donuts, return a string of the form 'Number of donuts: <count>', where <count>
> is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
> So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'

```python
def donuts(n):
    return f"Number of donuts: {(n, 'many')[n >= 10]}"
```

> **both_ends**
> 
> Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring'
> yields 'spng'. However, if the string length is less than 2, return instead the empty string.

```python
def both_ends(s):
    return f'{s[:2]}{s[-2:]}' if len(s) >= 2 else ''
```

> **fix_start**
> 
> Given a string s, return a string where all occurences of its first char have been changed to '*', except do not
> change the first char itself. e.g. 'babble' yields 'ba**le'. Assume that the string is length 1 or more.

```python
def fix_start(s):
    s = list(s)
    for i, letter in enumerate(s[1:]):
        if letter == s[0]:
            s[i + 1] = '*'

    return ''.join(s)
```

> **MixUp**
> 
> Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap
> the first 2 chars of each string. e.g. ('mix', pod' -> 'pox mid'), ('dog', 'dinner' -> 'dig donner')
> Assume a and b are length 2 or more.

```python
def mix_up(a, b):
    return f'{b[:2]}{a[2:]} {a[:2]}{b[2:]}'
```

### String2.py

> **verbing**
> 
> Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case
> add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.

```python
def verbing(s):
    if len(s) >= 3 and not s.endswith('ing'):
        s += 'ing'
    elif len(s) >= 3 and s.endswith('ing'):
        s += 'ly'
    elif len(s) >= 3 and s.endswith('ly'):
        s = s.replace('ly', 'ing')
    return s
```

>  **not_bad**
> 
> Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows
> the 'not', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string.
> So 'This dinner is not that bad!' yields: This dinner is good!

```python
def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if (n == -1 or b == -1) or n > b:
        return s
    else:
        not_bad_sub = s[n: b + 3]
        s = s.replace(not_bad_sub, 'good')

    return s
```
 
> **front_back**
> 
> Consider dividing a string into two halves. If the length is even, the front and back halves are the same length.
> If the length is odd, we'll say that the extra char goes in the front half. e.g. 'abcde', the front half is 'abc',
> the back half 'de'. Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back

```python
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
```

### Wordcount.py

```python
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
```