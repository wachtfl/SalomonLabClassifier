
from Controllers.IAlgController import IAlgController


class SVMController(IAlgController):

    def SVMController(self):
       decodingMode = None

    def getDecodingMode(self):
        return self.decodingMode

    def setDecodingMode(self, mode):
        self.decodingMode = mode
        print('from SVM Controller, decoding mode set is: ' + self.decodingMode)


