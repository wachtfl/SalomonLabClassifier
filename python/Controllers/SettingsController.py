from Model.Data import Data
from Model.Settings_m import SettingsM
from Controllers.DataHandler import DataHandler
from Model import Def
from Controllers.IAlgController import IAlgController
from Controllers.SVMController import SVMController

class SettingsController():
    dataModel = Data(2) #init here hoe many files need to be chosen
    #algs = [attr for attr in dir(Def.ALGORITHMS) if not callable(getattr(Def.ALGORITHMS, attr)) and not attr.startswith("__")]  # initialize any classification algorithms names in Def.ALGORITHMS
    algs = [Def.ALGORITHMS.SVM, Def.ALGORITHMS.NN]
    settingsModel = SettingsM(algs)

    algHandler = SVMController()    #change it later to initiate by type, and use IAlgController
    dataHandler = DataHandler(dataModel)

    def getFeatures(self):
        return self.dataModel.getFeatures()

    def getAlgorithms(self):
        return self.settingsModel.getAlgorithms()

    def getDecodingTypes(self):
        classifierType = self.getChosenAlgorithm()
        if classifierType == Def.ALGORITHMS.SVM:
            return [Def.DECODING_MODES.SPATIAL, Def.DECODING_MODES.TEMPORAL, Def.DECODING_MODES.SPATIO_TEMPORAL]
            #return [attr for attr in dir(Def.DECODING_MODES) if not attr.startswith("__")]
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

    def finishAndRunAlgorithm(self):
        #crate paramList accoding to the chosen algorithm:
        sbjNumber = 3 #get from user...
        params = [sbjNumber]
        self.algHandler.runAlgorithm(params)


    def setPathToData(self, path, fileName):
        self.dataModel.setPath(path, fileName)

    def getPathToData(self):
        return self.dataModel.getPathToData()

    def onCompleteChoosingData(self):
        # do whatever needed when initialize here
        self.dataHandler.fileChoosingCompleted()

    def isDataOk(self):
        msg = 'please complete data selection first.\n' + str(
            self.dataModel.getNumOfFiles()) + ' files should be selected, but only ' + str(
            len(self.dataModel.pathToData)) + ' was selected.'
        return len(self.dataModel.pathToData) == self.dataModel.getNumOfFiles(), msg

    def setChosenAlgorithem(self, alg):
        self.settingsModel.chosenClassifier = alg