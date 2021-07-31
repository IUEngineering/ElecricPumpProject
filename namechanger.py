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
