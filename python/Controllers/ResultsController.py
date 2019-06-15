

class ResultsController:

    resultsLib = 'results/Decoding_Results'

    def getText(self):
        msg = 'When Decoding is done, you can find the results in: ' + self.resultsLib + '\n There, check out the accuracy graph & decoding results mat'
        return msg