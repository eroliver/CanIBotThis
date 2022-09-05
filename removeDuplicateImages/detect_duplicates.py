from difPy import dif
from os import rename, walk, path


parentDir0 ='L:\\Dump\\PhoneM'
parentDir1 ='L:\\Dump\\PM may2017'
newDir ='L:\\Dump\\PM Cleaned'

directories = ['L:\\eric phone', 'L:\\Lenovo']

def recursiveDif(parent_directory):
    for root, dirs, files in walk(parent_directory):
        for dir in dirs:
            currentDir = path.join(root, dir)
            dif(currentDir, delete=True, silent_del=True)

for directory in directories:
    recursiveDif(directory)
