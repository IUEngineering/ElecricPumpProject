import os
import time
from zipfile import ZipFile
from os.path import basename
from pytz import timezone
from datetime import datetime

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

def addingTime(baseName):
    timeadded = baseName[:-4]+"-"+("{0}").format(datetime.now(timezone('UTC')).astimezone(timezone('Europe/Berlin')))+baseName[-4:]
    x = timeadded.replace(":", "_")
    return x

