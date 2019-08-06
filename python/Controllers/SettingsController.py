"""
Settings controller in charge on all logic that happens in the Settings screen.
gets and sets data in relevant Modlels, and initiates relevant methods.

holds and controls all the relevant Models:
Settings - as a Settings Model

activates the relevant controllers when needed:
dataHandler, algHandler
"""

from python.Model.Data import Data
from python.Model.Settings import Settings
from python.Model.AlogorithmsData import Algorithms, ALGORITHMS
from python.Controllers.DataHandler import DataHandler
from python.Model import Def
from python.Controllers.SVMController import SVMController
import threading


class SettingsController():
    numOfFilesToSave = 2
    dataModel = Data(numOfFilesToSave)       # init here how many files need to be chosen. as for now - only 2 is supported in all app.

    algModel = Algorithms()
    algs = algModel.getAlgorithms()
    settingsModel = Settings(algs)

    algHandler = SVMController(dataModel)   # after implement more algs, initiate by type, and use IAlgController
    dataHandler = DataHandler(dataModel)

    def getFeatures(self):
        """
        :return: return a list of data features from the data model
        """
        return self.dataModel.getFeatures()

    def getAlgorithms(self):
        """
        :return: list of available algorithms (strings)
        """
        return self.settingsModel.getAlgorithms()

    def getDecodingTypes(self):
        """
        :return: list of decoding modes (strings, from def)
        """
        classifierType = self.getChosenAlgorithm()
        if classifierType == ALGORITHMS.SVM:
            return [Def.DECODING_MODES.SPATIAL, Def.DECODING_MODES.TEMPORAL, Def.DECODING_MODES.SPATIO_TEMPORAL]
        else:
            return ['SVM not chosen...']

    def setDecodingMode(self, mode):
        """
        :param mode: string, from def
        :return:
        """
        self.algHandler.setDecodingMode(mode)

    def setChosenAlgorithm(self, alg):
        """
        :param alg: chosen alg, string.
        :return:
        """
        self.settingsModel.setChosenAlgorithem(alg)

    def getChosenAlgorithm(self):
        """
        :return: the chosen algorithm, string.
        """
        return self.settingsModel.getChosenAlgorithm()

    def setTargetForClassification(self, target):
        """
        :param target: define the target feature of classification from the features available.
        ---not in use---
        """
        self.settingsModel.setTargetForClassification(target)

    def startDecoding(self):
        """
        initiates a new thread for decoding and calls runAlgorithm from a IAlgController object
        """
        try:
            t = threading.Thread(target=self.algHandler.runAlgorithm)
            t.start()
        except:
            print("Error: unable to start thread for decoding")

    def canStartDecoding(self):
        """
        :return: boolean, string.
        true for 'can start decoding', false otherwise. msg - reason of false
        """
        self.dataHandler.updateDataModel()
        dataOk, msgData = self.isDataOk()
        if not dataOk:
            return dataOk, msgData
        if self.settingsModel.getChosenAlgorithm() == None:
            return False, "please choose a Decoding Algorithm"
        if self.algHandler.getDecodingMode() == None:
            return False, "please choose Decoding mode"
        return True, ""


    def updateDataModel(self):
        self.dataHandler.updateDataModel()

    def onCompleteChoosingData(self):
        # do whatever needed when initialize here
        self.dataHandler.updateDataModel()
        self.dataHandler.copyFilesTorawDataDir()

    def isDataOk(self):
        """
        true for 'dataOk', false otherwise. msg - reason of false
        :return: boolean, string

        """
        msg = 'please complete data selection first.\n' + str(
            self.dataModel.getNumOfFiles()) + ' files should be selected, but ' + str(
            self.dataHandler.getNumChosen()) + ' was selected.'
        return self.dataHandler.getNumChosen() == self.dataHandler.getNumFilesShouldBeSelected(), msg

    def setChosenAlgorithem(self, alg):
        """
        sets the chosen alg
        :param alg: string
        """
        self.settingsModel.chosenClassifier = alg

    def setFileName(self, num, path, name):
        """
        initiates setting of file name in dataHandler
        :param num: num of file to save (1 or 2)
        :param path: abs path to directory
        :param name: abs path to file
        """
        self.dataHandler.setFileName(num, path, name)

    def getFileName(self, num):
        """
        :param num: number of file to get (1 or 2)
        :return: abs path to file
        """
        return self.dataHandler.getFileName(num)
