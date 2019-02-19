class SettingsM:

    def __init__(self, data):
        self.data = data

    target = None
    classifierTypes = []
    numOfPermutations = 1  # or another default value?
    testSet = 20  # or another default value?


    def getFeatures(self):
        return self.data.getFeatures()

    def getClassifierTypes(self):
        return self.classifierTypes
