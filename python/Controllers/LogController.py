"""
this class represents the Logger.
in charge of reading the log file
"""
class LogController:

    def __init__(self):
        pass

    def getText(self):
        """
        :return: context of log file
        """
        f = open('output_log.txt', 'r')
        text = f.read()
        return text
