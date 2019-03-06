
from Model.Data import Data

class SettingsM:
    def __init__(self, ):
        self.data = Data(features=['a', 'b', 'c'])


    target = None
    classifierTypes = ['initialie here a list of classifier algorithms']
    numOfPermutations = 1  # or another default value?
    testSet = 20  # or another default value?

    def getAlgorithms(self):
        return self.classifierTypes

    def getFeatures(self):
        return self.data.getFeatures()

