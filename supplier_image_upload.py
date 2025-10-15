#!/usr/bin/env python3

import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
file_path = os.path.expanduser('~') + '/supplier-data/images/'

for image in os.listdir(file_path):
    if '.jpeg' in image:
        # print(file_path + image)
        with open(file_path + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})