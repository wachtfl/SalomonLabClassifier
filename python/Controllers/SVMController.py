
from Controllers.IAlgController import IAlgController
import matlab.engine
from Model import Def
from enum import Enum
import sys
import io



class DECODING_MODES(Enum):
    SPATIAL = 1
    TEMPORAL = 2
    SPATIO_TEMPORAL = 3


class SVMController(IAlgController):


    def __init__(self, dataModel):
       self.decodingMode = None#DECODING_MODES.SPATIAL.value # default value
       self.dataModel = dataModel

    def getDecodingMode(self):
        return self.decodingMode

    def setDecodingMode(self, mode):
        if mode == Def.DECODING_MODES.SPATIAL:
            self.decodingMode = DECODING_MODES.SPATIAL.value
        if mode == Def.DECODING_MODES.TEMPORAL:
            self.decodingMode = DECODING_MODES.TEMPORAL.value
        if mode == Def.DECODING_MODES.SPATIO_TEMPORAL:
            self.decodingMode = DECODING_MODES.SPATIO_TEMPORAL.value

        print('from svm Controller, decoding mode set is: ' + mode, ' ,number: '+ str(self.decodingMode))

    def runAlgorithm(self):
        eng = matlab.engine.start_matlab()
        eng.configuration_script(self.dataModel.getPathToData()[0], self.dataModel.getPathToData()[1], self.decodingMode)
