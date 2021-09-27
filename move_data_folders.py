#!/usr/bin/env python3

from pathlib import Path
from shutil import rmtree

datafolder = Path('/home/hernandom/data/Behavioural_Data/Bpod_data')

for folder in datafolder.glob('**/**/Data_Analysis'):
    print(f'::: {folder} :::')
    for content in folder.iterdir():
        print(content)
        content.rename(folder.parent / content.name)
    for item in folder.parent.iterdir():
        if item.is_dir():
            print(item)
            rmtree(str(item))
