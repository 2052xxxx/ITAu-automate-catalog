#!/usr/bin/env python3

import os, PIL
from PIL import Image

file_path = os.path.expanduser('~') + '/supplier-data/images/'
		
for image in os.listdir(file_path):
    if '.' in image:
        pre, ext = os.path.splitext(image)
        fixed_filename = pre + ".jpeg"
        fixed_path = os.path.join(file_path, fixed_filename)

        img = Image.open(file_path + image)
        img.resize((600,400)).convert("RGB").save(fixed_path)
        img.close()

