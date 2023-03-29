import os
import re
import shutil


def organize(path):
    if not os.path.isdir(path):
        return 'Path should be "dir"'

    if path[-1] != '/':
        path += '/'

    for file in os.listdir(path):
        if os.path.isfile(path + file):
            extension = re.search(r'\.\w+$', file)  # Take file extension

            # Check if file has extension
            if extension:
                extension = extension[0][1:].lower()
            else:
                extension = 'noExtension'

            extension += '/'

            # Check if folder exists
            if not os.path.exists(path + extension):
                os.mkdir(path + extension)
            else:
                shutil.move(path + file, path + extension + file)

    return 'Success!'
