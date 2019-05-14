from Model.Data import Data
from shutil import copyfile
import os
import sys
import shutil


class DataHandler:
    pass

    def __init__(self, data):
        self.data = data

    def fileChoosingCompleted(self):
        #copy the files to /raw data
        paths = self.data.getPathSToData()
        pathsToDirs = self.data.getPathsToDataDirs()
        currentDir = os.getcwd()
        rawDataDir = currentDir + '\..\..\\raw data'
        for i in range(len(paths)):
            try:
                shutil.copy2(paths[i], rawDataDir)
            except Exception as e:
                print("Error: %s" % str(e)) # if the file was chosen from raw data folde it will catch exception and prints msg. not good but harmless... fix later
            finally:
                pass

                # what else? electodes, features?