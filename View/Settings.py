from Model.Settings_m import SettingsM
from Model.Data import Data
from tkinter import *


class Settings:

    def __init__(self, master, model):
        self.master = master
        master.title("Classification Settings")
        self.model = model
        target = self.createTargetFrame()
        classifierTypes = self.createClassifierTypeFrame()


    def createTargetFrame(self):
        frame = Frame()
        frame.label = Label(self.master, text="choose classification target:").pack()
        values = self.model.getFeatures()
        frame.values = Radiobutton().pack()  # how to add posibilities?
        return frame

    def createClassifierTypeFrame(self):
        frame = Frame()
        frame.label = Label(self.master, text="choose classifier type:").pack()
        values = self.model.getClassifierTypes()
        frame.values = Radiobutton().pack()  # how to add posibilities?
        return frame

root = Tk()
settings = Settings(root, SettingsM(Data([])))
root.mainloop()
