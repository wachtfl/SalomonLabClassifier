"""
this class represents Results Controller
in charge on all logic behind representing the decoding results
"""

class ResultsController:

    resultsLib = 'SL Classification Results/Decoding_Results'

    def getText(self):
        """
        :return: msg to print in the view
        """
        msg = 'When Decoding is done, Accuracy map will show up on the screen. \nyou can find the results in: ' + self.resultsLib + '\nThere, check out the accuracy graph & decoding results matrix'
        return msg