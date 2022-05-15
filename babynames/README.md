# Baby Names

This directory contains my authentic solution to the Baby Names Exercise. Nick Parlante's sample solution can be found [here](https://github.com/seraph776/GooglePythonClass/tree/main/solutions/babynames).



## Instructions

This directory contains several `.html` files which contain popular boy and girl names by year. Loop through each `.html`
file  in the directory and extract the `rank`, `boy name`, and `girl name` from every row in each file, 
and save the data in a `.txt` file in the `data_dump` directory with same file name as the respective `.html` file.  
For example, the data extracted from `baby1990.html` will be saved in a file named `baby1990.txt` - so on and so forth.

```python
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
```

### 🪳 Bugs

- The `try and except` block is used to suppress a `IndexError - list index out of range` Traceback that returns while processing the last `.html` file in the directory - `babynames_2006.html`. 
- Currently, `babynames.py` will not process the last file in the directory.  
