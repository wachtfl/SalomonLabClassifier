import os

from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel

from Model.Settings_m import SettingsM
from Controllers.SettingsController import SettingsController

class CustomDropDown(DropDown):
    pass
    def select(self, feature):
        print(feature, ' was selected')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)
    text_input = ObjectProperty(None)


class Root(TabbedPanel):
    settingsController = SettingsController()

    files_to_save = 0
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    # e1 = NumericProperty(20)
    file_name1 = StringProperty('no file')
    file_name2 = StringProperty('no file')

    def showDecodingTypes(self, btn):
        self.createDropDown(self.settingsController.getDecodingTypes(), btn, self.onChooseDecodingMode)

    def onChooseDecodingMode(self, mode):
        self.settingsController.setDecodingMode(mode)

    def onChooseAlgorithem(self, alg):
        self.settingsController.setChosenAlgorithm(alg)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self, num):
        self.file_to_save = num
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, fileName):
        print('path chosen: ', path, 'file chosen: ', fileName[0])
        if self.file_to_save == 1:
            self.file_name1 = fileName[0]
            self.settingsController.setFileName(1, path, fileName[0])
        elif self.file_to_save == 2:
            self.file_name2 = fileName[0]
            self.settingsController.setFileName(2, path, fileName[0])
        self.dismiss_popup()

    def createWarningPopUp(self, msg):
        popup = Popup(title="warning", content=Label(text=msg), size_hint=(0.2, 0.2))
        popup.open()


    def onComplete(self):
        # can update settingsController here instead
        res, msg = self.settingsController.isDataOk()
        if res == False:
            self.createWarningPopUp(msg)
        else:
            self.settingsController.onCompleteChoosingData()
            self.switch_to(self.tab_list[2])


    def build(self):
        return GridLayout()

    def func(self, text):
        print(text)


    def createDropDown(self, list, but, funcOnSelect):
        dropdown = DropDown()
        for i in range(len(list)):
            btn = Button(text='%s' % str(list[i]), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            btn.bind(on_release=lambda btn: funcOnSelect(btn.text))
            dropdown.add_widget(btn)
        dropdown.open(but)


    def listAlgorithms(self, btn):
        self.createDropDown(self.settingsController.getAlgorithms(), btn, self.onChooseAlgorithem)

    def listFeatures(self, btn):
        self.createDropDown(self.settingsController.getFeatures(), btn, self.onChooseTarget)

    def onChooseTarget(self, target):
        self.settingsController.setTargetForClassification(target)

    def onStartDecoding(self):
        # set values if needed:
        self.settingsController.startDecoding()

    # def on_slider_value_changed(self, instance, value):
    #     self.e1 = value



class EEGApp(App):
    def build(self):
        root = Root()
        return root


if __name__ == '__main__':
    EEGApp().run()
