"""
This module contains an algorithm-definitions class,
and a class that represents the algorithms available.
"""

class ALGORITHMS:
    SVM = "SVM"
    NN = "Neural Network"
    DT = "Desicion Tree"


class Algorithms:

    algorithms = [ALGORITHMS.SVM]             # <---- after implementing more algs, initialize them here.

    def getAlgorithms(self):
        """
        :return: a list of available algorithms (strings)
        """
        return self.algorithms
