#!/usr/bin/env python3
"""
created: 2022-04-22 05:24:49
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Baby Names exercise
metadoc: Define the extract_names() function below and change main() to call it.
         Here's what the html looks like in the baby.html files:
         ...
         <h3 align="center">Popularity in 1990</h3>
         ....
         <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
         <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
         <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>

         Suggested milestones for incremental development:
         - Extract the year and print it
         - Extract the names and rank numbers and just print them
         - Get the name log_data into a dict and print it
         - Build the [year, 'name rank', ... ] list and print it
         - Fix main() to use the extract_names list
license: None
"""
import os

from bs4 import BeautifulSoup
import html5lib
from collections import namedtuple

Record = namedtuple(f'record', ['rank', 'boy_name', 'girl_name'])


def get_soup_object(filename):
    with open(filename) as html_file:
        soup_obj = BeautifulSoup(html_file, 'html5lib')
    return soup_obj


def refine_soup_object(soup_object):
    raw_output = []
    soup_title = soup_object.title.text
    # TODO: There is a bug here!
    soup_subtitle = soup_object.findAll('h3', {'align': 'center'})[0].text
    data_year = ''.join([i for i in soup_subtitle if i.isdigit()])
    name_data = soup_object.findAll('tr', {'align': 'right'})
    raw_output = ' '.join([col.text for row in name_data for col in row]).split('\n')
    return data_year, raw_output


def structure_data(raw_output) -> dict[str: tuple]:
    #
    data_dict = {}
    name_data = []

    year, soup = raw_output
    idx = 0
    while True:
        if idx == len(soup) - 1:
            break
        rank, boy_name, girl_name = soup[idx].split()[0], soup[idx].split()[1], soup[idx].split()[2]
        record = Record(rank=rank, boy_name=boy_name, girl_name=girl_name)
        name_data.append(record)
        idx += 1
    data_dict[year] = tuple(name_data)
    return data_dict


def write_to_file(name_dict):
    for key, value in name_dict.items():
        with open(f'data_dump/babynames_{key}.txt', 'w') as file_obj:
            # Title and Year:
            file_obj.write(f'Popular baby names in {key}\n')
            for record in value:
                # Writing log_data:
                file_obj.write(', '.join((record.rank, record.boy_name, record.girl_name)) + '\n')
    print('Data has been successfully written to file!')


if __name__ == '__main__':
    list_of_files = os.listdir()
    try:
        for file in list_of_files:
            data = refine_soup_object(get_soup_object(file))
            baby_names = structure_data(data)
            write_to_file(baby_names)
    except IndexError as e:
        pass
