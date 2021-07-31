import os
from zipfile import ZipFile
from os.path import basename

def newName(baseName):
    """Checks if baseName exists, if not inserts a running
    counter and increments it until file does not exist."""

    n = baseName[:-4]+"{}"+baseName[-4:]  # assumes a len-3 filenameextension like txt
    if not os.path.exists(baseName):
        return baseName

    i = 0
    while os.path.exists( n.format(i)):
        i+=1

    return n.format(i)

def latestName(baseName):
    n = baseName[:-4]+"{}"+baseName[-4:]  # assumes a len-3 filenameextension like txt
    if not os.path.exists(baseName):
        return baseName

    i = 0
    while os.path.exists( n.format(i)):
        i+=1

    return n.format(i-1)


# Zip the files from given directory that matches the filter
def zipFilesInDir(dirName, zipFileName, filter):
   # create a ZipFile object
   with ZipFile(zipFileName, 'w') as zipObj:
       # Iterate over all the files in directory
       for folderName, subfolders, filenames in os.walk(dirName):
           for filename in filenames:
               if filter(filename):
                   # create complete filepath of file in directory
                   filePath = os.path.join(folderName, filename)
                   # Add file to zip
                   zipObj.write(filePath, basename(filePath))