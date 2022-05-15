#!/usr/bin/env python3
"""
created: 2022-04-27 19:31:51
@author: seraph776
contact: seraph776@gmail.com
project: Google Python Class - Log Puzzle
metadoc: Given an apache logfile, find the puzzle urls and download the image.
license: None
"""
import os
import shutil
import sys
import urllib.request
import requests


def get_log_file(filename):
    with open(filename) as fo:
        content = [i.strip() for i in fo.readlines()]
    return content


def filter_log_file(logfile):
    output = {}
    pattern = '/images/puzzle/'
    for line in logfile:
        if pattern in line:
            url = line.split()[0]
            image_file = line.split()[6]
            output[url] = image_file
    return output


def read_urls(log_file, save_log):
    """
    Returns a list of the puzzle urls from the given log file, extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into increasing order.
    """
    data_dict = filter_log_file(log_file)

    for k, v in sorted(data_dict.items()):
        data = ''.join([k, v])
        print(data)
        with open(save_log, 'a') as fo:
            fo.write(data + '\n')
    print()


def download_image(img_url, save_folder):
    r = requests.get(image_url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        filename = image_url.split('/')[-1]
        full_path = os.path.join(save_folder, filename)
        urllib.request.urlretrieve(image_url, full_path)
        print('Image was successfully downloaded!:', filename)
    else:
        print('Image could not be retrieved')


if __name__ == '__main__':
    image_url = r'https://raw.githubusercontent.com/seraph776/seraph776/main/assets/black-red-serpent.jpg'
    destination_folder = os.path.join(os.getcwd(), 'image')

    animal_logs = get_log_file('animal_code.google.com')
    place_logs = get_log_file('place_code.google.com')
    save_logs = 'log_data/data.txt'

    read_urls(animal_logs, save_logs)
    read_urls(place_logs, save_logs)
    download_image(image_url, destination_folder)


