"""
This Class Represents the Settings tab Model.
holds all relevant data
"""

class Settings:
    def __init__(self, algList):
        """
        Constructor.
        :param algList: list of strings.
        """
        self.classifierTypes = algList
        self.chosenClassifier = None# Def.ALGORITHMS.SVM # default value

    def getAlgorithms(self):
        """
        :return: list of alforithms, strings.
        """
        return self.classifierTypes

    def setChosenAlgorithem(self, alg):
        """
        :param alg: the chosen algorithm, string
        :return:
        """
        self.chosenClassifier = alg
        print('settings model: chosen alg is: ' + self.chosenClassifier)

    def getChosenAlgorithm(self):
        """
        :return: the chosen algorithm, string
        """
        return self.chosenClassifier

    def setTargetForClassification(self, target):
        """
        :param target: target feature for classification, string
        """
        self.target = target
        print('settings model: target ' + target + ' is set')


