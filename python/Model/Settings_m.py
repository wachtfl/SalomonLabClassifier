
from Model.Data import Data

class SettingsM:
    def __init__(self, algList):
        self.classifierTypes = algList
        chosenClassifier = None
        target = None
        numOfPermutations = 1  # or another default value?
        testSet = 20  # or another default value?

    def getAlgorithms(self):
        return self.classifierTypes

    def setChosenAlgorithem(self, alg):
        self.chosenClassifier = alg
        print('settings model: chosen alg is: ' + self.chosenClassifier)

    def getChosenAlgorithm(self):
        return self.chosenClassifier

    def setTargetForClassification(self, target):
        self.target = target
        print('settings model: target ' + target + ' is set')


