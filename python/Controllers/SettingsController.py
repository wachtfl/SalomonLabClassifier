from Model.Data import Data
from Model.Settings_m import SettingsM
from Controllers.DataHandler import DataHandler
from Model import Def
from Controllers.IAlgController import IAlgController
from Controllers.SVMController import SVMController
import threading


class SettingsController():
    print('in settings controller')
    numOfFilesToSave = 2
    dataModel = Data(numOfFilesToSave) #init here hoe many files need to be chosen

    algs = [Def.ALGORITHMS.SVM, Def.ALGORITHMS.NN]
    settingsModel = SettingsM(algs)

    algHandler = SVMController(dataModel) #change it later to initiate by type, and use IAlgController
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

    def startDecoding(self):
        # check that all params are set - 2 data files, algorithm and decoding mode:
        try:
            t = threading.Thread(target=self.algHandler.runAlgorithm)
            t.start()
        except:
            print("Error: unable to start thread for decoding")

    def updateDataModel(self):
        self.dataHandler.updateDataModel()

    def onCompleteChoosingData(self):
        # do whatever needed when initialize here
        self.dataHandler.updateDataModel()
        self.dataHandler.copyFilesTorawDataDir()

    def isDataOk(self):
        msg = 'please complete data selection first.\n' + str(
            self.dataModel.getNumOfFiles()) + ' files should be selected, but ' + str(
            self.dataHandler.getNumChosen()) + ' was selected.'
        return self.dataHandler.getNumChosen() == self.dataHandler.getNumFilesShouldBeSelected(), msg

    def setChosenAlgorithem(self, alg):
        self.settingsModel.chosenClassifier = alg

    def setFileName(self, num, path, name):
        self.dataHandler.setFileName(num, path, name)

    def getFileName(self, num):
        return self.dataHandler.getFileName(num)
