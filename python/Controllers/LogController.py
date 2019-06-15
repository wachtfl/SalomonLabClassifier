

class LogController:

    def __init__(self):
        pass

    def getText(self):
        f = open('output_log.txt', 'r')
        text = f.read()
        return text
