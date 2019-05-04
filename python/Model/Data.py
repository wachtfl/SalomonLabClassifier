class Data:
    #
    # def __init__(self, features, pathToData):
    #     self.pathToData = pathToData
    #     self.features = features

    def __init__(self, numOfFiles):
        self.numOfFiles = numOfFiles
        self.pathToDataDir = []
        self.pathToData= []
        self.features = None

    def getFeatures(self):
        if self.features != None:
            return self.features
        else:
            return ['data features are not initialized']

    def setNumOfFiles(self, num):
        self.numOfFiles = num

    def getNumOfFiles(self):
        return self.numOfFiles

    def setFeatures(self, featues):
        self.features = featues

    def getPathSToData(self):
        if self.pathToData != None:
            return self.pathToData
        else:
            return ['Data is not initialized']

    def setPath(self, path, fileName):
        self.pathToDataDir.append(path)
        self.pathToData.append(fileName)
