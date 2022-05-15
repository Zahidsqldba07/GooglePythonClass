# Copy Special

This directory contains my authentic solution to the CopySpecial Exercise. Nick Parlante's sample solution can be found [here](https://github.com/seraph776/GooglePythonClass/tree/main/solutions/copyspecial).



## Instructions 

- **Objective 1**: `get_special_path()`: Find all "special files" and list them by their absolute paths.
 A special filename has two underscore followed by 1 or more word chars followed by two underscores.
 For example: xx__something__.jpg, xxy__special__.txt

- **Objective 2**: `copy_to_directory()`: Create a function that takes two arguments (src, dest). Move all special files to
 destination folder. If the folder does not exist, create it.

- **Objective 3**: `zip_special_files()`: Create a function that takes 1 argument (zip_name) that find all "special files"
 and invoke the zip utilities and zip files into a file specified with zip_name.


```python
import sys
import os
import re
import shutil
from zipfile import ZipFile

# constants
SOURCE_PATH = os.path.join(os.getcwd(), 'FolderA')
DESTINATION_PATH = os.path.join(os.getcwd(), 'FolderB')


def get_files(source: str) -> tuple:
    """This function gets the files, and applies regex to filter special files."""
    files = os.listdir(source)
    pattern = re.compile(r'__([a-zA-Z]){2,}__')
    matches = pattern.finditer('\n'.join(files))
    group = [file.group() for file in matches]
    return files, group


def get_special_path(source: str) -> None:
    """Prints the full path of all special files."""
    files, group = get_files(source)
    special_files = [file for file in files for s in group if s in file]
    for file in special_files:
        full_path = os.path.join(source, file)
        print(full_path)


def copy_to_directory(source: str, destination: str) -> None:
    """This functions copies special files from source to destination folder."""
    source_files = os.listdir(source)
    files, group = get_files(source)
    special_files = [file for file in files for s in group if s in file]
    for file in special_files:
        full_path = os.path.join(source, file)
        if os.path.isfile(full_path):
            shutil.copy(full_path, destination)
    print(f"The following files have been moved successfully!")
    for i, file in enumerate(special_files, start=1):
        print(f"\t{i}) {file}")


def zip_special_files(source: str) -> None:
    """"This function zips all special files in the container folder."""
    files = os.listdir(source)
    os.chdir(source)
    with ZipFile('special_zip.zip', 'w') as zipper:
        for file in files:
            zipper.write(file)
    print('Special files have been been zipped successfully!')


if __name__ == '__main__':
    get_special_path(SOURCE_PATH)
    copy_to_directory(SOURCE_PATH, DESTINATION_PATH)
    zip_special_files(DESTINATION_PATH)

```