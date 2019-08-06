"""
This is the program's main class. in charge of the initiating the
KIVY app, and some VIEW classes.
"""
import sys
import os


from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from python.Controllers.SettingsController import SettingsController
from python.Controllers.LogController import LogController
from python.Controllers.ResultsController import ResultsController
import threading
import time
import sys


from os import close, dup, O_WRONLY
import os

# old = dup(1)
# close(1)
# os.open("output_log.txt", O_WRONLY|os.O_CREAT) # should open on 1





class CustomDropDown(DropDown):
    pass
    def select(self, feature):
        print(feature, ' was selected')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    text_input = ObjectProperty(None)

class Root(TabbedPanel):
    rc = ResultsController()
    settingsController = SettingsController()
    files_to_save = 0
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    lc = LogController()
    log = StringProperty(lc.getText())
    resMsg = StringProperty(rc.getText())
    file_name1 = StringProperty(settingsController.getFileName(1))
    file_name2 = StringProperty(settingsController.getFileName(2))

    def showDecodingTypes(self, btn):
        """
        initiates gui to show decoding types
        :param btn: button pressed
        """
        self.createDropDown(self.settingsController.getDecodingTypes(), btn, self.onChooseDecodingMode)

    def onChooseDecodingMode(self, mode):
        """
        :param mode: mode chosen by user, string
        """
        self.settingsController.setDecodingMode(mode)

    def onChooseAlgorithem(self, alg):
        """
        :param alg: alg chosen by user, string
        """
        self.settingsController.setChosenAlgorithm(alg)

    def dismiss_popup(self):
        """
        make the popup disappear from GUI
        """
        self._popup.dismiss()

    def show_load(self, num):
        """
        loads the load Dialog
        :param num: num to file to choose (1 or 2)
        """
        self.file_to_save = num
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, fileName):
        """
        :param path: abs path to directory, passed by kivy
        :param fileName: abs path to file, passed by kivy
        """
        print('path chosen: ', path, 'file chosen: ', fileName[0])
        if self.file_to_save == 1:
            self.file_name1 = fileName[0]
            self.settingsController.setFileName(1, path, fileName[0])
            print('file chosen')
        elif self.file_to_save == 2:
            self.file_name2 = fileName[0]
            self.settingsController.setFileName(2, path, fileName[0])
            print('file chosen')
        self.dismiss_popup()

    def createPopUp(self, title, msg):
        """
        creates a popup on GUI, with title and a msg
        :param title: string
        :param msg: string
        """
        popup = Popup(title=title, content=Label(text=msg), size_hint=(0.2, 0.2))
        popup.open()


    def onComplete(self):
        """
        called when complete choosing data button is pressed
        """
        # can update settingsController here instead
        res, msg = self.settingsController.isDataOk()
        if res == False:
            self.createPopUp("Warning", msg)
        else:
            self.settingsController.onCompleteChoosingData()
            self.switch_to(self.tab_list[1])


    def build(self):
        return GridLayout()


    def createDropDown(self, list, but, funcOnSelect):
        """
        :param list: list of strings to show
        :param but: button to open to a drop down
        :param funcOnSelect: function to cal when a button is pressed
        :return:
        """
        dropdown = DropDown()
        for i in range(len(list)):
            btn = Button(text='%s' % str(list[i]), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: funcOnSelect(btn.text))
            dropdown.add_widget(btn)
        dropdown.open(but)

    def updateLog(self):
        """
        initiates a thread for logging
        """
        pass
        t = threading.Thread(target=self.up)
        t.start()


    def up(self):
        """
        logging
        """
        while (True):
            sys.stdout = open('output_log.txt', 'w')
            self.log = self.lc.getText()
            print(self.log)
            time.sleep(1)


    def listAlgorithms(self, btn):
        """
        shows a list of algorithms on the specified button press
        :param btn: btn to open
        """
        self.createDropDown(self.settingsController.getAlgorithms(), btn, self.onChooseAlgorithem)

    def listFeatures(self, btn):
        """
        shows a list of data features on the specified button press
        :param btn: btn to open
        """
        self.createDropDown(self.settingsController.getFeatures(), btn, self.onChooseTarget)

    def onChooseTarget(self, target):
        """
        initiates a set of the chosen target
        :param target: string
        """
        self.settingsController.setTargetForClassification(target)

    def onStartDecoding(self):
        """
        call when btn start decoding is pressed.
        initiates checks if can start decoding, and initiates start decoding.
        """
        # set values if needed:
        res, msg = self.settingsController.canStartDecoding()
        if res == False:
            self.createPopUp("Warning", msg)
        else:
            msg = "Decoding is starting. please wait a while..."
            self.createPopUp("Success!", msg)
            self.settingsController.startDecoding()
            self.switch_to(self.tab_list[0])


class EEGApp(App):
    def build(self):
        root = Root()
        # root.updateLog()
        return root


if __name__ == '__main__':
    EEGApp().run()

    # close(1)
    # dup(old)  # should dup to 1
    # close(old)  # get rid of left overs


