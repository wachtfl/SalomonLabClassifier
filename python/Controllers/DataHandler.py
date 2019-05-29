from Model.Data import Data
from shutil import copyfile
import os
import sys
import shutil


class DataHandler:

    def __init__(self, data):
        print('in data handler CONSTRUCTOR')

        self.data = data
        self.fileName1 = ""
        self.path1 = ""
        self.fileName2 = ""
        self.path2 = ""

    def setFileName1(self, path, name):
        self.path1 = path
        self.fileName1 = name

    def setFileName2(self, path, name):
        self.path2 = path
        self.fileName2 = name

    def getFileName1(self):
        return self.fileName1

    def getFileName2(self):
        return self.fileName2

    def fileChoosingCompleted(self):
        pass
        # copy the files to /raw data
        paths = self.data.getPathToData()
        pathsToDirs = self.data.getPathsToDataDirs()
        currentDir = os.getcwd()
        rawDataDir = currentDir + '\..\..\raw data'
        for i in range(len(paths)):
            try:
                shutil.copy2(paths[i], rawDataDir)
            except Exception as e:
                print("Error: %s" % str(e)) # if the file was chosen from raw data folde it will catch exception and prints msg. not good but harmless... fix later
            finally:
                pass

                # what else? electodes, features?