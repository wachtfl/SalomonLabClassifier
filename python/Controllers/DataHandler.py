
"""
This class represents a data controller.
In charge of saving the data locations, copy them and
manipulate if needed. has an 'Data' object as a Model.
"""

import os
import shutil

class DataHandler:

    def __init__(self, data):
        """
        Constructor.
        :param data: Data object (Model)
        """
        print('in data handler CONSTRUCTOR')
        self.data = data
        self.fileName1 = ''
        self.path1 = ''
        self.fileName2 = ''
        self.path2 = ''

    def setFileName(self, num, path, name):
        """
        sets the tmp file name
        :param num: file number (1 or 2)
        :param path: abs path to directory
        :param name: abs path to file
        """
        if num == 1:
            self.path1 = path
            self.fileName1 = name
        if num == 2:
            self.path2 = path
            self.fileName2 = name

    def getFileName(self, num):
        """
        :param num: number of file to get (1 or 2)
        :return: abs path to file_num
        """
        if num == 1:
            return self.fileName1
        if num == 2:
            return self.fileName2

    def updateDataModel(self):
        """
        final updates of the Data Model
        """
        self.data.clearAllPaths()
        if self.fileName1 != '':
            self.data.setPath(self.path1, self.fileName1)
        if self.fileName2 != '':
            self.data.setPath(self.path2, self.fileName2)

    def getNumChosen(self):
        """
        :return: num of files that are allready chosen
        """
        count = 0
        if self.fileName1 != '':
            count += 1
        if self.fileName2 != '':
            count += 1
        return count


    def getNumFilesShouldBeSelected(self):
        """
        :return: number of files that the user should select
        """
        return self.data.getNumOfFiles()

    def copyFilesTorawDataDir(self):
        """
        copy the files selected to the project raw data directory
        :return:
        """
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
