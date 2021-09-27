# change the name of files within a directory, recursively, pattern-matching
from pathlib import Path
import re
import os

# directory
input_directory = '/home/hernandom/data/Microscopy_Data/Plasticity/PH3_inmuno/Processed_data/PH308/'
# pattern to replace
pattern_to_replace = '_manualROI-Caudo'
pattern_to_replace_with = '_manualROI-Both-Caudo'

# go through all files
for path in Path(input_directory).rglob('*' + pattern_to_replace + '*'):
    new_name = re.sub(pattern_to_replace, pattern_to_replace_with, str(path.resolve()))
    print(new_name)
    os.rename(str(path.resolve()), new_name)
