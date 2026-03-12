import os
from config import SCAN_DIRECTORIES

def collect_files():

    files = []

    for directory in SCAN_DIRECTORIES:

        for root, dirs, filenames in os.walk(directory):

            for f in filenames:
                path = os.path.join(root, f)
                files.append(path)

    return files