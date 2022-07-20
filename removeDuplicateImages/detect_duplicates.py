from difPy import dif
from os import rename, walk, path

#search = dif('L:\\Amandas phone\\Iphone\\100APPLE\\', similarity='high')
#print(search.lower_quality)


parentDir ='L:\\Amandas phone\\Iphone'

for root, dirs, files in walk(parentDir):
    for dir in dirs:
        currentDir = path.join(root, dir)
        dif(currentDir, delete=True, silent_del=True)

