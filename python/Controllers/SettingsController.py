from Model.Data import Data
from Model.Settings_m import SettingsM

from Controllers.IAlgController import IAlgController
from Controllers.SVMController import SVMController

class SettingsController():
    dataModel = Data(2) #init here hoe many files need to be chosen
    settingsModel = SettingsM(['SVM', 'bbb', 'ggg']) # initialize any classification algorithms names here
    algHandler = SVMController()    #change it later to initiate by type, and use IAlgController


    def getFeatures(self):
        return self.dataModel.getFeatures()

    def getAlgorithms(self):
        return self.settingsModel.getAlgorithms()

    def getDecodingTypes(self):
        classifierType = self.getChosenAlgorithm()
        if classifierType == "SVM": #change later to enum
            return ['spatial', 'temporal', 'spatio-tempral'] #also cahnge to enum
        else:
            return ['SVM not chosen...']

    def setDecodingMode(self, mode):
        self.algHandler.setDecodingMode(mode)

    def setChosenAlgorithm(self, alg):
        self.settingsModel.setChosenAlgorithem(alg)

    def getChosenAlgorithm(self):
        return self.settingsModel.getChosenAlgorithm()

    def setTargetForClassification(self, target):
        self.settingsModel.setTargetForClassification(target)

    def setPathToData(self, path, fileName):
        self.dataModel.setPath(path, fileName)

    def getPathToData(self):
        return self.dataModel.getPathToData()

    def onCompleteChoosingData(self):
        # do whatever needed when initialize here
        pass

    def isDataOk(self):
        msg = 'please complete data selection first.\n' + str(
            self.dataModel.getNumOfFiles()) + ' files should be selected, but only ' + str(
            len(self.dataModel.pathToData)) + ' was selected.'
        return len(self.dataModel.pathToData) == self.dataModel.getNumOfFiles(), msg

    def setChosenAlgorithem(self, alg):
        self.settingsModel.chosenClassifier = alg