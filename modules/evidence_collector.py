import os
from config import SCAN_DIRECTORIES

def collect_files():

    collected_files = []

    for directory in SCAN_DIRECTORIES:

        for root, dirs, files in os.walk(directory):

            for file in files:

                path = os.path.join(root,file)
                collected_files.append(path)

    return collected_files