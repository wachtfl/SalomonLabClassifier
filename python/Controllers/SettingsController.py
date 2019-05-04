from Model.Data import Data
from Model.Settings_m import SettingsM

class SettingsController:
    dataModel = Data(2) #init here hoe many files need to be chosen
    settingsModel = SettingsM(['SVM']) # initialize any classification algorithms names here

    def getFeatures(self):
        return self.dataModel.getFeatures()

    def getAlgorithms(self):
        return self.settingsModel.getAlgorithms()

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