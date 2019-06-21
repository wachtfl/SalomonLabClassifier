"""
This class represents all the user saved data,
and any information regarding it should be saved here.
"""

class Data:

    def __init__(self, numOfFiles):
        """
        Constructor.
        :param numOfFiles:  num of files supported
        """
        self.numOfFiles = numOfFiles
        self.pathToDataDir = []
        self.pathToData= []
        self.features = None

    def getFeatures(self):
        """
        :return: list of the data features. strings
        """
        if self.features != None:
            return self.features
        else:
            return ['data features are not initialized']

    def setNumOfFiles(self, num):
        """
        :param num: num of files supported
        :return:
        """
        self.numOfFiles = num

    def getNumOfFiles(self):
        """
        :return: num of files supported
        """
        return self.numOfFiles

    def setFeatures(self, features):
        """
        :param features: list of data features as strings
        :return:
        """
        self.features = features

    def clearAllPaths(self):
        """
        clear all data saved
        """
        self.pathToData.clear()
        self.pathToDataDir.clear()

    def getPathToData(self):
        """
        :return: list of strings, abs paths to data files
        """
        if self.pathToData != None:
            return self.pathToData
        else:
            return ['Data is not initialized']

    def getPathsToDataDirs(self):
        """
        :return: list of strings, abs paths to data directories
        """
        return self.pathToDataDir

    def setPath(self, path, fileName):
        """
        :param path: abs path to directory
        :param fileName: abs path to file
        """
        self.pathToDataDir.append(path)
        self.pathToData.append(fileName)
