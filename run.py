#! /usr/bin/env python3

import os
import requests

"""
{
    "name": "Test Fruit", 
    "weight": 100, 
    "description": "This is the description of my test fruit", 
    "image_name": "icon.sheet.png"
}
"""

fruits = []

url = "http://localhost/fruits/"
file_path = os.path.expanduser('~') + '/supplier-data/descriptions/'

for text in os.listdir(file_path):
    pre, ext = os.path.splitext(text)
    with open(file_path + text, "r") as file:
        fruits.append({
                    "name": file.readline().rstrip("\n"),
            		"weight": int(file.readline().rstrip("\n").split(" ")[0]),
            		"description": file.readline().rstrip("\n"),
            		"image_name": str(pre + ".jpeg").rstrip("\n")
                    })
        
# for i in fruits:
#     print(i)

for fruit in fruits:
    resp = requests.post(url, json=fruit)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Fruit description ID: {}'.format(resp.json()["id"]))