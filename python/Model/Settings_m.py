
from Model.Data import Data

class SettingsM:
    def __init__(self, algList):
        self.classifierTypes = algList

    target = None
    chosenClassifier = None
    numOfPermutations = 1  # or another default value?
    testSet = 20  # or another default value?

    def getAlgorithms(self):
        return self.classifierTypes

    def setChosenAlgorithem(self, alg):
        self.chosenClassifier = alg

