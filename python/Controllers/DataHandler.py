from Model.Data import Data
from shutil import copyfile
import os
import sys
import shutil


class DataHandler:

    def __init__(self, data):
        print('in data handler CONSTRUCTOR')
        self.data = data
        self.fileName1 = ''
        self.path1 = ''
        self.fileName2 = ''
        self.path2 = ''

    def setFileName(self, num, path, name):
        if num == 1:
            self.path1 = path
            self.fileName1 = name
        if num == 2:
            self.path2 = path
            self.fileName2 = name

    def getFileName(self, num):
        if num == 1:
            return self.fileName1
        if num == 2:
            return self.fileName2

    def updateDataModel(self):
        self.data.clearAllPaths()
        if self.fileName1 != '':
            self.data.setPath(self.fileName1, self.path1)
        if self.fileName2 != '':
            self.data.setPath(self.fileName2, self.path2)

    def getNumChosen(self):
        count = 0
        if self.fileName1 != '':
            count += 1
        if self.fileName2 != '':
            count += 1
        return count


    def getNumFilesShouldBeSelected(self):
        return self.data.getNumOfFiles()

    def copyFilesTorawDataDir(self):
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