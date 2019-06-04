
from Model.Data import Data
from Model import Def

class SettingsM:
    def __init__(self, algList):
        self.classifierTypes = algList
        self.chosenClassifier = None# Def.ALGORITHMS.SVM # default value

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


